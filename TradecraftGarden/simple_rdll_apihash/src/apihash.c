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
