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

DECLSPEC_IMPORT PVOID             WINAPI NTDLL$RtlAddVectoredExceptionHandler(ULONG, PVECTORED_EXCEPTION_HANDLER);
DECLSPEC_IMPORT WINBOOL           WINAPI KERNEL32$ReadProcessMemory (HANDLE hProcess, LPCVOID lpBaseAddress, LPVOID lpBuffer, SIZE_T nSize, SIZE_T *lpNumberOfBytesRead);
DECLSPEC_IMPORT PRUNTIME_FUNCTION WINAPI KERNEL32$RtlLookupFunctionEntry(DWORD64, PDWORD64, PVOID);
DECLSPEC_IMPORT PVOID             WINAPI KERNEL32$RtlVirtualUnwind(DWORD, DWORD64, DWORD64, PRUNTIME_FUNCTION, PCONTEXT, PVOID*, PDWORD64, PVOID*);

/* I had some help from Google Gemini with the basic walk */
EXCEPTION_DISPOSITION MyHandler(PEXCEPTION_RECORD ExceptionRecord, ULONG64 EstablisherFrame, PCONTEXT ContextRecord, PDISPATCHER_CONTEXT DispatcherContext) {
	if (ExceptionRecord->ExceptionCode == EXCEPTION_BREAKPOINT) {
		CONTEXT * liveCtx = ContextRecord;
		CONTEXT   walkCtx = *ContextRecord;

		dprintf("Caught int3. Stack walk time!");

		for (int frameCount = 0; walkCtx.Rip != 0 && frameCount < 32; frameCount++) {
			ULONG64 rip = walkCtx.Rip;
			SIZE_T read;

			/* print our stack frame */
			dprintf("[%02d] %p", frameCount, rip);

			/* check if RIP is sane... terminate walk if it's not */
			if (!KERNEL32$ReadProcessMemory((HANDLE)-1, (LPCVOID)walkCtx.Rip, &rip, sizeof(PULONG64), &read)) {
				dprintf("Bad RIP! %p - Truncating stack walk", rip);
				break;
			}

			/* let's ask the OS for the .pdata information */
			ULONG64 imageBase;
			PRUNTIME_FUNCTION pFunctionEntry = KERNEL32$RtlLookupFunctionEntry(walkCtx.Rip, &imageBase, NULL);

			if (pFunctionEntry != NULL) {
				/* we found .pdata for this function, let's simulate the epilogue on walkCtx and find the next frame */
				PVOID handlerData;
				ULONG64 establisherFrame;
				KERNEL32$RtlVirtualUnwind(0, imageBase, walkCtx.Rip, pFunctionEntry, &walkCtx, &handlerData, &establisherFrame, NULL);
			}
			else {
				/* no .pdata? Assume it's a leaf and pop the return address off of the stack */
				walkCtx.Rip = *(PULONG64)(walkCtx.Rsp);
				walkCtx.Rsp += 8;
			}
		}

		/* advance rip to move past out int3 instruction */
		liveCtx->Rip += 1;

		/* this enum value is different from a VEH's long return value. Don't mistake the two */
		return ExceptionContinueExecution;
	}

	return ExceptionContinueSearch;
}
