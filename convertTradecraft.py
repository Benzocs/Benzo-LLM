import os
from pathlib import Path

# ================= SOZLAMALAR =================
SOURCE_DIR = Path("TradecraftGarden")
OUTPUT_FILE = Path("tradecraft_garden_compilation.md")
# Indekslash uchun kerakli fayl kengaytmalari
VALID_EXTENSIONS = {'.c', '.h', '.txt', '.spec', '.md', '.py', '.sh', '.bat', '.ps1'}
# ===============================================

def convert_to_markdown():
    if not SOURCE_DIR.exists():
        print(f"Xato: '{SOURCE_DIR}' papkasi topilmadi.")
        return

    content_parts = []
    content_parts.append("# Tradecraft Garden (Crystal Kit) - Full Source Code\n")
    content_parts.append("This document contains the complete source code and documentation for the Tradecraft Garden project, focusing on Position-Independent Code (PIC) and Reflective DLL Injection.\n\n---\n")

    file_count = 0
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            # Makefile kabi kengaytmasiz fayllarni ham olish
            if ext in VALID_EXTENSIONS or file == "Makefile":
                filepath = Path(root) / file
                # Source dir ga nisbatan nisbiy yo'l (sarlavha uchun)
                rel_path = filepath.relative_to(SOURCE_DIR).as_posix()
                
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                        code = f.read()
                except Exception as e:
                    print(f"O'qishda xato: {filepath} -> {e}")
                    continue

                # Fayl kengaytmasiga qarab kod tilini aniqlash (Markdown syntax highlighting)
                lang = ext.strip('.') if ext else 'text'
                if lang in ['txt', 'spec']:
                    lang = 'text'
                
                # Markdown bo'limini yaratish
                # RAG skriptingiz sarlavhalar (#) bo'yicha bo'lishi uchun '##' ishlatamiz
                part = f"## File: {rel_path}\n\n"
                part += f"```{lang}\n{code}\n```\n\n"
                content_parts.append(part)
                file_count += 1

    # Barchasini birlashtirib saqlash
    OUTPUT_FILE.write_text("".join(content_parts), encoding='utf-8')
    print(f"Muvaffaqiyatli yakunlandi! {file_count} ta fayl birlashtirildi.")
    print(f"Natija: {OUTPUT_FILE} ({(OUTPUT_FILE.stat().st_size / 1024):.1f} KB)")

if __name__ == "__main__":
    convert_to_markdown()