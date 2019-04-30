from colorama 	import init, Fore,  Back,  Style
from threading 	import Thread

# /core
from core.searchEmail 		import SearchEmail
from core.searchPersonne 	import searchPersonne
from core.searchAdresse 	import searchAdresse
from core.searchUserName 	import searchUserName
from core.ipFinder 			import ipFinder
from core.bssidFinder 		import bssidFinder
from core.mailToIP 			import mailToIP
from core.employee_lookup 	import employee_lookup
from core.google 			import google
from core.facebookStalk 	import facebookStalk
from core.searchTwitter		import searchTwitter
from core.searchInstagram	import searchInstagram
from core.profilerFunc 		import profilerFunc
from core.searchNumber 		import searchNumber
from core.hashDecrypt 		import hashdecrypt
from core.passwordLeak		import passwordLeak


def watching(options):
	
	# Récupération des valeurs 'set' par l'utilisateur
	prenom    = options.get("PRENOM")
	nom       =	options.get("NOM")
	adresse   = options.get("LOCALISATION")
	email     =	options.get("EMAIL")
	phone     =	options.get("TELEPHONE")
	IP 		  = options.get("IP")
	SSID      = options.get("SSID")
	facebook  = options.get("FACEBOOK")
	twitter   = options.get("TWITTER")
	instagram = options.get("INSTAGRAM")
	hashpwd   = options.get("HASH")
	passwd 	  = options.get("PASSWORD")


	# Initialisation des variable Thread à 'None':
	thread_nameLookup 		= None
	thread_emailLookup 		= None
	thread_adresseLookup 	= None
	thread_phoneLookup 		= None
	thread_ipLookup 		= None
	thread_ssidLookup 		= None
	thread_facebookLookup 	= None
	thread_twitterLookup	= None
	thread_instaLookup 		= None
	thread_hashDecrypt 		= None
	thread_passwdLookup 	= None

	# Préparation et lancement du multi threading en verifiant l'existance des arguments
	if prenom or nom and adresse:
		if not prenom:
			prenom = ''
		if not nom:
			nom = ''
		if not adresse:
			adresse = ''
		thread_nameLookup = Thread(target=searchPersonne, args=(prenom, nom, adresse,))
		thread_nameLookup.start()
	
	if email:
		input(email)
		thread_emailLookup = Thread(target=searchEmail, args=(email,))
		thread_emailLookup.start()
	
	# if adresse:
	# 	thread_adresseLookup = Thread(target=searchAdresse, args=(adresse,))
	# 	thread_adresseLookup.start()
	
	# if phone:
	# 	thread_phoneLookup = Thread(target=searchNumber, args=(*arg))
	# 	thread_phoneLookup.start()
	
	# if IP:
	# 	thread_ipLookup = Thread(target=ipFinder, args=(*arg))
	# 	thread_ipLookup.start()
	
	# if SSID:
	# 	thread_ssidLookup = Thread(target=bssidFinder, args=(*arg))
	# 	thread_ssidLookup.start()
	
	# if facebook:
	# 	thread_facebookLookup = Thread(target=facebookStalk, args=(*arg))
	# 	thread_facebookLookup.start()
	
	# if twitter:
	# 	thread_twitterLookup = Thread(target=searchTwitter, args=(*arg))
	# 	thread_twitterLookup.start()
	
	# if instagram:
	# 	thread_instaLookup = Thread(target=searchInstagram, args=(*arg))
	# 	thread_instaLookup.start()
	
	# if hashpwd:
	# 	thread_hashDecrypt = Thread(target=hashdecrypt, args=(*arg))
	# 	thread_hashDecrypt.start()
	
	# if passwd:
	# 	thread_passwdLookup = Thread(target=passwordLeak, args=(*arg))
	# 	thread_passwdLookup.start()

	# Attente des threads utilisé
	if thread_nameLookup:
		thread_nameLookup.join()
	if thread_emailLookup:
		thread_emailLookup.join()
	if thread_adresseLookup:
		thread_adresseLookup.join()
	if thread_phoneLookup:
		thread_phoneLookup.join()
	if thread_ipLookup:
		thread_ipLookup.join()
	if thread_ssidLookup:	
		thread_ssidLookup.join()
	if thread_facebookLookup:	
		thread_facebookLookup.join()
	if thread_twitterLookup:
		thread_twitterLookup.join()
	if thread_instaLookup:
		thread_instaLookup.join()
	if thread_hashDecrypt:
		thread_hashDecrypt.join()
	if thread_passwdLookup:
		thread_passwdLookup.join()