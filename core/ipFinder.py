import requests, re, json
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"


def ipFinder():
	ip = input(" Adresse IP: ")
	print("\n"+wait+" Locating '%s'..." % (ip))

	TABLE_DATA = []

	url = "http://ip-api.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print(warning+" Adresse IP invalide.")

	else:
		infos = ("IP", ip)
		TABLE_DATA.append(infos)
		infos = ("ISP", values['isp'])
		TABLE_DATA.append(infos)
		infos = ("Organisation", values['org'])
		TABLE_DATA.append(infos)
		infos = ("Pays", values['country'])
		TABLE_DATA.append(infos)
		infos = ("Region", values['regionName'])
		TABLE_DATA.append(infos)
		infos = ("Ville", values['city'])
		TABLE_DATA.append(infos)
		infos = ("Code Postal", values['zip'])
		TABLE_DATA.append(infos)
		localisation = str(values['lat'])+', '+str(values['lon'])
		infos = ("Localisation", localisation)
		TABLE_DATA.append(infos)
		infos = ("Maps", "https://www.google.fr/maps?q="+localisation)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA, ip)
		print("\n"+table.table)
		# print("[ %s ]" % (ip))
		# print("\n IP: " + ip)
		# print(" Hostname: " + values['ipName'])
		# print(" ISP: " + values['isp'])
		# print(" Organisation: "+values['org'])
		# print(" Pays: " + values['country'])
		# print(" Region: " + values['region'])
		# print(" Ville: " + values['city'])
		# localisation = str(values['lat']) + ','+str(values['lon'])
		# print(" Localisation: "+localisation)
		# print(" + Maps: https://www.google.fr/maps?q=%s" % (localisation))