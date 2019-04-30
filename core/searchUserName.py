import requests

# /core
from core.searchGoogle import searchGoogle

# settings
import settings

def searchUserName(username):

	# color
	wait = settings.wait

	# get settings
	verrou = settings.verrou
	personneInfo = settings.personneInfo

	with verrou:
		print("\n"+wait+" Recherche '%s'..." % (username))

	url = "https://www.google.com/search?num=100&q=\\%s\\"
	url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
	requete = requests.get(url % (username))
	requete2 = requests.get(url2 % (username))
	searchGoogle(requete=requete, requete2=requete2)