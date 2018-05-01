# coding: utf-8

import os
import requests
from bs4 import BeautifulSoup
import re
import socket
import sys
import json
import time
from datetime import date

from PIL import Image
from PIL.ExifTags import TAGS

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return times

def testConnexion():
	try:
		req = requests.get('http://google.com')
		return("Connecte")
	except:
		return("Aucune connexion internet")

today = date.today()

def mkdir(dossier):
	if os.path.exists(dossier):
		pass
	else:
		try:
			return(os.mkdir(dossier))
		except OSError:
			print("[!] Une erreur est survenu lors du creation du dossier.")

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def pause():
	raw_input("\n Appuyez sur [ENTER] pour retourner au Menu.")
    #

def printResult(name, adresse, num):
	print("\n"+"=" * 30 +"\n\n[Nom, Prenom]\n %s" % (name))
	adresse = adresse.split(",")
	print("\n[Adresse]\n %s %s " % (adresse[0], adresse[1]))
	print(" \n[Phone]\n %s" % (num))
	if (num != ''):
		phoneNumber(num)
	else:
		pass

def bssidFinder():
	bssid = raw_input("[#][LittleBrother][Lookup][MAC/Bssid:~$ ")
	url = "https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid="
	response = requests.get(url+bssid)
	data = response.content
	values = json.loads(data)
	code = str(values['result'])

	if code == "404":
		print("[%s]\n" % (bssid))
		print("Localisation Not Found")
	else:
		pass

	localisation = str(values['data']['lat']) + ','+str(values['data']['lon'])
	print("[ %s ]" % (bssid))
	print(" + Localisation: " + localisation)
	print(" + Maps: https://www.google.fr/maps?q=%s" % (localisation))

def ipFinder():
	ip = raw_input("\n[#][LittleBrother][Lookup][AdresseIP:~$ ")
	url = "https://extreme-ip-lookup.com/json/"
	# print("[*] Recherche...")
	response = requests.get(url+ip)
	data = response.text
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print("[!] IP not valid o.o'")

	else:
		print("[ %s ]" % (ip))
		print("\n IP: " + ip)
		print(" Hostname: " + values['ipName'])
		print(" ISP: " + values['isp'])
		print(" Organisation: "+values['org'])
		print(" Pays: " + values['country'])
		print(" Region: " + values['region'])
		print(" Ville: " + values['city'])
		localisation = str(values['lat']) + ','+str(values['lon'])
		print(" Localisation: "+localisation)
		print(" + Maps: https://www.google.fr/maps?q=%s" % (localisation))

def SearchEmail3():
	email = raw_input("\n[#][LittleBrother][Lookup][Email:~$ ")
	url = "https://hacked-emails.com/api?q="
	req = requests.get(url+email)
	data = req.text
	values = json.loads(data)

	x = 0

	status = values['status']
	results = values['results']
	if status == 'found':
		print("[+] "+email+": "+status)
		print("[+] Finds "+str(results)+" resultats !\n")
		print("[*] Recherche de l'email dans les bases de donnee...\n")

		while x <= int(results):
			try:
				url = values['data'][x]['source_url']
				if url != '#':
					req = requests.get(url)
					texte = req.content
					f = open("site.txt", 'w')
					f.write(texte)
					f.close()
					f = open("site.txt",'r')
					for line in f:
						line.rstrip()
						if email in line:
							if not "<li class=" in line:
								print(" + "+line.strip()+" | "+values['data'][x]['title']+"\n")
				else:
					# pass
					print("[%s]" % (values['data'][x]['title']))
					print(" + Leaked: "+values['data'][x]['date_leaked']).replace("T00:00:00+00:00","")
					print(" + Created: "+values['data'][x]['date_created']).replace("T00:00:00+00:00","\n")
					# print("Aucun resultat | "+values['data'][x]['title'])
			except:
				pass
			x = x + 1
		try:
			f.close()
			os.remove("site.txt")
		except:
			pass
	else:
		print("[!] "+email+" Not found")

