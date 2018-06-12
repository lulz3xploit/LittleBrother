# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
import re
import smtplib
import socket
import webbrowser
import sys
import json
import time
from datetime import date

# from PIL import Image
# from PIL.ExifTags import TAGS

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
		
		self.id = profilId
		self.bio = bio
		self.username = user
		self.name = name
		self.private = private
		self.follower = follower
		self.friend = friend
		self.media = media

class twitterSearchTool():

	def searchTwitter(self, nom):

		nom = nom.replace(" ", "%20")

		page = requests.get("https://twitter.com/search?f=users&vertical=default&q=%s" % (nom)).content.decode('utf-8')
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

		page = requests.get(url).content.decode('utf-8')

		jsonData = re.findall(r"<input type=\"hidden\" id=\"init-data\" class=\"json-data\" value=\"(.*)\">", page)
		data =  jsonData[0].replace("&quot;", "\"")

		values = json.loads(data)

		birthDate = re.findall(r"ProfileHeaderCard-birthdateText u-dir\" dir=\"ltr\"><span class=\"js-tooltip\" title=\"Publique\">(.*)", page)
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
		req = requests.get(url+num)
		page = req.content.decode('utf-8')
		p = []
		soup = BeautifulSoup(page, "html.parser")
		tags = soup("p")
		for n in tags:
			line = n.string
			p.append(line)
		ville2 = p[2]
		ville2 = ville2.strip()	

		self.location = location.get(pfx)

		if mob_fix(pfx) == 'Portable':
			self.phone_type = "Portable"
		elif mob_fix(pfx) == 'internet':
			self.phone_type = "Voip/FAI"
		else:
			self.phone_type = "Fixe"
		
		url = "http://www.smaltra.ovh/numero/%s/"

		page = requests.get(url % (num)).content.decode('utf-8')

		villeList = re.findall(r"<span class=\"grey-300\">Zone (.*):</span> ([a-zA-Z0-9_]+)</p>", page)
		operator = re.search(r"<span class=\"grey-300\">Op(.*)", page).group()
		date = re.search(r"<span class=\"grey-300\">Date (.*)", page).group()

		if villeList:
			pass
		else:
			ville = "None"

		for ville in villeList:
			ville = ville[1]
			break

		ville = ville.strip()
		ville = ville+" / "+ville2

		self.city = ville
		operator = operator.split("</span>")
		operator = operator[1].replace("<br/>", '')
		self.operator = operator.strip()
		date = date.split("</span>")
		date = date[1].replace("<br/>", "")
		self.date = date.strip()

