import requests
from core.searchLocalCH import searchLocalCH
from core.searchYellowLU import searchYellowLU
from core.searchPJ import searchPJ
from colorama import init, Fore,  Back,  Style

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def searchAdresse(codemonpays):
	adresse = input(" Adresse: ")
	# clear()
	print("\n"+wait+" Recherche '%s'..." % (adresse))

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }

	if codemonpays == "FR":
		# search PageBlanche
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
		requete = requests.get(url+adresse, headers=headers)
		searchPJ(requete)

	elif codemonpays == "CH":
		# search tel.local.hc
		url = "https://tel.local.ch/fr/q?ext=1&name=&company=&street={}&city=&area="
		searchLocalCH(url.format(adresse))

	else:
		# Recherche FR
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
		requete = requests.get(url+adresse, headers=headers)
		searchPJ(requete)

		# Recherche CH
		url = "https://tel.local.ch/fr/q?ext=1&name=&company=&street={}&city=&area="
		searchLocalCH(url.format(adresse))