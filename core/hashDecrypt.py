from core.leaked import leaked
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def hashdecrypt():
	hash = input(" Hash: ")
	print("\n"+wait+" Bruteforce '%s'..." % (hash))
	lkd = leaked()
	password = lkd.hash(hash)
	
	if password:
		print("\n"+found+" %s : %s" % (hash, password))
	else:
		print("\n"+warning+" %s : Not match found." % (hash))
