#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import Fore

# /lib
from lib.menu 		import checkVersion, clear, menu, printOption
from lib.loading 	import thread_loading

# /utils
from lib.printInfo import printInfo

# /core
from core.watching 	import watching

#Help & settings
from txt.help import helpMain, helpCountry, moreOption
import settings

checkVersion()
thread_loading()
clear()
menu()

information = settings.information
options 	= settings.optionPersonne
wait 		= settings.wait

try:
	while True:
		choix = input("\n LittleBrother("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

		if choix.lower() == 'h' or choix.lower() == 'help':
			print(helpMain)
		elif choix.lower() == 'clear':
			clear()
			menu()
		elif choix.lower() == "show option":
			printOption(options)
		elif choix.lower() == "show country":
			print(helpCountry)
		elif choix.lower() == 'show info':
			printInfo()
		elif choix.lower() == "more option":
			print(moreOption)
		elif choix.lower().startswith("set"):
			args = choix.lower().split(" ")
			if len(args) < 3:
				print("Un argument manquant. Veuillez précisez l'option et la valeur.")
			else:
				name = args[1].upper()
				value = ' '.join(args[2:])

				if name in options:
					if value == '':
						value = None
					options[name] = value
					print(information+" %s => %s" % (name, Fore.CYAN+value+Fore.RESET))

		elif choix.lower().startswith("country"):
			value = choix.upper().split(" ")
			value = value[1].strip()

			if value in settings.countryList:
				settings.codemonpays = value
				settings.monpays = settings.countryList.get(value)

		elif choix.lower() == 'run' or choix.lower() == 'start':
			print("\n"+wait+" Profiling...")
			watching(options)

		elif choix.lower() == 'exit' or choix.lower() == 'quit':
			sys.exit("\n"+information+" Bye ! :)")

		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")