"""
def Search118218():
	url = "http://www.118218.fr/recherche?category_id=&geo_id=&distance=46&category=&who=%s&where=%s"

	name = raw_input("\n[#][LittleBrother][Lookup][Nom Prenom:~$ ")
	city = raw_input("\n[#][LittleBrother][Lookup][Ville/Departement:~$")
	print("[*] Recherche...")
	req = requests.get(url % (name, city))
	data = req.content

	soup = BeautifulSoup(data, "html.parser")

	nameList = soup("h2")

	addresseList = soup.find_all("address", {"class": "addr"})
	depList = soup.find_all("span", {"class","nowrap"})
	phoneList = soup.find_all("p", {"class","telephone"})

	namesList2 = []
	addressesList2 = []
	depList2 = []
	phoneList2 = []

	for name in nameList:
		name = name.find("a")
		namesList2.append(name.string)
	for addr in addresseList:
		adresse = addr.find("span")
		addressesList2.append(adresse.string)
	for dep in depList:
		dep = dep.find("span")
		depList2.append(dep.string)
	for phone in phoneList:
		phoneList2.append(phone.string)

	regroup = zip(namesList2,addressesList2,depList2,phoneList2)
	for info in regroup:
		name = info[0]
		adresse = info[1]
		dep = info[2]
		phone = info[3]
		print(name)
		print(adresse+dep.replace(",",""))
		print(phone)
		print("______________")
"""

def searchPJ(requete='', num=''):
	def testResponse(requete):
		noReponse = soup.find("p", {"class": "wording-no-responses"})
		if noReponse:
			return 1
			# print("[!] Aucun resultattttt pour votre recherche... o_o' ")

	page = requete.text
	soup = BeautifulSoup(page, "html.parser")
	rep = testResponse(requete)
	if rep == 1:
		print("[!] Aucun resultat pour votre recherche... o_o'")
		if num != '':
			phoneNumber(num)
		else:
			pass
	else:
		pass

	try:
		nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
		addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
		numList = soup.find_all("strong", {"class": "num"})
	except AttributeError:
		pass

	namesList2 = []
	addressesList2 = []
	numesList2 = []

	for name in nameList:
		namesList2.append(name.string)
	for addresse in addressList:
		addressesList2.append(addresse.string)
	for num in numList:
		numesList2.append(num.string)

	regroup = zip(namesList2,addressesList2,numesList2)
	for infos in regroup:
        #print("\nNom Prenom: "+infos[0]+"\nAdresse: "+infos[1]+"\nNumero: "+infos[2])
		name = infos[0]
		adresse = infos[1]
		num = infos[2]
		try:
			printResult(name.strip(), adresse.strip(), num.strip())
		except AttributeError:
			pass

def searchGoogle(requete=''):
	content = requete.text
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
	        	# if "insta" in url or "twitter" in url or "facebook" in url:
				print("[+] Possible connection: "+url)

def Operator(num):
	url = 'https://www.infos-numero.com/numero/'
	url = url + num
	request = url
	http = requests.get(request)
	code = http.status_code
	if code != 301 and code != 404:
		if not 'Page not found' in http.content:
			Ope = http.content
			if 'Bouygues' in Ope:
				print(" + Bouygues")
			if 'Orange' in Ope:
				print(" + Orange")
			if 'Free' in Ope:
				print(" + Free")
			if 'SFR' in Ope:
				print(" + SFR")
		else:
			pass
	else:
		pass

