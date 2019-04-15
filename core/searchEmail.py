from colorama import init, Fore,  Back,  Style
from core.leaked import leaked
from terminaltables import SingleTable
import requests, re

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"

init()

def SearchEmail():
	email = input(" Email: ")
	print("\n"+wait+" Recherche d'information sur '%s'..." % (email))
	lkd = leaked()
	leak = lkd.email(email)

	if leak:
		TABLE_DATA = [
			('Title', 'Domain', 'Date'),
		]

		for lk in leak:
			name = lk['Title']
			domain = lk['Domain']
			date = lk['Date']

			tuples = (name, domain, date)
			TABLE_DATA.append(tuples)

		table = SingleTable(TABLE_DATA, " Leaked Site ")
		print(table.table)


		print("\n"+wait+" Recherche du Mot de passse...")

	table_dump = [
		('Email', 'Password'),
	]

	url = "https://www.google.fr/search?num=100&q=\\intext:\"%s\"\\"
	content = requests.get(url % (email)).text
	urls = re.findall('url\\?q=(.*?)&', content)
	cout = len(urls)
	if cout == 0:
		print(warning+" Aucun résultat.")
	else:
		print(wait+" Scan %s Link..." % (str(cout)))
		x = 1
		countPassword = 0
		for url in urls:
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "webcache.googleusercontent.com/" in url:
						if not "/policies/faq" in url:
							try:
								# print("(%s) link scanned. " % (str(x)))
								texte = requests.get(url).text
								# print("Search...")
								combo = re.search(email+r":([a-zA-Z0-9_ & * $ - ! / ; , ? + =  | \. ]+)", texte).group()
								if combo:
									passw = combo.split(":")[1]
									tuples = (email, passw)
									countPassword += 1
									table_dump.append(tuples)
									# print("[+] %s" % (combo))
							except:
								pass
								# print("[?] %s " % (url))
							# x = x + 1
		if countPassword > 0:
			table = SingleTable(table_dump, " Dump ")
			print("\n"+table.table)
		else:
			print(warning+" Aucune donnée pour '%s' " % (email))
