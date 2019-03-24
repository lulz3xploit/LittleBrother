import requests
from core.searchGoogle import searchGoogle
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def searchUserName():
	username = input(" Pseudo: ")
	print("\n"+wait+" Recherche '%s'..." % (username))

	# url = "https://www.google.com/search?num=100&q=\\\"%s\"\\"
	url = "https://www.google.com/search?num=100&q=\\%s\\"
	url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
	requete = requests.get(url % (username))
	requete2 = requests.get(url2 % (username))
	searchGoogle(requete=requete, requete2=requete2)