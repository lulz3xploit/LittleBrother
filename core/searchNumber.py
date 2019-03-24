import requests

from core.searchPJ import searchPJ
from core.searchInfoNumero import searchInfoNumero
from core.searchLocalCH import searchLocalCH
from core.searchYellowLU import searchYellowLU
from terminaltables import SingleTable

def searchNumber(codemonpays):
	num = input(" Téléphone: ")

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }

	if codemonpays == "FR":
		url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui="
		requete = requests.get(url+num, headers=headers)
		searchPJ(requete=requete, num=num)
		phone = searchInfoNumero()
		phone.search(num)

		TABLE_DATA = []

		city = phone.city
		operator = phone.operator
		location = phone.location
		_type = phone.phone_type

		infos = ("Numero", num)
		TABLE_DATA.append(infos)
		infos = ("Type", _type)
		TABLE_DATA.append(infos)
		infos = ("Operateur", operator)
		TABLE_DATA.append(infos)
		infos = ("City", city)
		TABLE_DATA.append(infos)
		infos = ("Localisation", location)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA)
		print("\n"+table.table)

	elif codemonpays == "CH":
		# search CH
		url = "https://tel.local.ch/fr/q?ext=1&rid=NV3M&name=&company=&street=&city=&area=&phone="
		searchLocalCH(url+num)

	elif codemonpays == "LU":
		url = "https://www.yellow.lu/fr/annuaire-inverse/recherche?query="
		searchYellowLU(url+num)

	else:
		# !!!! c'est deguelasse je sais... mais je n'avais pas le choix.. sa sera propre dans une prochaine MAJ... encore desole..
		url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui="
		requete = requests.get(url+num, headers=headers)
		searchPJ(requete=requete, num=num)
		phone = searchInfoNumero()
		phone.search(num)

		TABLE_DATA = []

		city = phone.city
		operator = phone.operator
		location = phone.location
		_type = phone.phone_type

		infos = ("Numero", num)
		TABLE_DATA.append(infos)
		infos = ("Type", _type)
		TABLE_DATA.append(infos)
		infos = ("Operateur", operator)
		TABLE_DATA.append(infos)
		infos = ("City", city)
		TABLE_DATA.append(infos)
		infos = ("Localisation", location)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA)
		print("\n"+table.table)

		url = "https://tel.local.ch/fr/q?ext=1&rid=NV3M&name=&company=&street=&city=&area=&phone="
		searchLocalCH(url+num)

		url = "https://www.yellow.lu/fr/annuaire-inverse/recherche?query="
		searchYellowLU(url+num)