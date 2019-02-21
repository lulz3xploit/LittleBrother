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
		profile = linkedin.profiles

		regroup = zip(employee, profile)

		TABLE_DATA = [
			("Name", "Url"),
		] 

		for r in regroup:
			TABLE_DATA.append(r)

		table = SingleTable(TABLE_DATA, title=" LinkedIn ")
		print(table.table)