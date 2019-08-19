# -*- coding: utf-8 -*-

from core.LinkedIn import searchLinkedIn
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def employee_lookup():
	entreprise = input(" Entreprise: ")
	city = input(" Ville: ")

	print("\n"+wait+" Recherche des employés de '%s'...\n" % (entreprise))

	linkedin = searchLinkedIn()
	linkedin.search(entreprise, city)
	
	found = linkedin.found

	if found:
		employee = linkedin.employees

		TABLE_DATA = [
			("Num", "Name"),
		] 

		x = 1
		for employe in employee:
			TABLE_DATA.append((x, employe))
			x += 1

		table = SingleTable(TABLE_DATA, title=" LinkedIn ")
		print(table.table)