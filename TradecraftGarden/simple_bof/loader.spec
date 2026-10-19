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
