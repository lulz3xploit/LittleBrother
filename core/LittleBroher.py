# -*- coding: utf-8 -*-

__version__ = 6.0

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
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

checkVersion()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def loadlib():

	import requests, json

	import datetime

	# fonction
	from core.bssidFinder import bssidFinder
	from core.employee_lookup import employee_lookup
	from core.google import google
	from core.hashDecrypt import hashdecrypt
	from core.ipFinder import ipFinder
	from core.mailToIP import mailToIP
	from core.profilerFunc import profilerFunc
	from core.searchAdresse import searchAdresse
	from core.searchTwitter import searchTwitter
	from core.searchPersonne import searchPersonne
	from core.searchInstagram import searchInstagram
	from core.searchUserName import searchUserName
	from core.searchNumber import searchNumber
	from core.searchEmail import SearchEmail
	from core.Profiler import Profiler
	from core.facebookStalk import facebookStalk

	global monip, monpays, codemonpays, pathDatabase
	global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
	global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
	global Profiler


	monip = requests.get("https://api.ipify.org/").text

	monpays = requests.get("http://ip-api.com/json/"+monip).text
	value = json.loads(monpays)
	monpays = value['country']
	codemonpays = value['countryCode']

	pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
	pathDatabase = "\\".join(pathDatabase)+"\\Watched"

	if not os.path.exists(pathDatabase):
		os.mkdir(pathDatabase)

def loadingHack(importlib):
	chaine = "[*]"+' Start LittleBrother...'
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

def loadingTextPrint(importlib):
	string = "Start littlebrother"

	while importlib.is_alive():

		space = " " * 100
		sys.stdout.write("\r"+space)
		
		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@littlebrother:~$ "+string[:x]+"|")
			time.sleep(float(times))
			x += 1

def thread_loading():

	num = random.choice([1, 2, 3])

	importlib = threading.Thread(target=loadlib)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	elif num == 3:
		load = threading.Thread(target=loadingTextPrint(importlib))

	load.start()
	importlib.join()
	load.join()

thread_loading()

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)


from datetime import date
today_date = date.today()

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
 Employés recherche               Recherche les employés d'une entreprise.
 Google search                    Faire des recherches sur google.
 Facebook graphSearch             Faire des recherche grace au graphSearch.
 twitter info                     Recuperer les informations d'un compte Twitter.
 instagram info                   Recuperer les informations d'un compte Instagram.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

helpOtherTool = """
 Name                             Action
 ----                             ------
 Hash decrypter                   Essaye de décrypter un hash via une base de donnée en ligne.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

helpProfiler = """
 Name                      Action
 ----                      ------
 Search Profiles           Recherche un profile dans la base de donnee.
 Show all Profiles         Affiche tout les profiles de la base de donnee.

 Exit Database             Quitte la base de donnee pour retourner au menu principal.
 Help message              Affiche se message
"""

helpCountry = """
 Name                      Action
 ----                      ------
 FR                        Utiliser les services Francais.
 BE                        Utiliser les services Belge.
 CH                        Utiliser les services Suisse.
 LU                        Utiliser les services Luxembourgeois.
 All                       Utiliser tout les services.

 Back main menu            Revenir au menu principal.
 Exit script               Pour quitter le logiciel.
 Clear screen              Efface l'ecran."""

mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country

 [e] Exit script    [h] Help Message    [c] Clear Screen"""

text = ['Press F to hack', 'LEAVE ME HERE', 'The security is an illusion.', 'Profiler ctOS v2.0', 'DedSec takeover', 'Fsociety00.dat', 'Evil Corp',
 'Hello, friend', 'Hacking is our weapon', 'Hello, World', 'Login the world...', 'Big Brother is watching you.', 'Fuck Society', 'Wrench is calling...',
 'The control is an illusion.', 'install google_crack.exe...', 'you are free ! lol no, it was a joke.', 'you are a 1 or a 0 ?', 'Matraque: 1 - Genou: 0', 'Je veux que tu comprenne... Que tu ne sera plus jamais libre..', 'Tu pense être intouchable... Je vais briser tes illusion...',
 'je veux que tu sache... que tu n\'es plus anonyme...', 'Snapchat: T-Bone sent you a new message.', 'LulzSec <3 <3', '<3 Kraken Security OS is bae <3', 'DedSec is now in LinkedIn !',
 'FRANCE World champion 2018 !!', '~~(8:> is Defalt ~~(8:>', 'Facebook: Neo in a relationship with Elliot Alderson.', 'Just.. fuck the society.', 'locating 127.0.0.1 ... No match found', 
 '101100100101100 01100110010110011001', '101100 0110011001', 'c2V5cHRvbyBteSBsb3Zl', '1 item in your web hisotry: \'Fkk cuckold how to make your wife a hotwife zootube\'', '49 20 4c 4f 56 45 20 55', 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6VUS3OKVZGQYSLJQ3GO===', 'Regarde derrière toi...',
 'dW4gZCdldXggdHJvdWUgw6AgcXUnYSB0J3JlIHNlaW4gcXVlIHNpIGNlIGNldHRl', 'Send me nudes: Harry.Truman@nsa.gov', "Access point 'AP-Zone51' was found nearby."]

lookupOption = """
 [1] Personne lookup          [8] Mail tracer                     
 [2] Username lookup          [9] Employés recherche
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch          
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup             

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

otherToolOption = """
 [1] Hash decrypter

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen 
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles   
 [3] Create profile

 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg) 
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)

 [e] back main menu   [c] Clear screen   [h] Help message
"""

def menu():

	pr = Profiler()
	pr.loadDatabase(pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
                         __..--.._ 
  .....              .--~  .....  `.         Time:      [ %s | %s ]
.":    "`-..  .    .' ..-'"    :". `         Author:    [ Lulz3xploit ]      
` `._ ` _.'`"(     `-"'`._ ' _.' '           Version:   [ %s ]              
     ~~~      `.          ~~~                Pays:      [ %s | %s ]
              .'                             Database:  [ %s | %s Ko ]  
             /                             
            (                             %s
             ^---'                                                                                  
	""" % (Fore.YELLOW+str(today_date)+Fore.RESET, Fore.YELLOW+times()+Fore.RESET, 
		   Fore.YELLOW+str(__version__)+Fore.RESET, 
		   Fore.CYAN+monpays+Fore.RESET, codemonpays,
		   Fore.GREEN+str(nbProfilesBDD)+Fore.RESET, Fore.RED+str(sizeOfDB)+Fore.RESET,
		   random.choice(text)
		  )
	
	print(lb_header())
	print(menu)

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n LittleBrother("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
	
		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = Profiler()
				pr.loadDatabase(pathDatabase)
				database = pr.database
				
				choix = input("\n LittleBrother("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpMsg)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					profile = input(" Profil: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=pathDatabase)
					
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Prenom Nom)"+Fore.RESET)
					name = input(" Nom du Profil: ")
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					twitter = input(" Twitter: ")
					# print(found+" %s" % (twitter))
					instagram = input(" Instagram: ")
					# print(found+" %s" % (instagram))
					facebook = input(" Facebook: ")
					# print(found+" %s" % (facebook))

					info = {"URL": {"Twitter": twitter, "Facebook":facebook, "Instagram": instagram}}
					create = pr.writeProfile(fileName=name, path=pathDatabase, info=info)

					if create:
						print("\n"+found+" Le profil '%s' a été créé avec succès." % (name))
					else:
						print("\n"+warning+" Une erreur est survenue. Le profil '%s' n'a pas pu être créé." % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n LittleBrother("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber(codemonpays)
				elif lookup.lower() == '7':
					SearchEmail()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse(codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
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
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n LittleBrother("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n LittleBrother("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					codemonpays = "FR"
					monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					codemonpays = "BE"
					monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					codemonpays = "CH"
					monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					codemonpays = "LU"
					monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					codemonpays = "XX"
					monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")