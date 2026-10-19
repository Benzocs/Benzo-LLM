#
# rc4 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_rc4_recover"

	# patch in the XOR key for our module too
	generate $RC4_KEY 16
	patch "_rc4key" $RC4_KEY

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "rc4_recover"

	generate $RC4_KEY 16
	patch "rc4key" $RC4_KEY

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	mask "rc4" $RC4_KEY

apply.x64:
	mask "rc4" $RC4_KEY
