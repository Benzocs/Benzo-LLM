#
# AES-CTR data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for AES recovery
	load "bin/recover.x86.o"
		merge

	# bring in our AES code too
	load "bin/aes.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_aes_recover"

	# patch in the AES key for our module too
	generate $AES_KEY 16
	patch "_aeskey" $AES_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	load "bin/aes.x64.o"
		merge

	redirect "recover" "aes_recover"

	generate $AES_KEY 16
	patch "aeskey" $AES_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "aes-ctr" $AES_KEY

apply.x64:
	mask "aes-ctr" $AES_KEY
