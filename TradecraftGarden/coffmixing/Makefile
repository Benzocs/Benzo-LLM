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
