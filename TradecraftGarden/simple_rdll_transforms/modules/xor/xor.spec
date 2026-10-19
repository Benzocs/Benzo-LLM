#
# xor data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_xor_recover"

	# patch in the XOR key for our module too
	generate $XOR_KEY 128
	patch "_xorkey" $XOR_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "xor_recover"

	generate $XOR_KEY 128
	patch "xorkey" $XOR_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "xor" $XOR_KEY

apply.x64:
	mask "xor" $XOR_KEY
