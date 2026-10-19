#
# prepare a PICO for execution as a BOF
#

x86:
	# set the entrypoint of this PICO to the first argument passed to this file
	entry %1

	# merge in the Beacon API implementation
	load "bin/bofapi.x86.o"
		merge

	#
	# attach our merged in API to any Beacon API imports
	#
	attach "$BeaconDataExtract"    "_BeaconDataExtract"
	attach "$BeaconDataLength"     "_BeaconDataLength"
	attach "$BeaconDataParse"      "_BeaconDataParse"
	attach "$BeaconDataPtr"        "_BeaconDataPtr"
	attach "$BeaconDataInt"        "_BeaconDataInt"
	attach "$BeaconDataShort"      "_BeaconDataShort"

	attach "$BeaconFormatAlloc"    "_BeaconFormatAlloc"
	attach "$BeaconFormatReset"    "_BeaconFormatReset"
	attach "$BeaconFormatAppend"   "_BeaconFormatAppend"
	attach "$BeaconFormatPrintf"   "_BeaconFormatPrintf"
	attach "$BeaconFormatToString" "_BeaconFormatToString"
	attach "$BeaconFormatFree"     "_BeaconFormatFree"
	attach "$BeaconFormatInt"      "_BeaconFormatInt"
	attach "$BeaconPrintf"         "_BeaconPrintf"

x64:
	entry %1

	load "bin/bofapi.x64.o"
		merge

	attach "$BeaconDataExtract"    "BeaconDataExtract"
	attach "$BeaconDataLength"     "BeaconDataLength"
	attach "$BeaconDataParse"      "BeaconDataParse"
	attach "$BeaconDataPtr"        "BeaconDataPtr"
	attach "$BeaconDataInt"        "BeaconDataInt"
	attach "$BeaconDataShort"      "BeaconDataShort"

	attach "$BeaconFormatAlloc"    "BeaconFormatAlloc"
	attach "$BeaconFormatReset"    "BeaconFormatReset"
	attach "$BeaconFormatAppend"   "BeaconFormatAppend"
	attach "$BeaconFormatPrintf"   "BeaconFormatPrintf"
	attach "$BeaconFormatToString" "BeaconFormatToString"
	attach "$BeaconFormatFree"     "BeaconFormatFree"
	attach "$BeaconFormatInt"      "BeaconFormatInt"
	attach "$BeaconPrintf"         "BeaconPrintf"
