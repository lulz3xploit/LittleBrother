import os, datetime
import requests, json
from colorama import Fore
from threading import RLock

# /core
# from core.bssidFinder       import bssidFinder
# from core.employee_lookup   import employee_lookup
# from core.google            import google
# from core.hashDecrypt       import hashdecrypt
# from core.ipFinder          import ipFinder
# from core.mailToIP          import mailToIP
# from core.profilerFunc      import profilerFunc
# from core.searchAdresse     import searchAdresse
# from core.searchTwitter     import searchTwitter
# from core.searchPersonne    import searchPersonne
# from core.searchInstagram   import searchInstagram
# from core.searchUserName    import searchUserName
# from core.searchNumber      import searchNumber
# from core.searchEmail       import SearchEmail
from core.Profiler          import Profiler
# from core.facebookStalk     import facebookStalk

def init():
    global version
    global optionPersonne, countryList, personneInfo
    global monip, monpays, codemonpays, pathDatabase
    global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
    global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
    # global Profiler
    global warning, question, information, wait, found, tiret
    global personneTitle, facebookTitle, twitterTitle, linkedinTitle, copainTitle, particulierTitle, instagramTitle
    global verrou

    verrou = RLock()

    version = '6.0.2'

    monip = requests.get("https://api.ipify.org/").text

    monpays     = requests.get("http://ip-api.com/json/"+monip).text
    value       = json.loads(monpays)
    monpays     = value['country']
    codemonpays = value['countryCode']

    warning     = "["+Fore.RED+"!"+Fore.RESET+"]"
    question    = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
    information = "["+Fore.BLUE+"i"+Fore.RESET+"]"
    wait        = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
    found       = "["+Fore.GREEN+"+"+Fore.RESET+"]"
    tiret       = "["+Fore.CYAN+"-"+Fore.RESET+"]"

    personneTitle = "["+Fore.CYAN+"Personne"+Fore.RESET+"]"
    facebookTitle = "["+Fore.YELLOW+"Facebook"+Fore.RESET+"]"
    twitterTitle = "["+Fore.YELLOW+"Twitter"+Fore.RESET+"]"
    linkedinTitle = "["+Fore.YELLOW+"Linkedin"+Fore.RESET+"]"
    copainTitle = "["+Fore.YELLOW+"Copain d'avant"+Fore.RESET+"]"
    particulierTitle = "["+Fore.YELLOW+"Particulier "+codemonpays+Fore.RESET+"]"
    instagramTitle = "["+Fore.YELLOW+"Instagram"+Fore.RESET+"]"



    pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
    pathDatabase = "\\".join(pathDatabase)+"\\Watched"

    countryList = {
        "FR": "France",
        "BE": "Belgique",
        "LU": "Luxembourgs",
        "CH": "Suisse",
        "XX": "Europe"
    }

    optionPersonne = {
        "PRENOM":       None,
        "NOM":          None,
        "LOCALISATION": None,
        "EMAIL":        None,
        "TELEPHONE":    None,
        "PSEUDO":       None,
        "IP":           None,
        "SSID":         None,
        "FACEBOOK":     None,
        "TWITTER":      None,
        "INSTAGRAM":    None,
        "HASH":         None,
        "PASSWORD":     None,
    }

    personneInfo = {
        "prenom":        '',
        "nom":           '',
        "nom_complet":   '',
        "adresse":       '',
        "telephone":     '',
        "operateur":     '',
        "email":         '',
        "facebook":      '',
        "twitter":       '',
        "instagram":     '',
        "copain_davant": '',
        "linkedin":      '',
        "password":      '',
        "lieux":         '',
        "images":        '',
        "anniversaire":  '',
        "travail":       '',
        "ip":            '',
        "fai":           '',
        "ssid":          '',
        "pseudos":       '',
        "biographie":    '',
    }



    if not os.path.exists(pathDatabase):
        os.mkdir(pathDatabase)
