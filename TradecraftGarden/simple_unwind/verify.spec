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
