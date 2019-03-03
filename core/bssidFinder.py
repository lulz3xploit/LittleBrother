import requests, re, json
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

def bssidFinder():
	bssid = input(" MAC/Bssid:  ")
	print("\n"+wait+" Locating '%s'..." % (bssid))
	url = "https://api.mylnikov.org/wifi?v=1.1&bssid=%s"
	response = requests.get(url % (bssid))
	data = response.content.decode('utf-8')
	values = json.loads(data)
	code = str(values['result'])

	if code == "404":
		print("\n[%s]\n" % (bssid))
		print(warning+" Localisation Not Found")
	else:
		pass
	
	try:
		localisation = str(values['data']['lat']) + ','+str(values['data']['lon'])
		print("\n[ %s ]" % (bssid))
		print(found+" Localisation: " + localisation)
		print(found+" Maps: https://www.google.fr/maps?q=%s" % (localisation))
	except:
		pass
