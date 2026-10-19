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
