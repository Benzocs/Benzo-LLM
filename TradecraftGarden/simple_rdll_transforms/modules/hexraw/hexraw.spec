#
# base64 data encoding module
#

# 'init' is called by loader.spec and is our opportunity to merge in code
# and set any global values we need to set.
init.x86:
	# merge in code for XOR recovery
	load "bin/recover.x86.o"
		merge

	# layer our xor recovery function over recover
	redirect "_recover" "_hexraw_recover"

init.x64:
	load "bin/recover.x64.o"
		merge

	redirect "recover" "hexraw_recover"

# 'apply' is called by loader.spec and is our opportunity to encode the data
apply.x86:
	encode "hexraw"

apply.x64:
	encode "hexraw"
