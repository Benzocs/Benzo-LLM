name      "Generic_ReflectiveDLLInjection"
author    "Stephen Fewer (original), AFF-WG (TCG integration)"
describe  "Loading libraries from memory into host processes since 2008"
reference "https://github.com/stephenfewer/ReflectiveDLLInjection, https://tradecraftgarden.org/rdlli.html"
license   "BSD"

x86:
	load "bin/loader.x86.o"
		make pic

		fixptrs "_caller"

		push $DLL
			link "my_dll"

		export

x64:
	load "bin/loader.x64.o"
		make pic

		push $DLL
			link "my_dll"

		export
