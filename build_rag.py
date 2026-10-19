"""
Obsidian -> lokal RAG indekser (Ollama embedding)

  - Obsidian markdown'ni tozalash: frontmatter, [[wikilink]], ![[embed]],
    %%izoh%%, callout, ^block-id, rasm va havola. Kod bloklari va inline kod buzilmaydi.
  - Sarlavha bo'yicha chunking, har chunkka bo'lim yo'li (breadcrumb) qo'shiladi.
  - Incremental: o'zgarmagan chunklar qayta embedding qilinmaydi (kesh).
  - Parallel batch embedding, retry, progress + ETA + hajm hisobi.
  - Ctrl+C bo'lsa ham yig'ilgan natija saqlanadi, keyingi ishga tushirishda davom etadi.

Ishga tushirish:
  python build_rag.py                    # to'liq build
  python build_rag.py --dry              # faqat statistika (Ollama kerak emas)
  python build_rag.py --preview "fayl.md"  # bitta faylning chunklarini ko'rish
"""

import hashlib
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path

import ollama

sys.stdout.reconfigure(encoding="utf-8")

# ============================ SOZLAMALAR ============================
VAULT = Path(r"C:\Tools\RedTeam-SecondBrain")
FOLDERS = ["CRTL", "CRTO", "HackTheBox", "WKL"]
OUT_DB = Path("rag_database.json")
LOG_FILE = Path("build_rag.log")

EMBED_MODEL = "nomic-embed-text"
OLLAMA_HOST = "http://localhost:11434"
REQUEST_TIMEOUT = 300   # soniya
BATCH_SIZE = 32         # bitta so'rovdagi matnlar soni
WORKERS = 2             # parallel so'rovlar (OLLAMA_NUM_PARALLEL bilan mos bo'lsin)
MAX_CHARS = 1200        # chunk maksimal uzunligi (belgi)
MIN_CHARS = 200         # bundan qisqa bo'lim keyingi chunk bilan birlashtiriladi
OVERLAP_BLOCKS = 1      # keyingi chunkka o'tadigan oldingi bloklar soni
EMBED_DIM_GUESS = 768   # nomic-embed-text o'lchami (hajm taxmini uchun)
# ====================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8", mode="a"),
    ],
)
log = logging.getLogger("build_rag")

