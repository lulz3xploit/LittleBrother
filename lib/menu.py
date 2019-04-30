import sys, os, time, random
from colorama import Fore
from datetime import date

# settings
import settings

# /core
from core.Profiler import *

# /txt
from txt.text 	import text
from txt.header import lb_header


def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def printOption(option):
	title = """
	Name \t\t Value
	---- \t\t -----     
	"""

	print(title)
	for o in option:
		lengt = len(o)
		lengt = 12 - lengt
		name = o
		name += ' ' * lengt
		value = option.get(o)
		
		if not value:
			value = Fore.RED+"None"+Fore.RESET
		else:
			value = Fore.CYAN+value+Fore.RESET

		print("\t%s \t %s" % (name, value))

def menu():
	pr = Profiler()
	pr.loadDatabase(settings.pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
                         __..--.._
  .....              .--~  .....  `.         Time:      [ %s | %s ]
.":    "`-..  .    .' ..-'"    :". `         Author:    [ Lulz3xploit ]
` `._ ` _.'`"(     `-"'`._ ' _.' '           Version:   [ %s ]
     ~~~      `.          ~~~                Pays:      [ %s | %s ]
              .'                             Database:  [ %s | %s Ko ]
             /
            (                             %s
             ^---'
	""" % (Fore.YELLOW+str(date.today())+Fore.RESET, Fore.YELLOW+times()+Fore.RESET,
		   Fore.YELLOW+str(settings.version)+Fore.RESET,
		   Fore.CYAN+settings.monpays+Fore.RESET, settings.codemonpays,
		   Fore.GREEN+str(nbProfilesBDD)+Fore.RESET, Fore.RED+str(sizeOfDB)+Fore.RESET,
		   random.choice(text)
		  )

	print(lb_header())
	print(menu)
