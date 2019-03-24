import requests
from core.searchGoogle import searchGoogle
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def google():
	print("\n"+information+" Renseignez Prénom, Nom, Ville, Département, Sport, Etablissement scolaire ...\n")
	nom = input(" Recherche: ")
	print("\n"+wait+" Recherche en cours...")
	url = "https://www.google.com/search?num=20&q=\\%s\\"
	try:
		nom2 = nom.split(" ")
		nom = nom2[0]+'+'+nom2[1]
	except:
		pass
	requete = requests.get(url % (nom))
	searchGoogle(requete=requete)