def phoneNumber(num):
	def mob_fix(pfx):
		if pfx == '06' or pfx == '07':
			return("Portable")
		elif pfx == '08' or pfx == '09':
			return("internet")
		else:
			return("Fixe")

	def loc(num):
		location = {
    	"01": "Ile de France.",
    	"02": "Nord-Ouest de la France.",
    	"03": "Nord-Est de la France.",
    	"04": "Sud-Est de la France.",
    	"05": "Sud-Ouest de la France."
		}

		print(" + "+location.get(pfx))
		url = 'https://www.infos-numero.com/numero/'
		req = requests.get(url+num)
		page = req.content
		p = []
		soup = BeautifulSoup(page, "html.parser")
		tags = soup("p")
		for n in tags:
			line = n.string
			p.append(line)
		ville = p[2]
		print(" + "+ville.strip())

	num = num.replace(" ","")
	pfx = num[0:2]
    # mob_fix(pfx)

	if mob_fix(pfx) == 'Portable':
		print(" + Portable")
	elif mob_fix(pfx) == 'internet':
		print(" + VOIP")
	else:
		print(" + Fixe")
		try:
			loc(num)
			num2 = num[2:6]
			num2 = '06'+num2+'0000'
			Operator(num2)
		except:
			pass
	Operator(num)

def searchPersonne():
	nom = raw_input("\n[#][LittleBrother][Lookup][Nom Prenom:~$ ")
	city = raw_input("\n[#][LittleBrother][Lookup][Ville/Departement:~$ ")
	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
	requete = requests.get(url.format(nom, city))
	print("[*] Recherche ...")
	searchPJ(requete)

	# url = "https://www.google.com/search?num=100&q=\%s\\"
	# try:
	# 	nom2 = nom.split(" ")
	# 	nom = nom2[0]+'.'+nom2[1]
	# except:
	# 	pass
	# requete = requests.get(url % (nom))
	# searchGoogle(requete=requete)

def searchAdresse():
	adresse = raw_input("\n[#][LittleBrother][Lookup][Adresse:~$ ")
	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
	requete = requests.get(url+adresse)
	searchPJ(requete)

def searchNumber():
	num = raw_input("\n[#][LittleBrother][Lookup][Phone:~$ ")
	#print("[*] Recherche...")
	url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui="
	requete = requests.get(url+num)
	searchPJ(requete=requete, num=num)

def searchUserName():
	username = raw_input("\n[#][LittleBrother][Lookup][Pseudo:~$ ")
	url = "https://www.google.com/search?num=100&q=\%s\\"
	requete = requests.get(url % (username))
	searchGoogle(requete=requete)

def google():
	nom = raw_input("\n[#][LittleBrother][Lookup][Nom Prenom:~$ ")
	url = "https://www.google.com/search?num=100&q=\%s\\"
	try:
		nom2 = nom.split(" ")
		nom = nom2[0]+'.'+nom2[1]
	except:
		pass
	requete = requests.get(url % (nom))
	searchGoogle(requete=requete)

def exifRead():
	photo = raw_input("\n[#][LittleBrother][Lookup][Photo:~$ ")
	try:
		metaData = {}

		imgFile = Image.open(photo)
		print("[*] Getting meta data...")
		info = imgFile._getexif()
		if info:
			print("[+] Found meta data!")
			for (tag, value) in info.items():
				tagname = TAGS.get(tag, tag)
				metaData[tagname] = value
				print(tagname, value)
	except:
		print("[!] Failed.")

def mailToIP():
	def isp_host(ip):
		url = "http://ip-api.com/json/" + ip
		response = requests.get(url)
		data = response.text
		values = json.loads(data)
		return values['isp']

	def ip_loc(ip):
		url = "https://extreme-ip-lookup.com/json/" + ip
		response = requests.get(url)
		data = response.text
		values = json.loads(data)

		return(values['country']+', '+values['region']+', '+ values['city'])

	def get_domain(ip):
		s = socket.gethostbyaddr(ip)
		return(s[0])

	files = raw_input("\n[#][LittleBrother][Lookup][Entete:~$ ")
	if not os.path.exists(files):
		print("\n Fichier introuvable.")
	else:
		pass	    
	print("[*] Recherche en cours ...")
	f = open(files, 'r')

	for line in f:
		line.strip()
		if "From: " in line:
			print("[I] Message envoye par: "+line.replace("From: ",""))
		if 'Received: from' in line:
			ip_find = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
			for ip in ip_find:
				try:
					isp = isp_host(ip)
					loc = ip_loc(ip)
					domain = get_domain(ip)
				except:
					isp = 'Not found'
					loc = 'Not found'
					domain = 'Not found'

				print("""
[ %s ]
 + %s
 + %s
 + %s
  	            """ % (ip, domain, isp, loc))
	f.close()

