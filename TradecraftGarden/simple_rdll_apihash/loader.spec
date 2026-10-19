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
