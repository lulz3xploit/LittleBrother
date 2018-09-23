# -*- coding: utf-8 -*-

__version__ = 5.0

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style

init()

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit("[!] Veuillez lancer la version 3 de python.")

checkVersion()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def loadlib():
	import requests
	from bs4 import BeautifulSoup
	import re
	from terminaltables import SingleTable, AsciiTable
	import smtplib
	import socket
	import webbrowser
	import json
	# import colorama
	from datetime import date
	import exifread

	global requests, BeautifulSoup, re, SingleTable, AsciiTable, smtplib, socket, webbrowser, json, date, exifread, internet # monip # , colorama
	# monip = requests.get("https://api.ipify.org/").text
	try:
		req = requests.get("https://google.com/")
		internet = Fore.GREEN+"√"+Fore.RESET
	except:
		internet = Fore.RED+"X"+Fore.RESET

def loadingHack(importlib):
	chaine = '[*] Start LittleBrother...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			# time.sleep(0.03)
			time.sleep(0.06)

def loadingUpper(importlib):

	string = "Start littlebrother"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			sys.stdout.write("\r[*] "+''.join(string) +'...')
			time.sleep(0.1)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1

def thread_loading():

	num = random.choice([1, 2])

	importlib = threading.Thread(target=loadlib)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	load.start()
	importlib.join()
	load.join()

thread_loading()

# import requests
# from bs4 import BeautifulSoup
# import re
# from terminaltables import SingleTable, AsciiTable
# import smtplib
# import random
# import socket
# import webbrowser
# import json
# import colorama
# from datetime import date
# import dns.resolver
import dns.resolver

class leaked:

	def hash(self, hash):
		try:
			text = requests.get("https://lea.kz/api/hash/"+hash).text
			data = json.loads(text)
			passw = data['password']
			return(passw)
		except:
			return(None)

	def email(self, email):
		try:
			text = requests.get("https://lea.kz/api/email/"+email).text
			data = json.loads(text)
			leaked = data['leaked']
			return(leaked)
		except:
			return(None)

class receiveSms:

	def searchServer(self):
		url = "https://www.receive-sms-online.info/"

		req = requests.get(url)
		page = req.content

		serverList = re.findall(r"<a href=\"([0-9]+)-([a-zA-Z0-9_]+)", page.decode('utf-8'))
		serverOnline = []

		n = 1

		for server in serverList:
			numero = server[0]
			country = server[1]
			tupleServer = (str(n), numero, country)
			serverOnline.append(tupleServer)
			# print("[%s] %s - +%s" % (str(n), country, numero))
			n = n + 1

		self.server_list = serverOnline
		self.url_of_site = url
	
	def sms(self, url):

		req = requests.get(url)
		page = req.content.decode('utf-8')
		fromUsersList = re.findall(r"data-label=\"From   :\">([a-zA-Z0-9_ +]+)</td>", page)
		messagesList = re.findall(r"data-label=\"Message:\">(.*)</td>", page)
		timeAgoList = re.findall(r"data-label=\"Added:\">(.*)</td>", page)

		regroup = zip(fromUsersList, messagesList, timeAgoList)

		self.contentMessages = regroup
		self.messageText = messagesList[1]
		self.fromUser = fromUsersList[1] 
		self.count = int(len(fromUsersList))