def doxMaker():
	prenom = raw_input("Prénom : ")
	nom = raw_input("Nom : ")
	naissance = raw_input("Date de naissance : ")
	tel = raw_input("Numéro de téléphone : ")
	email = raw_input("Email : ")
	fax = raw_input("Fax : ")
	ville = raw_input("Ville : ")
	adresse = raw_input("Adresse : ")
	cp = raw_input("Code postal : ")
	ip = raw_input("adresse IP : ")
	nameFichier = prenom.capitalize()+'_'+nom.capitalize()+'.txt'
	if os.path.exists("Watched"):
		pass
	else:
		mkdir("Watched")

	f = open("Watched/"+nameFichier,'a')
	f.write("Prénom: "+prenom.capitalize())
	f.write("\nNom: "+nom.capitalize())
	f.write("\nDate de naissance: "+naissance)
	f.write("\nTéléphone: "+tel)
	f.write("\nEmail: "+email)
	f.write("\nFax: "+fax)
	f.write("\nVille: "+ville.title())
	f.write("\nAdresse: "+adresse.title())
	f.write("\nCode postal: "+cp)
	f.write("\nAdresse IP: "+ip)
	s = raw_input(" Voulez vous ajoutez des resaux sociaux a la liste ? [y/N]: ").upper()
	if s == 'Y':
		while True:
			reseaux = raw_input(" Réseaux sociaux (ex: Facebook...): ")
			name = raw_input("Nom, pseudo, lien : ")
			f.write("\n"+reseaux.capitalize()+': '+name)
			c = raw_input(" Rajouter un compte ? : [y/N]: ").upper()
			if c == 'Y':
				pass
			else:
				break
	else:
		pass
	s = raw_input("Ajouter d'autre information ? [y/N]: ").upper()
	if s == 'Y':
		print(" ATTENTION! appuyez sur ENTRER une fois fini !\n")
		print(" Utilser des ';' pour espacer les infos")
		print("ex: couleur: bleu; bssid: FF:FF:FF:FF:FF; chat: miaou")
		infos = raw_input("> ").replace("; ","\n")
		f.write('\n'+infos)
	else:
		pass
	print("\n[+] Fichier enregistre dans : 'Watched/"+nameFichier+"'")

def showDataBase():
	fichiers = {}
	x = 0
	if os.path.exists("Watched"):
		pass
	else:
		mkdir("Watched")
	datas = os.listdir("Watched")
	for c in datas:
		x = x+1
	if str(x) == '0':
		print("[!] Aucun fichier dans la base de donnee.")
	else:
		print("[*] %s Fichiers dans la base de donnee.\n" % (str(x)))
	x = 1
	for data in datas:
		print("%s) %s" % (str(x), data))
		fichiers[str(x)] = data
		x = x + 1
	
	print("\n[I] Entrez le numero d'un fichier pour lire le contenu.")
	print(" ou entrez 'back' pour revenir au menu principal.")
	
	while True:
		action = raw_input("\n[#][LittleBrother][Database:~$ ")
		try:
			action = int(action)
			if action <= x:
				fichier = fichiers.get(str(action))
				clear()
				f = open('Watched/'+fichier, 'r')
				print("[ %s ]\n" % (fichier))
				for l in f:
					l = l.strip()
					print("---- %s" % (l))
				break
		except ValueError:
			if action.lower() == "back":
				clear()
				print(menu)
				break

