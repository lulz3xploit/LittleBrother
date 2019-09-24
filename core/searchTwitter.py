from core.twitterSearchTool import twitterSearchTool

def searchTwitter():
	username = input(" Username: ")
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
	geo = twitool.geo #
	verif = twitool.verified
	status = twitool.status
	langue = twitool.langue
	try:
		naissance = twitool.birth
	except:
		naissance = "None"
	print("\n[@%s]" % (username))
	print("\n[+] Name: %s" % (name))
	print("[+] Langue: %s" % (langue))
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
