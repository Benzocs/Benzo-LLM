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
