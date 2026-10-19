#
# Bring alternate API hashing into LibTCG's findModuleByHash and findFunctionByHash resolvers
#

djb2.x86:
	# load our implementation of our hash algo implementations onto the stack
	load "bin/apihash.x86.o"
		merge

	# opt into Dynamic Function resolution and pass DJB2 hashes to our _resolve function
	dfr "_resolve" "djb2"

	# redirect the ror13 local functions (in LibTCG) to our DJB2 implementations
	redirect "_hash_function" "_djb2_function"
	redirect "_hash_module"   "_djb2_module"

fnv1a.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "fnv1a"

	redirect "_hash_function" "_fnv1a_function"
	redirect "_hash_module"   "_fnv1a_module"

joaat.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "joaat"

	redirect "_hash_function" "_joaat_function"
	redirect "_hash_module"   "_joaat_module"

ror13.x86:
	dfr "_resolve" "ror13"

sdbm.x86:
	load "bin/apihash.x86.o"
		merge

	dfr "_resolve" "sdbm"

	redirect "_hash_function" "_sdbm_function"
	redirect "_hash_module"   "_sdbm_module"

#### x64 ####

djb2.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "djb2"

	redirect "hash_function" "djb2_function"
	redirect "hash_module"   "djb2_module"

fnv1a.x64:
	load "bin/apihash.x64.o"
		merge
	
	dfr "resolve" "fnv1a"

	redirect "hash_function" "fnv1a_function"
	redirect "hash_module"   "fnv1a_module"

joaat.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "joaat"

	redirect "hash_function" "joaat_function"
	redirect "hash_module"   "joaat_module"

ror13.x64:
	dfr "resolve" "ror13"

sdbm.x64:
	load "bin/apihash.x64.o"
		merge

	dfr "resolve" "sdbm"

	redirect "hash_function" "sdbm_function"
	redirect "hash_module"   "sdbm_module"