# ---------------------- Obsidian tozalash ----------------------
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---[ \t]*(?:\n|\Z)", re.S)
CALLOUT_RE = re.compile(r"^(\s*>+\s*)\[![A-Za-z]+\][+-]?\s*")
INLINE_CODE_RE = re.compile(r"(`[^`\n]+`)")
COMMENT_RE = re.compile(r"%%.*?%%")
EMBED_RE = re.compile(r"!\[\[([^\]|#]*)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
WIKI_RE = re.compile(r"\[\[([^\]|#]*)(?:#([^\]|]*))?(?:\|([^\]]*))?\]\]")
IMG_RE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
HL_RE = re.compile(r"==([^=\n]+)==")
BLOCKID_RE = re.compile(r"\s+\^[A-Za-z0-9-]+\s*$")

HEAD_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


def _wiki(m):
    target = (m.group(1) or "").strip()
    heading = (m.group(2) or "").strip()
    alias = m.group(3)
    if alias:
        return alias.strip()
    if target and heading:
        return f"{target} > {heading}"
    return target or heading


def _clean_text(s):
    s = COMMENT_RE.sub("", s)
    s = EMBED_RE.sub(lambda m: f"[ilova: {m.group(1).strip()}]", s)
    s = WIKI_RE.sub(_wiki, s)
    s = IMG_RE.sub(lambda m: m.group(1), s)
    s = LINK_RE.sub(lambda m: m.group(1), s)
    s = HL_RE.sub(lambda m: m.group(1), s)
    s = BLOCKID_RE.sub("", s)
    return s


def clean_line(line):
    line = CALLOUT_RE.sub(lambda m: m.group(1), line)
    parts = INLINE_CODE_RE.split(line)  # juft indeks: oddiy matn, toq: `inline code`
    return "".join(p if i % 2 else _clean_text(p) for i, p in enumerate(parts)).rstrip()


def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta, key = {}, None
    for line in m.group(1).split("\n"):
        if re.match(r"^\s+-\s+", line) and key and isinstance(meta.get(key), list):
            meta[key].append(line.split("-", 1)[1].strip().strip("\"'"))
        elif re.match(r"^[\w\- ]+:", line):
            k, _, v = line.partition(":")
            key = k.strip().lower()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                meta[key] = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
            elif v:
                meta[key] = v.strip("\"'")
            else:
                meta[key] = []
    return meta, text[m.end():]


# ---------------------- Chunking ----------------------
def to_sections(text):
    """[(bo'lim_yo'li, [bloklar])]. Kod bloki bitta atomik blok bo'lib qoladi."""
    sections, blocks, buf = [], [], []
    stack, crumb, fence = [], "", None

    def flush():
        if buf:
            s = "\n".join(buf).strip("\n")
            if s.strip():
                blocks.append(s)
            buf.clear()

    for raw in text.split("\n"):
        if fence:  # kod bloki ichida: hech narsaga tegmaymiz
            buf.append(raw)
            s = raw.strip()
            if len(s) >= 3 and set(s) == {fence[0]}:
                fence = None
                flush()
            continue

        m = FENCE_RE.match(raw)
        if m:
            flush()
            fence = m.group(1)[:3]
            buf.append(raw)
            continue

        line = clean_line(raw)
        h = HEAD_RE.match(line)
        if h:
            flush()
            if blocks:
                sections.append((crumb, list(blocks)))
                blocks.clear()
            level, title = len(h.group(1)), h.group(2).strip()
            stack = [(l, t) for l, t in stack if l < level] + [(level, title)]
            crumb = " > ".join(t for _, t in stack)
            continue

        if not line.strip():
            flush()
        else:
            buf.append(line)

    flush()
    if blocks:
        sections.append((crumb, list(blocks)))
    return sections


def _join_len(parts):
    return len("\n\n".join(parts))


def split_oversized(block):
    """MAX_CHARS dan katta blokni bo'laklarga bo'ladi. Kod bloki bo'lsa fence'ni har bo'lakka qaytaradi."""
    if len(block) <= MAX_CHARS:
        return [block]
    lines = block.split("\n")
    head = tail = ""
    if FENCE_RE.match(lines[0]):
        head = lines[0]
        if len(lines) > 1 and FENCE_RE.match(lines[-1]):
            tail, lines = lines[-1], lines[1:-1]
        else:
            lines = lines[1:]
    limit = MAX_CHARS - len(head) - len(tail) - 2

    def wrap(body):
        parts = ([head] if head else []) + body + ([tail] if tail else [])
        return "\n".join(parts)

    out, cur = [], []
    for ln in lines:
        while len(ln) > limit:  # juda uzun qatorni kesish
            if cur:
                out.append(wrap(cur))
                cur = []
            out.append(wrap([ln[:limit]]))
            ln = ln[limit:]
        if cur and sum(len(x) + 1 for x in cur) + len(ln) > limit:
            out.append(wrap(cur))
            cur = []
        cur.append(ln)
    if cur:
        out.append(wrap(cur))
    return out


def pack(blocks):
    """Bloklarni MAX_CHARS ichiga joylaydi, oxirgi blok(lar)ni keyingi chunkka overlap sifatida beradi."""
    pieces = [p for b in blocks for p in split_oversized(b)]
    chunks, cur = [], []
    for p in pieces:
        if cur and _join_len(cur + [p]) > MAX_CHARS:
            chunks.append("\n\n".join(cur))
            cur = cur[-OVERLAP_BLOCKS:] if OVERLAP_BLOCKS else []
            if cur and _join_len(cur + [p]) > MAX_CHARS:
                cur = []
        cur.append(p)
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def process_file(path: Path):
    raw = path.read_text(encoding="utf-8-sig", errors="replace").replace("\r\n", "\n")
    meta, body = parse_frontmatter(raw)
    title = str(meta.get("title") or path.stem)
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    tag_txt = " ".join("#" + str(t).lstrip("#") for t in tags)
    try:
        rel = path.relative_to(VAULT).as_posix()
    except ValueError:
        rel = path.name

    items = []  # (bo'lim, matn)
    for crumb, blocks in to_sections(body):
        for text in pack(blocks):
            if items and items[-1][0] == crumb and len(text) < MIN_CHARS:
                items[-1] = (crumb, items[-1][1] + "\n\n" + text)
            else:
                items.append((crumb, text))

    out = []
    for crumb, text in items:
        if not text.strip():
            continue
        head = f"title: {title}"
        if crumb:
            head += f" | section: {crumb}"
        if tag_txt:
            head += f" | tags: {tag_txt}"
        # nomic-embed-text v1.5 hujjat uchun "search_document: " prefiksini kutadi
        embed_text = f"search_document: {head}\n{text}"
        cid = hashlib.sha1(f"{EMBED_MODEL}\n{embed_text}".encode("utf-8")).hexdigest()
        out.append({
            "id": cid,
            "source": rel,
            "title": title,
            "section": crumb,
            "tags": tags,
            "content": text,
            "embed_text": embed_text,
        })
    return out


def collect_files():
    files = []
    for folder in FOLDERS:
        base = VAULT / folder
        if not base.exists():
            log.warning("Papka topilmadi: %s", base)
            continue
        for p in base.rglob("*.md"):
            if any(part.startswith(".") for part in p.relative_to(VAULT).parts):
                continue  # .trash, .obsidian
            files.append(p)
            
    # ★ YANGI: MITRE faylini qo'shish (skript joylashgan papkadan qidiradi)
    mitre_file = Path("mitre_full_infrastructure_english.md")
    if mitre_file.exists():
        files.append(mitre_file.resolve())
        log.info("MITRE fayli topildi va indekslashga qo'shildi: %s", mitre_file.resolve())
    else:
        log.warning("MITRE fayli topilmadi: %s", mitre_file.absolute())

    tcg_file = Path("tradecraft_garden_compilation.md")
    if tcg_file.exists():
        files.append(tcg_file.resolve())
        log.info("Tradecraft Garden fayli topildi va indekslashga qo'shildi")

    return sorted(set(files))


# ---------------------- Ollama ----------------------
def check_ollama(client):
    try:
        resp = client.list()
    except Exception as e:
        log.error("Ollama'ga ulanib bo'lmadi: %s -> 'ollama serve' ishlayotganini tekshiring", e)
        sys.exit(1)
    models = resp.models if hasattr(resp, "models") else resp["models"]
    names = [(getattr(m, "model", None) or m.get("model", "")) for m in models]
    base = EMBED_MODEL.split(":")[0]
    if not any(n.split(":")[0] == base for n in names):
        log.error("Model topilmadi: %s -> 'ollama pull %s' buyrug'ini bajaring", EMBED_MODEL, EMBED_MODEL)
        sys.exit(1)
    log.info("Ollama OK, %s tayyor", EMBED_MODEL)


def embed_texts(client, texts):
    """Batch embedding. Xato bo'lsa qayta uradi, so'ng batch'ni ikkiga bo'lib alohida yuboradi."""
    last = None
    for _ in range(2):
        try:
            res = client.embed(model=EMBED_MODEL, input=texts)
            vecs = res["embeddings"]
            if len(vecs) == len(texts):
                return vecs
            last = RuntimeError("javoblar soni mos emas")
        except Exception as e:
            last = e
        time.sleep(1.5)
    if len(texts) == 1:
        log.error("Embedding o'tkazib yuborildi: %s", last)
        return [None]
    mid = len(texts) // 2
    return embed_texts(client, texts[:mid]) + embed_texts(client, texts[mid:])


# ---------------------- Kesh va saqlash ----------------------
def load_cache():
    if not OUT_DB.exists():
        return {}
    try:
        data = json.loads(OUT_DB.read_text(encoding="utf-8"))
    except Exception as e:
        log.warning("Eski baza o'qilmadi, keshsiz boshlanadi: %s", e)
        return {}
    if not isinstance(data, dict) or data.get("meta", {}).get("model") != EMBED_MODEL:
        log.info("Mavjud baza boshqa formatda yoki modelda, kesh ishlatilmaydi")
        return {}
    cache = {r["id"]: r["embedding"] for r in data.get("chunks", []) if "id" in r}
    log.info("Keshdan yuklandi: %d ta embedding (holat: %s)", len(cache), data["meta"].get("status", "?"))
    return cache


def save_db(chunks, vectors, status):
    records = []
    for c in chunks:
        v = vectors.get(c["id"])
        if v is None:
            continue
        rec = {k: c[k] for k in ("id", "source", "title", "section", "tags", "content")}
        rec["embedding"] = v
        records.append(rec)
    dims = len(records[0]["embedding"]) if records else None
    payload = {
        "meta": {
            "model": EMBED_MODEL,
            "dims": dims,
            "count": len(records),
            "status": status,
            "chunk_max_chars": MAX_CHARS,
            "built_at": datetime.now().isoformat(timespec="seconds"),
            "doc_prefix": "search_document: ",
            "query_prefix": "search_query: ",
        },
        "chunks": records,
    }
    tmp = OUT_DB.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False)
    os.replace(tmp, OUT_DB)
    return len(records)


