rule Generic_ReflectiveDllInjection_0236c87e {
	meta:
		description = "ReflectiveDllInjection: Loading libraries from memory into host processes since 2008"
		author = "Stephen Fewer (original), AFF-WG (TCG integration)"
		date = "2026-06-28"
		reference = "https://github.com/stephenfewer/ReflectiveDLLInjection, https://tradecraftgarden.org/rdlli.html"
		arch_context = "x64"
		scan_context = "file, memory"
		os = "windows"
		license = "BSD"
		generator = "Crystal Palace"
	strings:
		// ----------------------------------------
		// Function: ReflectiveLoader
		// ----------------------------------------
		/*
		 * 48 83 EC 38                   sub rsp, 0x38
		 * 48 8D 3D 00 00 00 00          lea rdi, [my_dll]
		 * 65 48 8B 04 25 60 00 00 00    mov rax, qword ptr gs:[0x60]
		 * (Score: 28)
		 */
		$r0_ReflectiveLoader = { 48 83 EC 38 48 8D 3D ?? ?? ?? ?? 65 48 8B 04 25 60 00 00 00 }

		/*
		 * 4D 01 CB                      add r11, r9
		 * 41 8B 4B 20                   mov ecx, dword ptr [r11+0x20]
		 * 4C 01 C9                      add rcx, r9
		 * 45 8B 43 24                   mov r8d, dword ptr [r11+0x24]
		 * (Score: 72)
		 */
		$r1_ReflectiveLoader = { 4D 01 CB 41 8B 4B 20 4C 01 C9 45 8B 43 24 }

		/*
		 * 41 8B 43 1C                   mov eax, dword ptr [r11+0x1C]
		 * 4C 01 C8                      add rax, r9
		 * 41 0F B7 10                   movzx edx, word ptr [r8]
		 * 44 8B 2C 90                   mov r13d, dword ptr [rax+rdx*4]
		 * (Score: 28)
		 */
		$r2_ReflectiveLoader = { 41 8B 43 1C 4C 01 C8 41 0F B7 10 44 8B 2C 90 }

		/*
		 * 48 83 C0 01                   add rax, 1
		 * 48 83 C2 01                   add rdx, 1
		 * 0F B6 48 FF                   movzx ecx, byte ptr [rax-1]
		 * 88 4A FF                      mov byte ptr [rdx-1], cl
		 * (Score: 24)
		 */
		$r3_ReflectiveLoader = { 48 83 C0 01 48 83 C2 01 0F B6 48 FF 88 4A FF }

		/*
		 * 41 8B 51 14                   mov edx, dword ptr [r9+0x14]
		 * 48 01 FA                      add rdx, rdi
		 * 45 8B 41 10                   mov r8d, dword ptr [r9+0x10]
		 * 4D 85 C0                      test r8, r8
		 * (Score: 72)
		 */
		$r4_ReflectiveLoader = { 41 8B 51 14 48 01 FA 45 8B 41 10 4D 85 C0 }

		/*
		 * 0F B7 D2                      movzx edx, dx
		 * 8B 40 10                      mov eax, dword ptr [rax+0x10]
		 * 48 29 C2                      sub rdx, rax
		 * 8B 04 91                      mov eax, dword ptr [rcx+rdx*4]
		 * (Score: 23)
		 */
		$r5_ReflectiveLoader = { 0F B7 D2 8B 40 10 48 29 C2 8B 04 91 }

		/*
		 * 49 83 C5 14                   add r13, 0x14
		 * 4C 89 EF                      mov rdi, r13
		 * 41 8B 45 0C                   mov eax, dword ptr [r13+0xC]
		 * 85 C0                         test eax, eax
		 * (Score: 29)
		 */
		$r6_ReflectiveLoader = { 49 83 C5 14 4C 89 EF 41 8B 45 0C 85 C0 }

		/*
		 * 0F B7 02                      movzx eax, word ptr [rdx]
		 * 25 FF 0F 00 00                and eax, 0xFFF
		 * 4E 01 14 00                   add qword ptr [rax+r8], r10
		 * (Score: 22)
		 */
		$r7_ReflectiveLoader = { 0F B7 02 25 FF 0F 00 00 4E 01 14 00 }

		/*
		 * 0F B7 02                      movzx eax, word ptr [rdx]
		 * 25 FF 0F 00 00                and eax, 0xFFF
		 * 66 46 01 14 00                add word ptr [rax+r8], r10w
		 * (Score: 22)
		 */
		$r8_ReflectiveLoader = { 0F B7 02 25 FF 0F 00 00 66 46 01 14 00 }

		/*
		 * 89 C0                         mov eax, eax
		 * 48 83 E8 08                   sub rax, 8
		 * 48 89 C1                      mov rcx, rax
		 * 48 D1 E9                      shr rcx, 1
		 * 49 8D 53 08                   lea rdx, [r11+8]
		 * (Score: 43)
		 */
		$r9_ReflectiveLoader = { 89 C0 48 83 E8 08 48 89 C1 48 D1 E9 49 8D 53 08 }

	condition:
		5 of them
}