helpDataBase = """
		showdb : Affiche les elements dans la base de donnee.
		show <name> : Affiche le contenu du fichier.
		
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

helpMsg = """
		lookup : Faire des recherches sur une personne.  
		make : Creer un fichier '.txt' avec toute les infos obtenu.
		db : Accedez a la base de donnee.

		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

helpLookup = """
		personne : Faire des recherches avec un nom, prenom et (ville).
		pseudo : Faire des recherches avec un pseudonyme.  
		adresse : Faire des recherches avec une adresse.
		phone : Faire des recherches avec un numero de telephone.
		ip : Faire des recherches avec une adresse IP.
		bssid : Faire des recherches avec une adresse MAC/BSSID
		email : Faire des recherches avec une adresse email.
		mail : Faire des recherches avec l'entete d'un mail.
		photo : Faire des recherches grace au MetaData d'une photo
		google : Faire des recherches sur google

		back : Revenir au menu principal.
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

menu = """
                         __..--.._   
  .....              .--~  .....  `.    
.":    "`-..  .    .' ..-'"    :". `     -------=+[  _LittleBrother_  ]__
` `._ ` _.'`"(     `-"'`._ ' _.' '       ......................................
     ~~~      `.          ~~~            ------------=+[ Author: Lulz3xploit ]__
              .'                         ------------=+[ Version: 3.0 ]__
             /                                    
            (                                   [ %s ] [ %s ]
             ^---'                                
 _     _ _   _   _      ____            _   _           [ %s ]          
| |   (_) |_| |_| | ___| __ ) _ __ ___ | |_| |__   ___ _ __ 
| |   | | __| __| |/ _ \  _ \| '__/ _ \| __| '_ \ / _ \ '__|  
| |___| | |_| |_| |  __/ |_) | | | (_) | |_| | | |  __/ |      
|_____|_|\__|\__|_|\___|____/|_|  \___/ \__|_| |_|\___|_|      
                                                        
        Tapez 'help' pour avoir plus d'information.
""" % (today, times(),testConnexion())

clear()
print(menu)

try:
	while True:
		choix = raw_input("\n[#][LittleBrother:~$ ")
		if choix.lower() == 'help':
			print(helpMsg)
		elif choix.lower() == 'lookup':
			clear()
			print(menu)
			while True:
				lookup = raw_input("\n[#][LittleBrother][Lookup:~$ ")
				if lookup == 'help':
					print(helpLookup)
				elif lookup.lower() == 'personne':
					searchPersonne()
				elif lookup.lower() == 'ip':
					ipFinder()
				elif lookup.lower() == 'bssid':
					bssidFinder()
				elif lookup.lower() == 'phone':
					searchNumber()
				elif lookup.lower() == 'email':
					SearchEmail3()
				elif lookup.lower() == 'adresse':
					searchAdresse()
				elif lookup.lower() == 'pseudo':
					searchUserName()
				elif lookup.lower() == 'google':
					google()
				elif lookup.lower() == 'photo':
					exifRead()
				elif lookup.lower() == 'mail':
					mailToIP()
				elif lookup.lower() == "back":
					clear()
					print(menu)
					break
				elif lookup.lower() == "clear":
					clear()
					print(menu)
				elif lookup == '':
					pass
				elif lookup.lower() == "exit" or lookup.lower() == "quit":
					sys.exit("\nBye !")
				else:
					print("Commande introuvable")
		elif choix.lower() == 'db':
			clear()
			print(menu)
			showDataBase()
		elif choix.lower() == 'make':
			doxMaker()
		elif choix == '':
			pass			
		elif choix.lower() == "clear":
			clear()
			print(menu)
		elif choix.lower() == "exit" or choix.lower() == 'quit':
			sys.exit("\nBye !")
		else:
			print("Commande introuvable")
except KeyboardInterrupt:
	sys.exit("\nBye !")