class facebookSearchTool:

	def searchFacebook(self, nom):

		url = "https://www.facebook.com/public/%s"

		name = nom.replace(" ","%20")

		try:
			page = requests.get(url % (name)).content.decode('utf-8')
		except urllib2.HTTPError:
			print("[!] Aucun resultat.")
			quit()

		data = page

		urlsAccount = re.findall('http[s]?://www.facebook.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
		nameAccount = re.findall("width=\"100\" height=\"100\" alt=\"([a-zA-Z0-9_ ,]+)", data)

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
			else:
				if "/pages/" in u:
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

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit("[!] Veuillez lancer la version 3 de python.")

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

	print("[@%s]" % (username))
	print("\n[+] Name: %s" % (name))
	print("[+] ID: %s" % (profilId))
	print("[+] Protected: %s" % (protected))
	print("[+] Abonnees: %s | Abonnements: %s" % (followers, friend))
	print("[BIO] %s" % (description))
	print("[+] Ville: %s" % (location))
	print("[+] Naissance: %s"  % (date))
	print("[+] Url: %s" % (url))
	print("[+] Create: %s" % (dateCreate))

def searchInstagram():
	user = input("\n[#][LittleBrother][Lookup][Username:~$ ")

	insta = instagramGetInfo(user)

	name = insta.name
	userId = insta.id
	username = insta.username
	private = insta.private
	followers = insta.follower
	friend = insta.friend
	publication = insta.media
	bio = insta.bio

	print("\n[%s]" % (username))
	print("\n[+] Name: %s" % (name))
	print("[+] ID: %s" % (userId))
	print("[+] Protected: %s" % (private))
	print("[+] Abonnees: %s  |  Abonnements: %s" % (followers, friend))
	print("[+] Publication: %s" % (publication))
	print("[+] Bio: %s" % (bio))

def phoneNumber(num):
	phone = searchInfoNumero()
	phone.search(num)
	city = phone.city
	operator = phone.operator
	date = phone.date.title()
	location = phone.location
	_type = phone.phone_type
	# print("\n[%s]" % (num))
	print(" + Telephone: %s" % (_type))
	if location:
		print(" + Secteur: %s" % (location))
	else:
		pass
	try:
		print(" + Ville: %s" % (city))
	except:
		pass
	print(" + Operateur: %s" % (operator))
	print(" + Date: %s" % (date))

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

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

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
		print("[*] Connexion...")

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
				clear()
				print("{} -> {} ({})").format(spoof_mail, target_email, send)
				send = send+1
		except KeyboardInterrupt:
			print(str(send)+" mail envoye")
			sys.exit()
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

	if facebookID:

		print(resultProfile % (name, work, loc, ID))

		print(menuStalk)

		while True:
			s = input("\n[#][LittleBrother][Lookup][StalkFB:~$ ")
			if s == "help":
				print(helpMsgFbStalk)
			elif s == "clear":
				clear()
				print(menuStalk)
			elif s == "back":
				break
			elif s == "exit" or s == "quit":
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
	else:
		print("[!] Impossible de recuperer l'ID.")

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
	url = "https://extreme-ip-lookup.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
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

def SearchEmail4():
	email = input("\n[#][LittleBrother][Lookup][Email:~$ ")
	# email = email.replace("@", "%40")
	# clear()
	# url = "https://www.google.com/search?num=100&q=\%s\\"
	url = "https://www.google.fr/search?num=100&q=\\intext:\"%s\"\\"
	print(url % (email))
	requete = requests.get(url % (email)).content.decode('utf-8')
	urls = re.findall('url\\?q=(.*?)&', content)
	cout = len(urls) - 1
	print("[*] Scan %s Link..." % (str(cout)))
	x = 1
	for url in urls:
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				if not "webcache.googleusercontent.com/" in url:	
					try:
						# print("(%s) link scanned. " % (str(x)))
						text = requests.get(url).content.decode('utf-8')
						# print("Search...")
						combo = re.search(email+r":([a-zA-Z0-9_]+)", texte).group()
						if combo:
							print("[+] %s" % (combo))
					except:
						print("[?] %s " % (url))
					# x = x + 1

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
		 	birthdayList0.append("None.")
	
		for b in birthdayList0:
			birthdayList.append(str(b))

		travailList0 = soup.find_all("p", {"class": "title"})
		item = len(travailList0)
		if item == 0:
		 	travailList0.append("None.")
	
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
	for info in regroup:
		name = info[0]
		adresse = info[1]
		dateBirthday = info[2]
		travail = info[3]
		url = info[4]
		print("\n[Copaindavant] %s - %s" % (name, url))
		print("(+) Ville: %s" % (adresse))
		print("(+) Date: %s" % (dateBirthday))
		if travail != "None.":
			print("(+) Profession: %s" % (travail))


def searchPJ(requete='', num=''):
	def testResponse(requete):
		noReponse = soup.find("p", {"class": "wording-no-responses"})
		if noReponse:
			return 1
			# print("[!] Aucun resultattttt pour votre recherche... o_o' ")

	page = requete.content.decode('utf-8')
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
		# name = name.string.strip()
		# adresse = adresse.string.strip()
		# num = num.string.strip()
		# printResult(name, adresse, num)
	except AttributeError:
		pass

	namesList2 = []
	addressesList2 = []
	numesList2 = []

	# try:
	for name in nameList:
		namesList2.append(name.string)
	for addresse in addressList:
		addressesList2.append(addresse.string)
	for num in numList:
		numesList2.append(num.string)
	# except:
	# 	print("[!] Aucun resultat pour votre recherche... o_o'")

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
		content = requete2.content.decode('utf-8')
		urls = re.findall('url\\?q=(.*?)&', content)
		for url in urls:
			for char in encodeList:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					# if "insta" in url or "twitter" in url or "facebook" in url:
						print("[++] Possible connection: "+url)
	else:
		pass

	content = requete.content.decode('utf-8')
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		for char in encodeList:
			find = re.search(char, url)
			if find:
				charDecode = encodeDic.get(char)
				url = url.replace(char, charDecode)
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				# if "insta" in url or "twitter" in url or "facebook" in url:
					print("[+] Possible connection: "+url)

def searchPersonne():
	nom = input("\n[#][LittleBrother][Lookup][Prenom Nom:~$ ")
	city = input("\n[#][LittleBrother][Lookup][Ville/Departement:~$ ")
	# clear()
	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
	requete = requests.get(url.format(nom, city))
	print("[*] Recherche...")
	searchPJ(requete)
	# print("\n[*] Recherche Facebook...")
	try:
		searchCopainsdavant(nom, city)
		
		fbtool = facebookSearchTool()
		accountsFb = fbtool.searchFacebook(nom)
		for a in accountsFb:
			name = a[1]
			username = a[0]
			print("\n[Facebook] %s - %s" % (name, username))
			fbtool.getInfoProfile(username)
			loc = fbtool.location
			work = fbtool.work
			if loc != "None":
				print("(+) Location:  %s" % (loc))
			if work != "None":
				print("(+) Travail: %s" % (work))
		
		# searchFacebook(nom)

		twitool = twitterSearchTool()
		accountTwitter = twitool.searchTwitter(nom)
		for a in accountTwitter:
			name = a[1]
			username = "@"+a[0]
			print("\n[Twitter] %s - %s" % (name, username))
			twitool.getInfoProfile(a[0])
			
			location = twitool.location
			date = twitool.birth
			bio = twitool.description
			url = twitool.url
			
			if bio:
				print("(+) Bio: %s" % (bio))
			if location:
				print("(+) Ville: %s" % (location))
			if date != "None":
				print("(+) Naissance: %s"  % (date))
			if url:
				print("(+) Url: %s" % (url))

		# searchTwitterPersonne(nom)

	except IOError:
		pass

def searchAdresse():
	adresse = input("\n[#][LittleBrother][Lookup][Adresse:~$ ")
	# clear()
	url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=&ou="
	requete = requests.get(url+adresse)
	searchPJ(requete)

def searchNumber():
	num = input("\n[#][LittleBrother][Lookup][Phone:~$ ")
	# clear()
	#print("[*] Recherche...")
	url = "https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui="
	requete = requests.get(url+num)
	#phoneNumber(num)
	searchPJ(requete=requete, num=num)
	# phoneNumber(num)

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
		print("[!] Failed")

def reveiveSms():
	
	url = "https://www.receive-sms-online.info/"

	page = requests.get(url).content.decode('utf-8')

	serverList = re.findall(r"<a href=\"([0-9]+)-([a-zA-Z0-9_]+)", page)

	print("[*] Server online: \n")

	dicNum = {}

	n = 1

	for server in serverList:
		numero = server[0]
		country = server[1]

		dicNum[str(n)] = numero+'-'+country
		print("[%s] %s - +%s" % (str(n), country, numero)) 
		n = n + 1

	while True:
		s = input("\n[#][LittleBrother][SETool][Server Num:~$ ")
		try:
			int(s)
			path = dicNum.get(str(s))
			break
		except:
			pass

	page = requests.get(url+path).content.decode('utf-8')
	
	# print(page)

	fromUsersList = re.findall(r"data-label=\"From   :\">([a-zA-Z0-9_]+)</td>", page)
	messagesList = re.findall(r"data-label=\"Message:\">(.*)</td>", page)
	timeAgoList = re.findall(r"data-label=\"Added:\">(.*)</td>", page)

	regroup = zip(fromUsersList, messagesList, timeAgoList)

	for sms in regroup:
		user = sms[0]
		message = sms[1]
		time = sms[2]

		print("\n============\n%s (%s) :\n%s\n=============" % (user, time, message))

def mailToIP():
	def isp_host(ip):
		url = "http://ip-api.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(data)
		return values['isp']

	def ip_loc(ip):
		url = "https://extreme-ip-lookup.com/json/" + ip
		response = requests.get(url).content.decode('utf-8')
		values = json.loads(data)

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
	nameFichier = prenom.capitalize()+'_'+nom.capitalize()+'.txt'
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
		action = input("\n[#][LittleBrother][Database:~$ ")
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
		setool : Utiliser des outils pour du social engineering.
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
		photo : Faire des recherches grace au MetaData d'une photo.
		google : Faire des recherches sur google.
		facebook: Faire des recherche grace au graphSearch.
		twitter: Recuperer les informations d'un compte Twitter.
		instagram: Recuperer les informations d'un compte Instagram.

		back : Revenir au menu principal.
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""

helpSEtool = """
		sms : Recevoir des SMS sur des numeros libre. 
		spam: Spamer une adresse email.

		back : Revenir au menu principal.
		exit / quit  : Pour quitter le logiciel.
		clear : Efface l'ecran."""


menuLookup = """
            ______              
         .-'      `-.           
       .'            `.         
      /    01101       \        
     ;      10011      ;`       
     |     01110       |;        -------=+[  _LittleBrother_  ]__
     ;      1101001    ;|        ......................................
     '\               / ;        ------------=+[ Author: Lulz3xploit ]__
      \`.           .' /         ------------=+[ Version: 3.0 ]__
       `.`-._____.-' .'         
         / /`_____.-'            [%s] [%s]
        / / /                   
       / / /                           [%s]
      / / /                              
     / / /
    / / /
   / / /   _     _ _   _   _      ____            _   _            
  / / /   | |   (_) |_| |_| | ___| __ ) _ __ ___ | |_| |__   ___ _ __ 
 / / /    | |   | | __| __| |/ _ \  _ \| '__/ _ \| __| '_ \ / _ \ '__|  
/ / /     | |___| | |_| |_| |  __/ |_) | | | (_) | |_| | | |  __/ |      
\/_/      |_____|_|\__|\__|_|\___|____/|_|  \___/ \__|_| |_|\___|_|      
                                                        
        Tapez 'help' pour avoir plus d'information.
""" % (today, times(),testConnexion())

menu = """
                         __..--.._   
  .....              .--~  .....  `.    
.":    "`-..  .    .' ..-'"    :". `     -------=+[  _LittleBrother_  ]__
` `._ ` _.'`"(     `-"'`._ ' _.' '       ......................................
     ~~~      `.          ~~~            ------------=+[ Author: Lulz3xploit ]__
              .'                         ------------=+[ Version: 2.1 ]__
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
checkVersion()

try:
	while True:
		# clear()
		# print(menu)
		choix = input("\n[#][LittleBrother:~$ ")
		if choix.lower() == 'help':
			print(helpMsg)
		elif choix.lower() == 'lookup':
			clear()
			print(menuLookup)
			while True:
				lookup = input("\n[#][LittleBrother][Lookup:~$ ")
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
					SearchEmail4()
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
				elif lookup.lower() == "facebook":
					facebookStalk()
				elif lookup.lower() == "twitter":
					searchTwitter()
				elif lookup.lower() == "instagram":
					searchInstagram()
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
		elif choix.lower() == "setool":
			clear()
			print(menu)
			while True:
				se = input("\n[#][LittleBrother][SETool:~$ ")
				if se == 'help':
					print(helpSEtool)
				elif se.lower() == "sms":
					reveiveSms()
				elif se.lower() == "spam":
					emailSpam()
				elif se.lower() == "back":
					clear()
					print(menu)
					break
				elif se.lower() == "clear":
					clear()
					print(menu)
				elif se == '':
					pass
				elif se.lower() == "exit" or se.lower() == "quit":
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
	sys.exit("\nBye ! :)")