class instagramGetInfo:

	def __init__(self, username):
		if username.startswith("http"):
			url = username
		else:
			url = "https://instagram.com/"+username

		page = requests.get(url).content.decode('utf-8')

		# username = re.findall(r"\"username\":\"([a-zA-Z0-9 _ - \. ]+)\"", page)
		jsonData = re.findall(r"<script type=\"text/javascript\">(.*);</script>", page)
		jsonDataFound = jsonData[0].replace("window._sharedData = ", "")
		
		values = json.loads(jsonDataFound)

		profilId = values['entry_data']['ProfilePage'][0]['graphql']['user']['id']
		bio = values['entry_data']['ProfilePage'][0]['graphql']['user']['biography']
		user = values['entry_data']['ProfilePage'][0]['graphql']['user']['username']
		name = values['entry_data']['ProfilePage'][0]['graphql']['user']['full_name']
		private = values['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified']
		follower = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
		friend = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']
		media = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
		profilPicHd = values['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
		
		self.id = profilId
		self.profi_pic_hd = profilPicHd
		self.biography = bio
		self.username = user
		self.name = name
		self.private = private
		self.followers = follower
		self.friends = friend
		self.medias = media

class twitterSearchTool():

	def searchTwitter(self, nom):

		nom = nom.replace(" ", "%20")

		page = requests.get("https://twitter.com/search?f=users&vertical=default&q=%s" % (nom)).text #.content.decode('utf-8')
		datas = re.findall(r"data-screen-name=\"(.*) ", page)
		# data = data.replace("\"", '').replace("data-screen-name=", '').replace("data-name=", '')
		
		usernamesList = []
		namesList = []
		
		for d in datas:
			d = d.split("data-name=")
			usernamesList.append(d[0].replace("\" ", ''))
			namesList.append(d[1].replace("\"", ''))

		regroup = zip(usernamesList, namesList)

		return(regroup)

	def getInfoProfile(self, usernmae):
		if usernmae.startswith('http'):
			url = usernmae
		else:
			url = "https://twitter.com/"+usernmae

		req = requests.get(url)
		page = req.content.decode('utf-8')
		page0 = req.text

		jsonData = re.findall(r"<input type=\"hidden\" id=\"init-data\" class=\"json-data\" value=\"(.*)\">", page)
		data =  jsonData[0].replace("&quot;", "\"")

		values = json.loads(data)

		birthDate = re.findall(r"ProfileHeaderCard-birthdateText u-dir\" dir=\"ltr\"><span class=\"js-tooltip\" title=\"Publique\">(.*)", page0)
		profilId = values['profile_user']['id_str']
		name = values['profile_user']['name']
		username = values['profile_user']['screen_name']
		location = values['profile_user']['location']
		url = values['profile_user']['url']
		description = values['profile_user']['description']
		protected = values['profile_user']['protected']
		followers = values['profile_user']['followers_count']
		friends = values['profile_user']['friends_count']
		favoris = values['profile_user']['favourites_count']
		create = values['profile_user']['created_at']
		geo = values['profile_user']['geo_enabled']
		verified = values['profile_user']['verified']
		status = values['profile_user']['statuses_count']
		langue = values['profile_user']['lang']

		if not birthDate:
			self.birth = "None"
		else:
			self.birth = birthDate[0].strip()

		self.id = profilId
		self.name = name
		self.username = username
		self.location = location
		self.url = url
		self.description = description
		self.protected = protected
		self.followers = str(followers)
		self.friends = str(friends)
		self.create = create
		self.geo = geo
		self.verified = verified
		self.status = str(status)
		self.langue = langue

class searchInfoNumero:

	def search(self, num):
		def mob_fix(pfx):
			if pfx == '06' or pfx == '07':
				return("Portable")
			elif pfx == '08' or pfx == '09':
				return("internet")
			else:
				return("Fixe")

		location = {
			"01": "Ile de France.",
			"02": "Nord-Ouest de la France.",
			"03": "Nord-Est de la France.",
			"04": "Sud-Est de la France.",
			"05": "Sud-Ouest de la France."
		}

		num = num.replace(" ","").replace("+33", "0")
		pfx = num[0:2]

		url = 'https://www.infos-numero.com/numero/'
		page = requests.get(url+num).content.decode('utf-8')
		p = []
		soup = BeautifulSoup(page, "html.parser")
		tags = soup("p")

		for n in tags:
			line = n.string
			p.append(line)

		operator = p[2]
		ville = p[3]

		self.location = location.get(pfx)
		self.city = ville
		self.operator = operator

		if mob_fix(pfx) == 'Portable':
			self.phone_type = "Portable"
		elif mob_fix(pfx) == 'internet':
			self.phone_type = "Voip/FAI"
		else:
			self.phone_type = "Fixe"

class facebookSearchTool:

	def searchFacebook(self, nom):

		url = "https://www.facebook.com/public/%s"

		name = nom.replace(" ","%20")

		try:
			page = requests.get(url % (name)).content.decode('utf-8')
		except:
			print("[!] Aucun résultat.")

		data = page

		urlsAccount = re.findall('http[s]?://www.facebook.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
		nameAccount = re.findall("width=\"100\" height=\"100\" alt=\"([a-zA-Z0-9_ é , ]+)", data)
		# print(nameAccount)

		urlList = []

		for nbr in urlsAccount:
			c = urlsAccount.count(nbr)
			if c > 1:
				urlsAccount.remove(nbr)

		for x in urlsAccount:
			if x.endswith("s"):
				urlsAccount.remove(x)

		for u in urlsAccount:
			if "/public/" in u or "/login.php" in u or "/recover" in u or "/help/" in u:
				pass
			elif "directory/pages_variations/" in u:
				pass
			elif "login/" in u:
				pass
			elif "&" in u:
				pass
			elif "/pages/" in u:
				pass
			else:
				urlList.append(u)

		usersAccount = []

		accountsFound = []

		for url in urlList:
			try:
				url = url.replace("https://www.facebook.com/", '')
				c = url.count("/")
				if c == 1:
					pass  # un url avec 2 fois "/" signifie que c'est une page.
				else:
					usersAccount.append(url)

			except:
				pass

		regroup = zip(usersAccount, nameAccount)
	
		return(regroup)

	def getInfoProfile(self, profile):
		if not "http" in profile:
			url = "https://www.facebook.com/"+profile
		else:
			url = profile

		try:
			page = requests.get(url).content.decode('utf-8')
			findId = re.search(r"entity_id=([0-9]+)", page).group(0)

			if findId:
				facebookID = findId.replace("entity_id=", '')
			else:
				self.facebookId = "None"
			
			self.facebookId = facebookID

		except:
			self.facebookId = "None"

		name = re.search(r'pageTitle\">(.*)</title>', page).group(0)
			
		if name:
			name = name.replace("pageTitle\">", '').replace("| Facebook</title>", '')
			self.name = name

		else:
			self.name = "None"

		works = re.findall(r"<div class=\"_2lzr _50f5 _50f7\"><a href=\"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\">([a-zA-Z0-9_ - à é è ê ù ç ô ò û]+)", page)

		if works:
			self.work = works
		else:
			self.work = "None"

		locations = re.findall(u"<span class=\"_2iel _50f7\"><a href=\"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\">([a-zA-Z0-9_ - à é è ê ù ç ô ò û]+)", page)

		if locations:
			self.location = locations
		else:
			self.location = "None"

	def searchPageLiked(self, profile):
		if not "http" in profile:
			profile = "https://www.facebook.com/"+profile

		nom = profile.replace("https://www.facebook.com/", '')

		page = requests.get(profile).content.decode('utf-8')
		
		urlsPages = re.findall('http[s]?://www.facebook.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page)
		
		for nbr in urlsPages:
			c = urlsPages.count(nbr)
			if c > 1:
				urlsPages.remove(nbr)

		pagesLiked = []
		for url in urlsPages:
			if "/public/" in url or "/login.php" in url or "/recover" in url or "/help/" in url:
				pass
			else:
				if nom in url:
					pass
				else:
					pagesLiked.append(url)

		return(pagesLiked)

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return times

def searchTwitter():
	username = input("\n[#][LittleBrother][Lookup][Username:~$ ")
	twitool = twitterSearchTool()
	twitool.getInfoProfile(username)

	username = twitool.username
	profilId = twitool.id
	name = twitool.name
	location = twitool.location
	url = twitool.url
	description = twitool.description
	protected = twitool.protected
	followers = twitool.followers
	friend = twitool.friends
	dateCreate = twitool.create
	geo = twitool.geo
	verif = twitool.verified
	status = twitool.status
	langue = twitool.langue
	naissance = twitool.birth

	print("[@%s]" % (username))
	print("\n[+] Name: %s" % (name))
	print("[+] Langue: %s" % (langue.upper()))
	print("[+] Privee: %s" % (protected))
	print("[+] ID: %s" % (profilId))
	print("[+] Protected: %s" % (protected))
	print("[+] Abonnees: %s | Abonnements: %s" % (followers, friend))
	print("[+] Tweets: %s" % (status))
	print("[+] Ville: %s" % (location))
	print("[+] Naissance: %s"  % (naissance))
	print("[+] Url: %s" % (url))
	print("[+] Create: %s" % (dateCreate))
	print("[BIO]: %s" % (description))

def searchInstagram():
	user = input("\n[#][LittleBrother][Lookup][Username:~$ ")

	insta = instagramGetInfo(user)

	name = insta.name
	userId = insta.id
	images = insta.profi_pic_hd
	username = insta.username
	private = insta.private
	followers = insta.followers
	friend = insta.friends
	publication = insta.medias
	bio = insta.biography

	print("\n[%s]" % (username))
	print("\n[+] Name: %s" % (name))
	print("[+] Pictures: %s" % (images))
	print("[+] ID: %s" % (userId))
	print("[+] Protected: %s" % (private))
	print("[+] Abonnees: %s  |  Abonnements: %s" % (followers, friend))
	print("[+] Publication: %s" % (publication))
	print("[+] Bio: %s" % (bio))

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

def pause():
	input("\n Appuyez sur [ENTER] pour retourner au Menu.")
	#

def printResult(name, adresse, num):

	# print("\n"+"=" * 30 +"\n\n[Nom, Prenom]\n %s" % (name))
	# adresse = adresse.split(",")
	# print("\n[Adresse]\n %s %s " % (adresse[0], adresse[1]))
	# print(" \n[Phone]\n %s" % (num))
	
	print("\n[Particulier] %s" % (name))
	adresse = adresse.split(",")
	print("(+) Adresse: %s %s" % (adresse[0], adresse[1]))
	print("(+) Telephone: %s" % (num))

	if (num != ''):
		phoneNumber(num)
	else:
		pass

def emailSpam():
	try:
		email = input("[#][LittleBrother][SETool][Ton email:~$ ")
		password = input("[#][LittleBrother][SETool][Ton mot de passe:~$ ")
		print(wait+" Connexion...")

		if ('@gmail' in email):
			server = 'smtp.gmail.com'
			port = 587

		elif ('@live' in email or '@hotmail' in email or '@ootlook'):
			server = 'smtp.live.com'
			port = 465

		try:
			server = smtplib.SMTP(server, port)
			server.ehlo()
			server.starttls()
			server.login(email, password)
			print("[+] Connexion effectue avec succes !\n")
		except:
			print("[!] Mot de passe incorrect ! ")
			sys.exit()
		spoof_mail = input("[#][LittleBrother][SETool][From:~$ ")
		target_email = input("[#][LittleBrother][SETool][To:~$ ")
		nb = input("[#][LittleBrother][SETool][Nb Email a envoyer:~$ ")
		nb = int(nb)

		objet = input("[#][LittleBrother][SETool][Objet:~$ ")
		message = input("[#][Inserer votre message ici > ")
		send = 1

		try:
			while (nb >= send):
				server.sendmail(email, target_email, message)
				sys.stoud.write("\r%s -> %s (%s)" % (spoof_mail, target_email, send))
				send = send+1
		except KeyboardInterrupt:
			print(str(send)+" mail envoye")
			sys.exit()

		print("")

	except:
		print("[!] Erreur")
		
def facebookStalk():
	profile = input("\n[#][LittleBrother][Lookup][ProfileFB:~$ ")

	menuStalk = """

        TAGS              PERSONNES              LIEUX
    ------------        -------------        -------------
    [1] Photos          [4] Famille          [10] Tout
    [2] Videos          [5] Amis             [11] Bars
    [3] Publication     [6] Amis en commun   [12] Restaurants
                        [7] Travaille        [13] Magasin
        LIKE            [8] Etude            [14] Exterieur
    ------------        [9] Locaux           [15] Hotels
    [17] Photos                              [16] Theatre
    [18] Videos          COMMENTAIRE
    [19] Publications   -------------          INTERETS     
                        [20] Photos          -------------
        PROFIL                               [29] Pages
    -------------                            [30] Politiques
    [21] Photos                              [31] Religion
    [22] Videos                              [32] Musiques
    [23] Publications                        [33] Films
    [24] Groupes                             [34] Livres
    [25] Futur evenements                    [35] Lieux
    [26] Evenements passes
    [27] Jeux
    [28] Apps

        [b] Back    [c] Clear screen    [e] Exit script
	"""

	dicFbStalk = {
	# TAGS
	"1": "https://www.facebook.com/search/%s/photos-of/intersect",
	"2": "https://www.facebook.com/search/%s/videos-of/intersect",
	"3": "https://www.facebook.com/search/%s/stories-tagged/intersect",
	# PERSONNE
	"4": "https://www.facebook.com/search/%s/relatives/intersect",
	"5": "https://www.facebook.com/search/%s/friends/intersect",
	"6": "https://www.facebook.com/search/%s/friends/friends/intersect",
	"7": "https://www.facebook.com/search/%s/employees/intersect/",
	"8": "https://www.facebook.com/search/%s/schools-attended/ever-past/intersect/students/intersect/",
	"9": "https://www.facebook.com/search/%s/current-cities/residents-near/present/intersect",
	# LEUX
	"10": "https://www.facebook.com/search/%s/places-visited/",
	"11": "https://www.facebook.com/search/%s/places-visited/110290705711626/places/intersect/",
	"12": "https://www.facebook.com/search/%s/places-visited/273819889375819/places/intersect/",
	"13": "https://www.facebook.com/search/%s/places-visited/200600219953504/places/intersect/",
	"14": "https://www.facebook.com/search/%s/places-visited/935165616516865/places/intersect/",
	"15": "https://www.facebook.com/search/%s/places-visited/164243073639257/places/intersect/",
	"16": "https://www.facebook.com/search/%s/places-visited/192511100766680/places/intersect/",
	# LIKE
	"17": "https://www.facebook.com/search/%s/photos-liked/intersect",
	"18": "https://www.facebook.com/search/%s/videos-liked/intersect",
	"19": "https://www.facebook.com/search/%s/stories-liked/intersect",
	# COMMENTAIRE
	"20": "https://www.facebook.com/search/%s/photos-commented/intersect",
	# PROFIL
	"21": "https://www.facebook.com/search/%s/photos-by/",
	"22": "https://www.facebook.com/search/%s/videos-by/",
	"23": "https://www.facebook.com/search/%s/stories-by/",
	"24": "https://www.facebook.com/search/%s/groups",
	"25": "https://www.facebook.com/search/%s/events-joined/",
	"26": "https://www.facebook.com/search/%s/events-joined/in-past/date/events/intersect/",
	"27": "https://www.facebook.com/search/%s/apps-used/game/apps/intersect",
	"28": "https://www.facebook.com/search/%s/apps-used/",
	# INTERETS
	"29": "https://www.facebook.com/search/%s/pages-liked/intersect",
	"30": "https://www.facebook.com/search/%s/pages-liked/161431733929266/pages/intersect/",
	"31": "https://www.facebook.com/search/%s/pages-liked/religion/pages/intersect/",
	"32": "https://www.facebook.com/search/%s/pages-liked/musician/pages/intersect/",
	"33": "https://www.facebook.com/search/%s/pages-liked/movie/pages/intersect/",
	"34": "https://www.facebook.com/search/%s/pages-liked/book/pages/intersect/",
	"35": "https://www.facebook.com/search/%s/places-liked/"
	}

	helpMsgFbStalk = """
		back : Revenir au menu principal.
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

	resultProfile = """
    [Name] %s
    [work] %s
    [Loc] %s
    [ID] %s"""

	fbtool = facebookSearchTool()

	try:
		fbtool.getInfoProfile(profile)
		
		loc = fbtool.location
		work = fbtool.work
		name = fbtool.name
		ID = fbtool.facebookId
		
		facebookID = ID

	except:
		pass

	while True:

		if facebookID == "None":
			print("[!] Impossible de recuperer l'ID.")
			_id_  = input("\n[?] Connaissez-vous l'ID ? [O/N]: ")
			if _id_.upper() == "O" or _id_.upper() == "Y":
				facebookID = input("\n[#][LittleBrother][Lookup][ID:~$ ")
				input(facebookID)
			else:
				break

		print(resultProfile % (name, work, loc, ID))
		print(menuStalk)
		
		while True:
			s = input("\n[#][LittleBrother][Lookup][StalkFB:~$ ")
			if s == "help":
				print(helpMsgFbStalk)
			elif s.lower() == "c":
				clear()
				print(menuStalk)
			elif s.lower() == "b":
				break
			elif s.lower() == "e":
				quit()
			else:
				if str(s) == '29':
					# searchPageLiked(profile)
					pages = fbtool.searchPageLiked(profile)
					for p in pages:
						print("[Liked] %s" % (p))
				try:
					int(s)
					facebookUrl = dicFbStalk.get(str(s))
					webbrowser.open(facebookUrl % (facebookID))
				except ValueError:
					pass
		break

def bssidFinder():
	bssid = input("[#][LittleBrother][Lookup][MAC/Bssid:~$ ")
	# clear()
	url = "https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid="
	response = requests.get(url+bssid).content.decode('utf-8')
	data = response.content
	values = json.loads(data)
	code = str(values['result'])

	if code == "404":
		print("\n[%s]\n" % (bssid))
		print("[!] Localisation Not Found")
	else:
		pass
	
	try:
		localisation = str(values['data']['lat']) + ','+str(values['data']['lon'])
		print("\n[ %s ]" % (bssid))
		print(" + Localisation: " + localisation)
		print(" + Maps: https://www.google.fr/maps?q=%s" % (localisation))
	except:
		pass

def ipFinder():
	ip = input("\n[#][LittleBrother][Lookup][AdresseIP:~$ ")
	# clear()

	TABLE_DATA = []

	url = "https://extreme-ip-lookup.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print("[!] IP not valid o.o'")

	else:
		infos = ("IP", ip)
		TABLE_DATA.append(infos)
		infos = ("Hostname", values['ipName'])
		TABLE_DATA.append(infos)
		infos = ("ISP", values['isp'])
		TABLE_DATA.append(infos)
		infos = ("Organisation", values['org'])
		TABLE_DATA.append(infos)
		infos = ("Pays", values['country'])
		TABLE_DATA.append(infos)
		infos = ("Region", values['region'])
		TABLE_DATA.append(infos)
		infos = ("Ville", values['city'])
		TABLE_DATA.append(infos)
		localisation = values['lat']+', '+values['lon']
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

def SearchEmail4():
	email = input("\n[#][LittleBrother][Lookup][Email:~$ ")
	print(wait+" Recherche d'information sur '%s'" % (email))
	lkd = leaked()
	leak = lkd.email(email)

	if leak:
		print(found+" Site leak : "+leak)
		print(wait+" Recherche du Mot de passse...")
		# email = email.replace("@", "%40")
		# clear()
		# url = "https://www.google.com/search?num=100&q=\%s\\"

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
									print("[?] %s " % (url))
								# x = x + 1
			if countPassword > 0:
				table = SingleTable(table_dump, " Dump ")
				print("\n"+table.table)
			else:
				pass
	else:
		print(warning+" Aucune donnée pour '%s' " % (email))

def Search118218():
	url = "http://www.118218.fr/recherche?category_id=&geo_id=&distance=46&category=&who=%s&where=%s"

	name = input("\n[#][LittleBrother][Lookup][Nom Prenom:~$ ")
	city = input("\n[#][LittleBrother][Lookup][Ville/Departement:~$")

	data = requests.get(url % (name, city)).content.decode('utf-8')

	soup = BeautifulSoup(data, "html.parser")

	nameList = soup("h2")

	addresseList = soup.find_all("address", {"class": "addr"})
	depList = soup.find_all("span", {"class","nowrap"})
	phoneList = soup.find_all("p", {"class","telephone"})

	namesList2 = []
	addressesList2 = []
	depList2 = []
	phoneList2 = []
	# try:
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

def check_email_exist():
	email_address = input("[LittleBrother][#][Email:~$ ")
	print(wait+" Verification...")
	addressToVerify = email_address

	domain_name = addressToVerify.split('@')[1]

	#get the MX record for the domain
	records = dns.resolver.query(domain_name, 'MX')
	mxRecord = records[0].exchange
	mxRecord = str(mxRecord)

	host = socket.gethostname()

	server = smtplib.SMTP()
	server.set_debuglevel(0)
	# SMTP Conversation
	server.connect(mxRecord)
	server.helo(host)
	server.mail('me@domain.com')
	code, message = server.rcpt(str(addressToVerify))
	server.quit()

	if code == 250:
		print(found+" %s existe." % (email_address))
	else:
		print(warning+" %s n'existe pas." % (email_address))

def searchCopainsdavant(nom, city):
	url = "http://copainsdavant.linternaute.com/s/?ty=1&prenom=%s&nom=%s&nomjf=&annee=&anneeDelta=&ville=%s"
	name = nom
	if " " in name:
		nom = name.split(" ")[1]
		prenom = name.split(" ")[0]
	else:
		prenom = ""
		nom = name

	data = requests.get(url % (prenom, nom, city)).content.decode('utf-8')

	soup = BeautifulSoup(data, "html.parser")

	nameList = soup.find_all("div", {"class": "grid_last"})
	addresseList = soup.find_all("span", {"class": "app_list--result__search__place"})
	urlList = soup.find_all("h3")
	birthdayList = []
	travailList = []

	urlList2 = []

	for url in urlList:
		url = url.find("a")
		urls = str(url)
		href = re.search(r"/p/([a-zA-Z0-9_-]+)", urls).group()
		urlList2.append(href)

	for url in urlList2:
		data = requests.get("http://copainsdavant.linternaute.com/%s" % (url)).content.decode('utf-8')
		soup = BeautifulSoup(data, "html.parser")
		birthdayList0 = soup.find_all("abbr", {"class": "bday"})
		item = len(birthdayList0)
		if item == 0:
		 	birthdayList0.append("None")
	
		for b in birthdayList0:
			birthdayList.append(str(b))

		travailList0 = soup.find_all("p", {"class": "title"})
		item = len(travailList0)
		if item == 0:
		 	travailList0.append("None")
	
		for t in travailList0:
			travailList.append(str(t))

	namesList2 = []
	addressesList2 = []
	birthdayList2 = []
	travailList2 = []

	for name in nameList:
		name = name.find("a")
		namesList2.append(name.string)
	for addr in addresseList:
		addressesList2.append(addr.string.strip())
	for date in birthdayList:
		date = date.replace("<abbr class=\"bday\" title=\"", "").replace("00:00:00\">", "- ").replace("</abbr>", "").replace("\">", "")
		birthdayList2.append(date)
	for travail in travailList:
		travail = travail.replace("<p class=\"title\">", "").replace("</p>", "")
		travailList2.append(travail)

	regroup = zip(namesList2, addressesList2, birthdayList2, travailList2, urlList2)

	title = " Copain D'avant "

	TABLE_DATA = [
		('Name', 'Adresse', 'Date', 'Work', 'url'),
	]


	count = 0

	for info in regroup:
		count += 1
		name = info[0]
		adresse = info[1]
		adresse = adresse.split(" - ")[0]
		dateBirthday = info[2]
		try:
			dateBirthday = dateBirthday.split(" - ")[1]
		except:
			pass
		travail = info[3]
		url = info[4]

		infos = (name, adresse, dateBirthday, travail, url)

		TABLE_DATA.append(infos)

	if count > 0:
		table_instance = SingleTable(TABLE_DATA, title)
		print(table_instance.table)

def searchPJ(requete='', num=''):
	def testResponse(requete):
		noReponse = soup.find("p", {"class": "wording-no-responses"})
		if noReponse:
			return 1
			# print("[!] Aucun resultattttt pour votre recherche... o_o' ")

	page = requete.text #content.decode('utf-8')
	soup = BeautifulSoup(page, "html.parser")
	rep = testResponse(requete)
	if rep == 1:
		print(warning+" Aucun résultat pour votre recherche... o_o'")
		if num != '':
			# phoneNumber(num)
			pass
		else:
			pass
	else:
		pass

	try:
		nameList = soup.find_all("a", {"class": "denomination-links pj-lb pj-link"})
		addressList = soup.find_all("a", {"class": "adresse pj-lb pj-link"})
		numList = soup.find_all("strong", {"class": "num"})
		# name = name.string.strip()
		# adresse = adresse.string.strip()
		# num = num.string.strip()
		# printResult(name, adresse, num)
	except AttributeError:
		pass

	namesList2 = []
	addressesList2 = []
	numesList2 = []
	operatorList = []

	# try:
	for name in nameList:
		namesList2.append(name.text.strip())
	for addresse in addressList:
		addressesList2.append(addresse.text.strip())
	for num in numList:
		phone = searchInfoNumero()
		phone.search(num.text.strip())
		operator = phone.operator
		operatorList.append(operator) 
		numesList2.append(num.text.strip())
	# except:
	# 	pass
	# 	print("[!] Aucun resultat pour votre recherche... o_o'")

	regroup = zip(namesList2,addressesList2,numesList2, operatorList)
	
	title = " Particulier "

	TABLE_DATA = [
		('Name', 'Adresse', 'Phone', 'Operateur'),
	]

	listeInfos = []

	for infos in regroup:
		
		try:

			TABLE_DATA.append(infos)

		except AttributeError:
			pass

	if rep != 1:
		table_instance = SingleTable(TABLE_DATA, title)
		print("\n"+table_instance.table)

def searchGoogle(requete='', requete2=''):

	encodeList = [
		"%21","%23","%24","%26","%27","%28","%29","%2A","%2B","%2C","%2F","%3A","%3B","%3D","%3F","%40","%5B","%5D",
		"%20","%22","%25","%2D","%2E","%3C","%3E","%5C","%5E","%5F","%60","%7B","%7C","%7D","%7E"
	]

	encodeDic = {
		"%21": "!",
		"%23": "#",
		"%24": "$",
		"%26": "&",
		"%27": "'",
		"%28": "(",
		"%29": ")",
		"%2A": "*",
		"%2B": "+",
		"%2C": ",",
		"%2F": "/",
		"%3A": ":",
		"%3B": ";",
		"%3D": "=",
		"%3F": "?",
		"%40": "@",
		"%5B": "[",
		"%5D": "]", 
		"%20": " ",
		"%22": "\"",
		"%25": "%",
		"%2D": "-",
		"%2E": ".",
		"%3C": "<",
		"%3E": ">",
		"%5C": "\\",
		"%5E": "^",
		"%5F": "_",
		"%60": "`",
		"%7B": "{",
		"%7C": "|",
		"%7D": "}",
		"%7E": "~",
	}

	if requete2 != '':
		content = requete2.text #.content.decode('utf-8')
		urls = re.findall('url\\?q=(.*?)&', content)
		for url in urls:
			for char in encodeList:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "/policies/faq" in url:
					# if "insta" in url or "twitter" in url or "facebook" in url:
						print("[++] Possible connection: "+url)
	else:
		pass

	content = requete.text
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		for char in encodeList:
			find = re.search(char, url)
			if find:
				charDecode = encodeDic.get(char)
				url = url.replace(char, charDecode)
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				if not "/policies/faq" in url:
				# if "insta" in url or "twitter" in url or "facebook" in url:
					print("[+] Possible connection: "+url)

def searchPersonne():
	nom = input("\n[#][LittleBrother][Lookup][Prenom Nom:~$ ")
	city = input("\n[#][LittleBrother][Lookup][Ville/Departement:~$ ")
	print(wait+" Recherche...")

	try:
# Page Jaune search
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
		headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    	    'referrer': 'https://google.com',
        	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        	'Accept-Encoding': 'gzip, deflate, br',
        	'Accept-Language': 'en-US,en;q=0.9',
        	'Pragma': 'no-cache'
        }
        
		requete = requests.get(url.format(nom, city), headers=headers)
		searchPJ(requete)

# Copain d'avant search
		searchCopainsdavant(nom, city)

# Facebook search		
		fbtool = facebookSearchTool()
		accountsFb = fbtool.searchFacebook(nom)

		title = " Facebook "

		TABLE_DATA = [
			('Name', 'User', 'Location'),
		]

		count = 0

		for a in accountsFb:
			count += 1
			name = a[1]
			username = a[0]
			fbtool.getInfoProfile(username)
			loc = fbtool.location
			if loc == "None":
				loc = ""
			else:
				loc = ", ".join(loc)
			tuples = (name, username, loc)
			# listeInfos.append(tuples)
			TABLE_DATA.append(tuples)
		
		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			print(table_instance.table)
		
# Twitter Search		
		title = " Twitter "

		TABLE_DATA = [
			('Name', 'User', 'Date', 'Location'),
		]

		twitool = twitterSearchTool()
		accountTwitter = twitool.searchTwitter(nom)

		count = 0

		for a in accountTwitter:
			count += 1
			name = a[1]
			username = "@"+a[0]
			twitool.getInfoProfile(a[0])
			
			location = twitool.location
			date = twitool.birth
			bio = twitool.description
			url = twitool.url

			tuples = (name, username, date, location)
			TABLE_DATA.append(tuples)

		if count > 0:
			table_instance = SingleTable(TABLE_DATA, title)
			print(table_instance.table)

	except IOError:
		pass

def searchAdresse():
	adresse = input("\n[#][LittleBrother][Lookup][Adresse:~$ ")
	# clear()
	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }
	requete = requests.get(url+adresse, headers=headers)
	searchPJ(requete)

def searchNumber():
	num = input("\n[#][LittleBrother][Lookup][Phone:~$ ")
	url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui="
	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, br',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }
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

def searchUserName():
	username = input("\n[#][LittleBrother][Lookup][Pseudo:~$ ")
	# clear()
	# url = "https://www.google.com/search?num=100&q=\\\"%s\"\\"
	url = "https://www.google.com/search?num=100&q=\\%s\\"
	url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
	requete = requests.get(url % (username))
	requete2 = requests.get(url2 % (username))
	searchGoogle(requete=requete, requete2=requete2)

def google():
	nom = input("\n[#][LittleBrother][Lookup][nom, prenom, ville (...):~$ ")
	url = "https://www.google.com/search?num=20&q=\\%s\\"
	try:
		nom2 = nom.split(" ")
		nom = nom2[0]+'+'+nom2[1]
	except:
		pass
	requete = requests.get(url % (nom))
	searchGoogle(requete=requete)

def exifRead():
	photo = input("\n[#][LittleBrother][Lookup][Photo:~$ ")
	print("[+] Decode exif data...")
	with open(photo, 'rb') as f:
		tags = exifread.process_file(f)
		for tag in tags.keys():
			if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
				print("%s, value %s" % (tag, tags[tag]))

def receive_sms():
	def logTimes():
		times = time.strftime("%H:%M:%S")
		times = str(times)
		today = date.today()
		return(times)

	times = logTimes()
	receive = receiveSms()
	receive.searchServer()
	
	servers = receive.server_list
	numDic = {}
	url = receive.url_of_site

	title = ' Server '

	TABLE_DATA = [
		('ID', 'Numeo', 'Country'),
	]

	for num in servers:
		index = num[0]
		numero = num[1]
		country = num[2]

		numDic[index] = numero+'-'+country
	
		tuples = (index, "+"+numero, country)
		TABLE_DATA.append(tuples)
	
	table_instance = SingleTable(TABLE_DATA, title)
	print(table_instance.table)

	while True:
		s = input("\n[#][LittleBrother][SETool][Server ID:~$ ")
		try:
			int(s)
			path = numDic.get(str(s))
			break
		except:
			pass

	url = url+path

	receive.sms(url)

	lastMsg = receive.messageText

	times = logTimes()
	print("[I] Press 'Ctrl + C' pour quitter")
	print("[%s] Last message: %s" % (times, lastMsg))
	print("[%s] Listen..." % (times))

	try:
		while True:
			receive2 = receiveSms()
			receive2.sms(url)
			newMsg = receive2.messageText

			if newMsg != lastMsg:
				times = logTimes()
				print("[%s] New Message !" % (times))
				messages = receive2.messageText
				user = receive2.fromUser
				print("\n============ MESSAGE ============\nFrom: %s\nContent: %s\n=================================" % (user, messages))
				lastMsg = newMsg
			else:
				pass
	except KeyboardInterrupt:
		times = logTimes()
		print("\n[%s] Arret..." % (times))

def mailToIP():
	def isp_host(ip):
		url = "http://ip-api.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(response)
		return values['isp']

	def ip_loc(ip):
		url = "https://extreme-ip-lookup.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(response)

		return(values['country']+', '+values['region']+', '+ values['city'])

	def get_domain(ip):
		s = socket.gethostbyaddr(ip)
		return(s[0])

	files = input("\n[#][LittleBrother][Lookup][Entete:~$ ")
	if not os.path.exists(files):
		print("\n Fichier introuvable.")
	else:
		pass
	# clear()		
	print(wait+" Recherche en cours ...")
	f = open(files, 'r')

	for line in f:
		line.strip()
		if "From: " in line:
			print(information+" Message envoye par: "+line.replace("From: ",""))
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
	prenom = input("Prénom : ")
	nom = input("Nom : ")
	naissance = input("Date de naissance : ")
	telPortable = input("Numéro de téléphone portable : ")
	email = input("Email : ")
	fax = input("Fax : ")
	telFixe = input("Numéro de téléphone fixe:  ")
	ville = input("Ville : ")
	adresse = input("Adresse : ")
	cp = input("Code postal : ")
	ip = input("adresse IP : ")
	nameFichier = prenom.capitalize()+'_'+nom.replace(" ", "_").capitalize()+'.txt'
	if os.path.exists("Watched"):
		pass
	else:
		mkdir("Watched")

	f = open("Watched/"+nameFichier,'a')
	f.write("Prénom: "+prenom.capitalize())
	f.write("\nNom: "+nom.capitalize())
	f.write("\nDate de naissance: "+naissance)
	f.write("\nTéléphone portable: "+telPortable)
	f.write("\nTéléphone fixe: "+telFixe)
	f.write("\nEmail: "+email)
	f.write("\nFax: "+fax)
	f.write("\nVille: "+ville.title())
	f.write("\nAdresse: "+adresse.title())
	f.write("\nCode postal: "+cp)
	f.write("\nAdresse IP: "+ip)
	s = input(" Voulez vous ajoutez des resaux sociaux a la liste ? [y/N]: ").upper()
	if s == 'Y':
		while True:
			reseaux = input(" Réseaux sociaux (ex: Facebook...): ")
			name = input("Nom, pseudo, lien : ")
			f.write("\n"+reseaux.capitalize()+': '+name)
			c = input(" Rajouter un compte ? : [y/N]: ").upper()
			if c == 'Y':
				pass
			else:
				break
	else:
		pass
	s = input("Ajouter d'autre information ? [y/N]: ").upper()
	if s == 'Y':
		print(" ATTENTION! appuyez sur ENTRER une fois fini !\n")
		print(" Utilser des ';' pour espacer les infos")
		print("ex: couleur: bleu; bssid: FF:FF:FF:FF:FF; chat: miaou")
		infos = input("> ").replace("; ","\n")
		f.write('\n'+infos)
	else:
		pass
	print("\n[+] Fichier enregistre dans : 'Watched/"+nameFichier+"'")

def hashdecrypt():
	hash = input("\n[#][LittleBrother][Lookup][Hash:~$ ")
	print(wait+" Decrypt '%s'..." % (hash))
	lkd = leaked()
	password = lkd.hash(hash)
	
	if password:
		print(found+" %s : %s" % (hash, password))
	else:
		print(warning+" %s : Not match found." % (hash))

def showDataBase():
	def reverseName(name):
		nameSplit = name.split(" ")
		nameReversed = "%s %s" % (nameSplit[1], nameSplit[0])
		return(nameReversed.capitalize())

	def nameToFile(name):
		nameSplit = name.split(" ")
		nameCapital = []
		for n in nameSplit:
			nameCapital.append(n.capitalize())

		nameFile = nameCapital[0] + '_' + nameCapital[1] + '.txt'

		return(nameFile) 

	def readProfile(name):
		f = open('Watched/'+name, 'r')
		print("")
		for l in f:
			l = l.strip()
			print("%s" % (l))

	def showAllProfiles(ProfilesDic):

		table_data = [
			('ID', 'Name'),
		]

		for p in ProfilesDic:
			name = p
			num = ProfilesDic.get(name)
			name = name.replace("_", " ").replace(".txt", "")

			tuples = (str(num), name)
			table_data.append(tuples)

		table = AsciiTable(table_data)
		print(table.table)

	def searchProfiles():
		name = input("Name/ID: ")
		nameType =''

		try:
			int(name)
			nameType = 'ID'
		except:
			pass

		if nameType == 'ID' :
			numId = name
			print(wait+" Search ID %s..." % (name))
			for p in ProfilesDic:
				num = ProfilesDic.get(p)
				if num == int(numId):
					nameFile = p
					break
				else:
					nameFile = None
				# print(str(num)+'          ' + p)



			if nameFile is None:
				print(warning+" ID not found.")
			else:
				name = nameFile.replace("_", " ").replace(".txt", "")
				print("[+] Profile '%s' found." % (name))
				print("[ID] %s" % (numId))
				readProfile(nameFile)

		else:
			nameFile = nameToFile(name)

			find = ProfilesDic.get(nameFile)
			
			if not find:
				nameReversed = reverseName(name)
				nameReversedFile = nameToFile(nameReversed)
				find = ProfilesDic.get(nameReversedFile)
				
				if not find:
					print("[!] No profiles found for '%s'." % (name))
					# print("[?] View all profiles [ Y / N ]")
					# s = input(" ")
					# if s.upper() == 'Y':
					# 	showAllProfiles(ProfilesDic)
					# else:
					# 	pass
				
				else:
					num = ProfilesDic.get(nameReversedFile)
					print("[+] Profile found for name: %s." % (nameReversed))
					print("[*] Loading Profile...")
					print("[ID] %s" % (str(num)))
					readProfile(nameReversedFile)
			else:
				num = ProfilesDic.get(nameFile)
				print("[+] Profile '%s' found." % (name))
				print("[*] Loading Profile...")
				print("[ID] %s" % (str(num)))
				readProfile(nameFile)

	helpMsg = """
 Name                      Action
 ----                      ------
 Search Profiles           Recherche un profile dans la base de donnee.
 Show all Profiles         Affiche tout les profiles de la base de donnee.

 Exit Database             Quitte la base de donnee pour retourner au menu principal.
 Help message              Affiche se message
"""

	menuLogo = """
      :::::::::      ::: ::::::::::: :::           
     :+:    :+:   :+: :+:   :+:   :+: :+:          
    +:+    +:+  +:+   +:+  +:+  +:+   +:+          
   +#+    +:+ +#++:++#++: +#+ +#++:++#++:          
  +#+    +#+ +#+     +#+ +#+ +#+     +#+           
 #+#    #+# #+#     #+# #+# #+#     #+#            
#########  ###     ### ### ###     ###             
      :::::::::      :::      ::::::::  :::::::::: 
     :+:    :+:   :+: :+:   :+:    :+: :+:         
    +:+    +:+  +:+   +:+  +:+        +:+          
   +#++:++#+  +#++:++#++: +#++:++#++ +#++:++#      
  +#+    +#+ +#+     +#+        +#+ +#+            
 #+#    #+# #+#     #+# #+#    #+# #+#             
#########  ###     ###  ########  ##########       
"""
		
	menu = "\n[s] Search Profiles     [a] Show all Profiles    [e] Exit Database    [c] Clear screen   [h] Help message"

	clear()
	print(menuLogo)
	print("[*] Access to the Database...")
	print("[*] Search Data...")

	ProfilesDic = {}
	x = 1
		
	if os.path.exists("Watched"):
		print("[+] Data Found.")
	
	else:
		print("[!] Data not found ! ")
		print("[?] Want to create a new folder ? [ Y / N ]")
		s = input(" ")
		
		if s.upper() == 'Y':
			mkdir("Watched")
			print("[+] The file was successfully created.")
		
		else:
			pass
		
	datas = os.listdir("Watched")
	
	for data in datas:
		# print("%s) %s" % (str(x), data.replace(".txt", "")))
		ProfilesDic[data] = x
		x = x + 1
	
		if str(x) == '0':
			print("[!] No profiles found.")
	
	else:
		profilesCount = x-1
		print("[+] %s Profiles Found." % (str(profilesCount)))
	
		while True:
			print(menu)
	
			choix = input("\n[#][LittleBrother][Database:~$ ")
			
			if choix.lower() == 'h':
				print(helpMsg)
			elif choix.lower() == 's':
				searchProfiles()
			elif choix.lower() == 'a':
				showAllProfiles(ProfilesDic)
			elif choix.lower() == 'c':
				clear()
				print(menuLogo)
			elif choix.lower() == 'e':
				break
			else:
				print("Command not found")


header1 = """
  _      _ _   _   _      ____            _   _               
 | |    (_) | | | | |    |  _ \          | | | |              
 | |     _| |_| |_| | ___| |_) |_ __ ___ | |_| |__   ___ _ __ 
 | |    | | __| __| |/ _ \  _ <| '__/ _ \| __| '_ \ / _ \ '__|
 | |____| | |_| |_| |  __/ |_) | | | (_) | |_| | | |  __/ |   
 |______|_|\__|\__|_|\___|____/|_|  \___/ \__|_| |_|\___|_|   
"""

header2 = """

 /$$       /$$   /$$     /$$     /$$           /$$$$$$$                        /$$     /$$                          
| $$      |__/  | $$    | $$    | $$          | $$__  $$                      | $$    | $$                          
| $$       /$$ /$$$$$$ /$$$$$$  | $$  /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$      | $$|_  $$_/|_  $$_/  | $$ /$$__  $$| $$$$$$$  /$$__  $$ /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$ /$$__  $$
| $$      | $$  | $$    | $$    | $$| $$$$$$$$| $$__  $$| $$  \__/| $$  \ $$  | $$    | $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$  | $$ /$$| $$ /$$| $$| $$_____/| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$  | $$| $$_____/| $$      
| $$$$$$$$| $$  |  $$$$/|  $$$$/| $$|  $$$$$$$| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$  | $$|  $$$$$$$| $$      
|________/|__/   \___/   \___/  |__/ \_______/|_______/ |__/       \______/    \___/  |__/  |__/ \_______/|__/                                                                                                                       
"""

header5 = """
 ___        __  ___________  ___________  ___       _______                  
|"  |      |" \\("     _   ")("     _   ")|"  |     /"     "|                 
||  |      ||  |)__/  \\__/  )__/  \\__/ ||  |    (: ______)                 
|:  |      |:  |   \\_ /        \\_ /    |:  |     \\/    |                   
 \\  |___   |.  |   |.  |        |.  |     \\  |___  // ___)_                  
