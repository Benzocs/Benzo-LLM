/*
 * Copyright 2026 Adversary Fan Fiction Writers Guild
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

void BeaconOutput(int type, char * data, int len);

/*
 * This is IMPORTFUNCS with one other entry. We use this struct to pass function pointers to a
 * PICO using the import command in our Crystal Palace .spec file.
 */
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
	__typeof__(BeaconOutput)   * BeaconOutput;
} BOFIMPORTS;

typedef void (*BOFMAIN)(char * args, int len);

/*
 * This is our BOF runner...
 */
void run_bof(char * src, char * args, int alen) {
	BOFIMPORTS    funcs;
	char        * dstCode;
	char        * dstData;

	/* setup our IMPORTFUNCS data structure (with one additional entry) */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;
	funcs.BeaconOutput   = BeaconOutput;

	/* allocate memory for our PICO */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );

	/* load our pico into our destination address, thanks! */
	PicoLoad((IMPORTFUNCS *)&funcs, src, dstCode, dstData);

	/* execute our pico */
	((BOFMAIN)PicoEntryPoint(src, dstCode)) (args, alen);
}

/*
 * This is the one piece of the Beacon API we need to define. Everything else is merged into the BOF by
 * Crystal Palace. Any output is (eventually) passed through this function.
 */
void BeaconOutput(int type, char * data, int len) {
	dprintf("BeaconOut[%x]: %s", type, data);
}

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __BOFDATA__[0] __attribute__((section("my_data")));

/*
 * The entry point to our little BOF runner...
 */
void go() {
	run_bof((char *)__BOFDATA__, NULL, 0);
}
