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