( \\_|:  \\  /\\  |\\  \\:  |        \\:  |    ( \\_|:  \\(:      "|                 
 \\_______)(__\\_|_)  \\__|         \\__|     \\_______)\\_______)                                                                               
 _______    _______     ______  ___________  __    __    _______   _______   
|   _  "\\  /"      \\   /    " \\("     _   ")/" |  | "\\  /"     "| /"      \\  
(. |_)  :)|:        | // ____  \\)__/  \\__/(:  (__)  :)(: ______)|:        | 
|:     \\/ |_____/   )/  /    ) :)  \\_ /    \\/      \\/  \\/    |  |_____/   ) 
(|  _  \\  //      /(: (____/ //   |.  |    //  __  \\  // ___)_  //      /  
|: |_)  :)|:  __   \\ \\        /    \\:  |   (:  (  )  :)(:      "||:  __   \\  
(_______/ |__|  \\___) \"_____/      \\__|    \\__|  |__/  \\_______)|__|  \\___) 
"""

header6 = """
 _      ____  ______  ______  _        ___  ____   ____    ___   ______  __ __    ___  ____  
| T    l    j|      T|      T| T      /  _]|    \\ |    \\  /   \\ |      T|  T  T  /  _]|    \\ 
| |     |  T |      ||      || |     /  [_ |  o  )|  D  )Y     Y|      ||  l  | /  [_ |  D  )
| l___  |  | l_j  l_jl_j  l_j| l___ Y    _]|     T|    / |  O  |l_j  l_j|  _  |Y    _]|    / 
|     T |  |   |  |    |  |  |     T|   [_ |  O  ||    \\ |     |  |  |  |  |  ||   [_ |    \\ 
|     | j  l   |  |    |  |  |     ||     T|     ||  .  Yl     !  |  |  |  |  ||     T|  .  Y
l_____j|____j  l__j    l__j  l_____jl_____jl_____jl__j\\_j \\___/   l__j  l__j__jl_____jl__j\\_j
"""

header7 = """
 _    _    _      _    _       ___             _    _             
| |  <_> _| |_  _| |_ | | ___ | . > _ _  ___ _| |_ | |_  ___  _ _ 
| |_ | |  | |    | |  | |/ ._>| . \| '_>/ . \ | |  | . |/ ._>| '_>
|___||_|  |_|    |_|  |_|\___.|___/|_|  \___/ |_|  |_|_|\___.|_|                                                       
"""

header8 = """
     _                   ______                        
 ___/__) ,        /)    (, /    )           /)         
