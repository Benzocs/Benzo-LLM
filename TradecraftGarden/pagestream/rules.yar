rule TCG_GuardExec_2e508ce9 {
	meta:
		description = "PageStream rDLL: Use VEHs and guard pages to limit DLL visibility in eXecutable memory"
		author = "Adversary Fan Fiction Writers Guild"
		date = "2026-06-28"
		reference = "https://tradecraftgarden.org/pagestream.html"
		arch_context = "x64"
		scan_context = "file, memory"
		os = "windows"
		license = "BSD"
		generator = "Crystal Palace"
	strings:
		// ----------------------------------------
		// Function: TrackPage
		// ----------------------------------------
		/*
		 * 48 69 C0 56 55 55 55          imul rax, 0x55555556
		 * 48 C1 E8 20                   shr rax, 0x20
		 * 89 D1                         mov ecx, edx
		 * C1 F9 1F                      sar ecx, 0x1F
		 * (Score: 144)
		 */
		$r0_TrackPage = { 48 69 C0 56 55 55 55 48 C1 E8 20 89 D1 C1 F9 1F }

		/*
		 * 48 8D 35 00 00 00 00          lea rsi, [.bss]
		 * 8B 15 18 00 00 00             mov edx, dword ptr [.bss+0x18]
		 * 48 63 C2                      movsxd rax, edx
		 * 48 69 C0 56 55 55 55          imul rax, 0x55555556
		 * (Score: 146)
		 */
		$r1_TrackPage = { 48 8D 35 ?? ?? ?? ?? 8B 15 ?? ?? ?? ?? 48 63 C2 48 69 C0 56 55 55 55 }

		/*
		 * 48 69 D2 56 55 55 55          imul rdx, 0x55555556
		 * 48 C1 EA 20                   shr rdx, 0x20
		 * 89 C1                         mov ecx, eax
		 * C1 F9 1F                      sar ecx, 0x1F
		 * (Score: 530)
		 */
		$r2_TrackPage = { 48 69 D2 56 55 55 55 48 C1 EA 20 89 C1 C1 F9 1F }

		// ----------------------------------------
		// Function: VEHHandler
		// ----------------------------------------
		/*
		 * 48 8B 11                      mov rdx, qword ptr [rcx]
		 * B8 00 00 00 00                mov eax, 0
		 * 81 3A 01 00 00 80             cmp dword ptr [rdx], 0x80000001
		 * (Score: 521)
		 */
		$r3_VEHHandler = { 48 8B 11 B8 00 00 00 00 81 3A 01 00 00 80 }

		/*
		 * B9 00 10 00 00                mov ecx, 0x1000
		 * F3 A4                         rep movsb
		 * BA 00 10 00 00                mov edx, 0x1000
		 * (Score: 65)
		 */
		$r4_VEHHandler = { B9 00 10 00 00 F3 A4 BA 00 10 00 00 }

		// ----------------------------------------
		// Function: GuardSections
		// ----------------------------------------
		/*
		 * 25 00 00 00 20                and eax, 0x20000000
		 * 83 F8 01                      cmp eax, 1
		 * 19 F6                         sbb esi, esi
		 * 83 E6 E4                      and esi, 0xFFFFFFE4
		 * 83 C6 20                      add esi, 0x20
		 * (Score: 150)
		 */
		$r5_GuardSections = { 25 00 00 00 20 83 F8 01 19 F6 83 E6 E4 83 C6 20 }

		// ----------------------------------------
		// Function: go
		// ----------------------------------------
		/*
		 * E8 87 01 00 00                call SizeOfDLL
		 * 48 8D 15 20 00 00 00          lea rdx, [.bss+0x20]
		 * 48 8D 8A 00 02 00 00          lea rcx, [rdx+0x200]
		 * (Score: 140)
		 */
		$r6_go = { E8 ?? ?? ?? ?? 48 8D 15 ?? ?? ?? ?? 48 8D 8A 00 02 00 00 }

		// ----------------------------------------
		// Function: freeAndRun
		// ----------------------------------------
		/*
		 * 48 83 EC 28                   sub rsp, 0x28
		 * 48 89 D3                      mov rbx, rdx
		 * 4C 89 C6                      mov rsi, r8
		 * 41 B8 00 80 00 00             mov r8d, 0x8000
		 * (Score: 44)
		 */
		$r7_freeAndRun = { 48 83 EC 28 48 89 D3 4C 89 C6 41 B8 00 80 00 00 }

	condition:
		5 of them
}