# ---------------------- Log yordamchilari ----------------------
def fmt_dur(sec):
    sec = int(sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def log_progress(done, total, start):
    elapsed = time.time() - start
    rate = done / elapsed if elapsed else 0
    left = total - done
    eta = left / rate if rate else 0
    finish = (datetime.now() + timedelta(seconds=eta)).strftime("%H:%M")
    filled = int(30 * done / total)
    bar = "#" * filled + "-" * (30 - filled)
    log.info("[%s] %5.1f%%  %d/%d | %.1f chunk/s | o'tdi %s | qoldi %d ta, ~%s | tugash ~%s",
             bar, done * 100 / total, done, total, rate,
             fmt_dur(elapsed), left, fmt_dur(eta), finish)


# ---------------------- Asosiy oqim ----------------------
def main():
    if "--preview" in sys.argv:
        p = Path(sys.argv[sys.argv.index("--preview") + 1])
        for c in process_file(p):
            print("-" * 70)
            print(c["embed_text"])
        return

    dry = "--dry" in sys.argv
    t0 = time.time()
    log.info("=" * 70)
    log.info("BUILD RAG | model=%s | batch=%d | workers=%d | chunk<=%d belgi",
             EMBED_MODEL, BATCH_SIZE, WORKERS, MAX_CHARS)

    client = ollama.Client(host=OLLAMA_HOST, timeout=REQUEST_TIMEOUT)
    if not dry:
        check_ollama(client)

    files = collect_files()
    log.info("1/4 Fayllar: %d ta .md topildi", len(files))

    chunks, read_errors = [], 0
    for i, p in enumerate(files, 1):
        try:
            chunks.extend(process_file(p))
        except Exception as e:
            read_errors += 1
            log.warning("O'qish xatosi: %s -> %s", p.name, e)
        if i % 100 == 0 or i == len(files):
            log.info("   chunking: %d/%d fayl, %d chunk", i, len(files), len(chunks))

    total_chars = sum(len(c["content"]) for c in chunks)
    log.info("2/4 Chunklar: %d ta | jami %s belgi | taxminan %s token",
             len(chunks), f"{total_chars:,}", f"{total_chars // 3:,}")

    cache = load_cache()
    vectors = dict(cache)
    need, reused = {}, 0
    for c in chunks:
        if c["id"] in cache:
            reused += 1
        elif c["id"] not in need:
            need[c["id"]] = c["embed_text"]

    est_mb = (total_chars * 1.1 + len(chunks) * (EMBED_DIM_GUESS * 14 + 200)) / 1e6
    log.info("3/4 Kesh: %d chunk keshdan | %d ta yangi embedding kerak | DB hajmi taxminan %.1f MB",
             reused, len(need), est_mb)

    if dry:
        log.info("--dry rejimi: embedding va saqlash o'tkazib yuborildi")
        return

    ids = list(need)
    failed = 0
    if ids:
        batches = [ids[s:s + BATCH_SIZE] for s in range(0, len(ids), BATCH_SIZE)]
        log.info("4/4 Embedding: %d ta chunk, %d ta batch, %d parallel",
                 len(ids), len(batches), WORKERS)
        start = time.time()
        done = 0
        ex = ThreadPoolExecutor(max_workers=WORKERS)
        futures = {ex.submit(embed_texts, client, [need[i] for i in b]): b for b in batches}
        try:
            for fut in as_completed(futures):
                b = futures[fut]
                for cid, vec in zip(b, fut.result()):
                    if vec is None:
                        failed += 1
                    else:
                        vectors[cid] = vec
                done += len(b)
                log_progress(done, len(ids), start)
        except KeyboardInterrupt:
            ex.shutdown(wait=False, cancel_futures=True)
            n = save_db(chunks, vectors, "partial")
            log.warning("To'xtatildi. %d ta chunk qisman saqlandi. Qayta ishga tushirsangiz shu joydan davom etadi.", n)
            sys.exit(130)
        finally:
            ex.shutdown(wait=False, cancel_futures=True)
    else:
        log.info("4/4 Embedding: yangi chunk yo'q, hammasi keshdan olindi")

    missing = sum(1 for c in chunks if c["id"] not in vectors)
    n = save_db(chunks, vectors, "complete" if missing == 0 else "incomplete")
    size_mb = OUT_DB.stat().st_size / 1e6

    log.info("=" * 70)
    log.info("TAYYOR | %d chunk -> %s (%.1f MB) | umumiy vaqt %s",
             n, OUT_DB, size_mb, fmt_dur(time.time() - t0))
    if failed or missing or read_errors:
        log.warning("Muammolar: embedding xato=%d, o'qish xato=%d, yozilmagan=%d",
                    failed, read_errors, missing)


if __name__ == "__main__":
    main()