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
