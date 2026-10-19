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
