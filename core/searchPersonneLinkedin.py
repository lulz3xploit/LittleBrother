from core.LinkedIn import searchLinkedIn
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable


warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"

def searchPersonneLinkedin(nom, city):
	linkedin = searchLinkedIn()
	linkedin.search(nom, city)
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