(, /      _/__/_ //  _    /---(  __  ____/_(/    _  __ 
  /    _(_(__(__(/__(/_) / ____)/ (_(_) (__/ )__(/_/ (_
 (_____               (_/ (                            
        )                                              
"""

header9 = """
   __ _ _   _   _        ___           _   _               
  / /(_) |_| |_| | ___  / __\_ __ ___ | |_| |__   ___ _ __ 
 / / | | __| __| |/ _ \/__\// '__/ _ \| __| '_ \ / _ \ '__|
/ /__| | |_| |_| |  __/ \/  \ | | (_) | |_| | | |  __/ |   
\____/_|\__|\__|_|\___\_____/_|  \___/ \__|_| |_|\___|_|                                                              
"""

header11 = """
  |     _)  |    |    |        __ )               |    |                 
  |      |  __|  __|  |   _ \  __ \    __|  _ \   __|  __ \    _ \   __| 
  |      |  |    |    |   __/  |   |  |    (   |  |    | | |   __/  |    
 _____| _| \__| \__| _| \___| ____/  _|   \___/  \__| _| |_| \___| _|    
"""

header12 = """                                             
 __    _ _   _   _     _____         _   _           
|  |  |_| |_| |_| |___| __  |___ ___| |_| |_ ___ ___ 
|  |__| |  _|  _| | -_| __ -|  _| . |  _|   | -_|  _|
|_____|_|_| |_| |_|___|_____|_| |___|_| |_|_|___|_|  

                 \\\\
                  \\\\_   \\\\
                   (')   \\\\_
 LittleBrother -> / )=.---(') <- Privacy
                o( )o( )_-\_
"""

header13 = """
 __         __     ______   ______   __         ______                     
/\ \       /\ \   /\__  _\ /\__  _\ /\ \       /\  ___\                    
\ \ \____  \ \ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\                    
 \ \_____\  \ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\                  
  \/_____/   \/_/     \/_/     \/_/   \/_____/   \/_____/                  
                                                                           
 ______     ______     ______     ______   __  __     ______     ______    
/\  == \   /\  == \   /\  __ \   /\__  _\ /\ \_\ \   /\  ___\   /\  == \   
\ \  __<   \ \  __<   \ \ \/\ \  \/_/\ \/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/ /_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ /_/ 
"""

header14 = """
    __    _ __  __  __     ____             __  __             
   / /   (_) /_/ /_/ /__  / __ )_________  / /_/ /_  ___  _____
  / /   / / __/ __/ / _ \/ __  / ___/ __ \/ __/ __ \/ _ \/ ___/
 / /___/ / /_/ /_/ /  __/ /_/ / /  / /_/ / /_/ / / /  __/ /    
/_____/_/\__/\__/_/\___/_____/_/   \____/\__/_/ /_/\___/_/          
"""

header15 = """                                                                                             
,--.   ,--.  ,--.    ,--.  ,--.       ,-----.                  ,--.  ,--.                    
|  |   `--',-'  '-.,-'  '-.|  | ,---. |  |) /_ ,--.--. ,---. ,-'  '-.|  ,---.  ,---. ,--.--. 
|  |   ,--.'-.  .-''-.  .-'|  || .-. :|  .-.  \|  .--'| .-. |'-.  .-'|  .-.  || .-. :|  .--' 
|  '--.|  |  |  |    |  |  |  |\   --.|  '--' /|  |   ' '-' '  |  |  |  | |  |\   --.|  |    
`-----'`--'  `--'    `--'  `--' `----'`------' `--'    `---'   `--'  `--' `--' `----'`--'                                                                                                 
"""

header16 = """
 _____   __ __   __   __         ______              __   __               
|     |_|__|  |_|  |_|  |.-----.|   __ \.----.-----.|  |_|  |--.-----.----.
|       |  |   _|   _|  ||  -__||   __ <|   _|  _  ||   _|     |  -__|   _|
|_______|__|____|____|__||_____||______/|__| |_____||____|__|__|_____|__|                 
"""

header17 = """
 ____ ____ ____ ____ ____ ____      
||L |||i |||t |||t |||l |||e ||     
||__|||__|||__|||__|||__|||__||     
|/__\|/__\|/__\|/__\|/__\|/__\|     
 ____ ____ ____ ____ ____ ____ ____ 
||B |||r |||o |||t |||h |||e |||r ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
"""

header18 = """
                                                              
@@@      @@@ @@@@@@@ @@@@@@@ @@@      @@@@@@@@                
@@!      @@!   @!!     @!!   @@!      @@!                     
@!!      !!@   @!!     @!!   @!!      @!!!:!                  
!!:      !!:   !!:     !!:   !!:      !!:                     
: ::.: : :      :       :    : ::.: : : :: ::                 
                                                              
                                                              
@@@@@@@  @@@@@@@   @@@@@@  @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@  
@@!  @@@ @@!  @@@ @@!  @@@   @!!   @@!  @@@ @@!      @@!  @@@ 
@!@!@!@  @!@!!@!  @!@  !@!   @!!   @!@!@!@! @!!!:!   @!@!!@!  
!!:  !!! !!: :!!  !!:  !!!   !!:   !!:  !!! !!:      !!: :!!  
:: : ::   :   : :  : :. :     :     :   : : : :: ::   :   : : 
"""

def lb_header():

    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))

helpMain = """
 Name                       Action
 ----                       ------
 Lookup                     Faire des recherches sur une personne. 
 Social engineering         Utiliser des outils pour du social engineering.
 Make file                  Creer un fichier '.txt' pour y ecrire les infos obtenu.
 Show Database              Accedez a la base de donnee.

 Exit                       Quitter le logiciel.
 Help                       Affiche se message.
 Clear                      Efface l'ecran."""

helpLookup = """
 Name                             Action
 ----                             ------
 Personne lookup                  Faire des recherches avec un nom, prenom et (ville).
 Username lookup                  Faire des recherches avec un pseudonyme.  
 Adresse lookup                   Faire des recherches avec une adresse.
 Phone lookup                     Faire des recherches avec un numero de telephone.
 IP lookup                        Faire des recherches avec une adresse IP.
 SSID locator                     Faire des recherches avec une adresse MAC/BSSID
 Email lookup                     Faire des recherches avec une adresse email.
 Mail tracer                      Faire des recherches avec l'entete d'un mail.
 Exif data                        Faire des recherches grace au MetaData d'une photo.
 Google search                    Faire des recherches sur google.
 Facebook graphSearch             Faire des recherche grace au graphSearch.
 twitter info                     Recuperer les informations d'un compte Twitter.
 instagram info                   Recuperer les informations d'un compte Instagram.
 Hash decrypter                   Essaye de secrypter un hash via une base de donnée en ligne.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

helpSEtool = """
 Name                             Action
 ----                             ------
 SMS                              Recevoir des SMS sur des numeros libre. 
 Spam email                       Spamer une adresse email.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

mainOption = """
 [1] Lookup
 [2] Social engineering tool
 [3] Make file
 [4] Show Database

 [e] Exit script    [h] Help Message    [c] Clear Screen"""

text = ['Press F to hack', 'LEAVE ME HERE', 'The security is an illusion.', 'Profiler ctOS v2.0', 'DedSec takeover', 'Fsociety00.dat', 'Evil Corp',
 'Hello, friend', 'Hacking is our weapon', 'Hello, World', 'Login the world...', 'Big Brother is watching you.', 'Fuck Society', 'Wrench is calling...',
 'The control is an illusion.', 'install google_crack.exe...', 'you are free ! lol no, it was a joke.', 'you are a 1 or a 0 ?', 'Matraque: 1 - Genou: 0', 'Je veux que tu comprenne... Que tu ne sera plus jamais libre..', 'Tu pense être intouchable... Je vais briser tes illusion...',
 'je veux que tu sache... que tu n\'es plus anonyme...', 'Snapchat: T-Bone sent you a new message.', 'LulzSec <3 <3', '<3 Kraken Security OS is bae <3', 'DedSec is now in LinkedIn !',
 'FRANCE World champion 2018 !!', '~~(8:> is Defalt ~~(8:>', 'Facebook: Neo in a relationship with Elliot Alderson.', 'Just.. fuck the society.', 'locating 192.168.1.34 ... No match found', 
 '01110000 01100101 01101110 01101001 01110011', '49 20 4c 4f 56 45 20 55', 'Regarde derrière toi...']

# [!] LE JEUX COMMENCE A LA LIGNE 2000

lookupOption = """
 [1] Personne lookup          [8] Mail tracer                     [15] Hash decrypter
 [2] Username lookup          [9] Exif data
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearchq          
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup             [14] Check email

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

setoolOption = """
 [1] SMS
 [2] Spam email

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen 
"""

def menu():

	menu = """
                         __..--.._ 
  .....              .--~  .....  `.         Time:      [ %s | %s ]
.":    "`-..  .    .' ..-'"    :". `         Author:    [ Lulz3xploit ]
` `._ ` _.'`"(     `-"'`._ ' _.' '           Version:   [ %s ]
     ~~~      `.          ~~~                Internet:  [ %s ]
              .'                               
             /                             
            (                             %s
             ^---'                                                                                  
	""" % (Fore.YELLOW+str(today)+Fore.RESET, Fore.YELLOW+times()+Fore.RESET, Fore.YELLOW+str(__version__)+Fore.RESET, internet, random.choice(text))
	
	print(lb_header())
	print(menu)

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n[LittleBrother:~$ ")
	
		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '4':
			showDataBase()
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			doxMaker()
		elif choix.lower() == 'e':
			sys.exit(information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n[LittleBrother][Lookup:~$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne()
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber()
				elif lookup.lower() == '7':
					SearchEmail4()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse()
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					exifRead()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "14":
					check_email_exist()
				elif lookup.lower() == "15":
					hashdecrypt()

				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit(information+" Bye ! :)")
				else:
					print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(setoolOption)
			while True:
				se = input("\n[LittleBrother][SETool:~$ ")
				if se == 'h':
					print(helpSEtool)
				elif se.lower() == "1":
					receive_sms()
				elif se.lower() == "2":
					emailSpam()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(setoolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit(information+" Bye ! :) ")
				else:
					print("Commande introuvable")
		else:
			print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit(information+" Bye ! :)")