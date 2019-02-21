from colorama import init, Fore,  Back,  Style
from core.watcher import watcher
from core.instagramSearchTool import instagramSearchTool
from core.facebookSearchTool import facebookSearchTool
from core.twitterSearchTool import twitterSearchTool
from core.Profiler import Profiler
from terminaltables import SingleTable
import time

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"

def profilerFunc(profile='', path=''):

	from datetime import date
	today = date.today()

	list_biographi = []
	list_placeVisited = []
	list_emails = []
	list_phones = []
	list_urls = []
	list_news = []

	if profile:
		profileName = profile['name']
		profileID = profile['id']
		file = profile['file']

		print("\n"+found+" Profil séléctionné: %s (%s)\n" % (profileName, profileID))

		pr = Profiler()
		dataProfile = pr.readProfile(file, path=path)

		if dataProfile:
			for data in dataProfile:
				if data.upper() == 'URL':
					url_twitter = dataProfile[data]['Twitter']
					url_instagram = dataProfile[data]['Instagram']
					url_facebook = dataProfile[data]['Facebook']

		name_txt = file.replace(".prfl", ".txt")
		path_txt = path+'\\'+name_txt
		
		twitterInfoDic = {"Twitter": {}}
		twittool = twitterSearchTool()
		twittool.getInfoProfile(url_twitter)
		twitterID, twitterInfoDic['Twitter']['id'] = twittool.id, twittool.id 
		twitterName, twitterInfoDic['Twitter']['name'] = twittool.name, twittool.name
		twitterUsername, twitterInfoDic['Twitter']['username'] = twittool.username, twittool.username
		twitterLocation, twitterInfoDic['Twitter']['location'] = twittool.location, twittool.location
		twitterUrlFound, twitterInfoDic['Twitter']['urlFound'] = twittool.url, twittool.url
		twitterBio, twitterInfoDic['Twitter']['description'] = twittool.description, twittool.description
		twitterUrlAccount, twitterInfoDic['Twitter']['urlAccount'] = url_twitter, url_twitter

		facebookInfoDic = {"Facebook": {}}
		fbtool = facebookSearchTool()
		fbtool.getInfoProfile(url_facebook)
		facebookID, facebookInfoDic['Facebook']['id'] = fbtool.facebookId, fbtool.facebookId
		faecbookName, facebookInfoDic['Facebook']['name'] = fbtool.name, fbtool.name
		facebookLocation, facebookInfoDic['Facebook']['location'] = fbtool.address, fbtool.address
		facebookWork, facebookInfoDic['Facebook']['job'] = fbtool.job, fbtool.job
		facebookUrl, facebookInfoDic['Facebook']['urlAccount'] = url_facebook, url_facebook
		facebookUsername, facebookInfoDic['Facebook']['username'] = fbtool.username, fbtool.username
		facebookAffiliation, facebookInfoDic['Facebook']['affiliations'] = fbtool.affiliations, fbtool.affiliations

		instagramInfoDic = {"Instagram": {}}
		instatool = instagramSearchTool()
		instatool.getInfo(url_instagram)
		instagramID, instagramInfoDic['Instagram']['id'] = instatool.id, instatool.id
		instagramBio, instagramInfoDic['Instagram']['description'] = instatool.biography, instatool.biography
		instagramUsername, instagramInfoDic['Instagram']['username'] = instatool.username, instatool.username
		instagramName, instagramInfoDic['Instagram']['name'] = instatool.name, instatool.name
		instagramEmail, instagramInfoDic['Instagram']['email'] = instatool.email, instatool.email
		instagramPhone, instagramInfoDic['Instagram']['phone'] = instatool.phone, instatool.phone
		instagramUrlFound, instagramInfoDic['Instagram']['urlFound'] = url_instagram, url_instagram
		instagramLocation, instagramInfoDic['Instagram']['location'] = instatool.adresse, instatool.adresse
		InstagramUrlAccount, instagramInfoDic['Instagram']['urlAccount'] = instatool.urlAccount, instatool.urlAccount

		for data in dataProfile:
			if data.upper() == 'TWITTER':
				if dataProfile[data]['name'] != twitterName:
					dataProfile[data]['name'] = twitterName
					list_news.append(twitterName)
				if dataProfile[data]['location'] != twitterLocation:
					dataProfile[data]['location'] = twitterLocation
					list_news.append(twitterLocation)
				if dataProfile[data]['urlFound'] != twitterUrlFound:
					dataProfile[data]['urlFound'] = twitterUrlFound
					list_news.append(twitterUrlFound)
				if dataProfile[data]['description'] != twitterBio:
					dataProfile[data]['description'] = twitterBio
					list_news.append(twitterBio)

			elif data.upper() == "FACEBOOK":
				if dataProfile[data]['name'] != faecbookName:
					dataProfile[data]['name'] = faecbookName
					list_news.append(faecbookName)
				if dataProfile[data]['location'] != facebookLocation:
					dataProfile[data]['location'] = facebookLocation
					list_news.append(facebookLocation)
				if dataProfile[data]['job'] != facebookWork:
					dataProfile[data]['job'] = facebookWork
					list_news.append(facebookWork)
				if dataProfile[data]['affiliations'] != facebookAffiliation:
					dataProfile[data]['affiliations'] = facebookAffiliation
					list_news.append(facebookAffiliation)

			elif data.upper() == 'INSTAGRAM':
				if dataProfile[data]['name'] != instagramName:
					dataProfile[data]['name'] = instagramName
					list_news.append(instagramName)
				if dataProfile[data]['location'] != instagramLocation:
					dataProfile[data]['location'] = instagramLocation
					list_news.append(instagramLocation)
				if dataProfile[data]['urlFound'] != instagramUrlFound:
					dataProfile[data]['urlFound'] = instagramUrlFound
					list_news.append(instagramUrlFound)
				if dataProfile[data]['description'] != instagramBio:
					dataProfile[data]['description'] = instagramBio
					list_news.append(instagramBio)


		dataProfile.update(twitterInfoDic)
		dataProfile.update(facebookInfoDic)
		dataProfile.update(instagramInfoDic)
		pr.writeProfile(file, path, dataProfile)

		if instagramEmail:
			list_emails.append(instagramEmail)
		
		placeVisited = "; ".join(list_placeVisited)

		for bio in list_biographi:
			regex = RegexTool(bio)
			emails = regex.Email().email
			phones = regex.Telephone().telephone
			urls = regex.Url().url

			for email in emails:
				list_emails.append(email)
			for phone in phone:
				list_phone.append(phone)
			for url in urls:
				list_urls.append(urls)

		if list_emails:
			emails = ", ".join(list_emails)
		else:
			emails = ''
			
		if list_phones:
			phones = ", ".join(list_phones)
		else:
			phones = ''

		if list_urls:
			urls = ", ".join(list_urls)
		else:
			urls = ''

		global_info = """
Date: %s

Profil ID : %s
Prénom, Nom: %s

Téléphone: %s
Emails: %s
Localisation: %s ; %s ; %s
Profession: %s
Pseudos: %s ; %s ; %s

Facebook  (%s) - %s
Twitter   (%s) - %s
Instagram (%s) - %s

Endroit visité: %s

Descriptions: 
%s	

%s
		""" % (
				today, profileID, profileName, phones, emails, 
				instagramLocation, twitterLocation, facebookLocation,
				facebookWork,
				facebookUsername, twitterUsername, instagramUsername,
				facebookID, facebookUrl, twitterID, twitterUrlAccount, instagramID, InstagramUrlAccount,
				placeVisited,
				twitterBio, instagramBio
				)

		w = watcher()
		w.instagramWatcher(url_instagram)
		w.twitterWatcher(url_twitter)

		lists = [w.medias, w.tweet]
		data = pr.timeSort(lists, reverse=True) # True: Ordre Decroissant, False: Ordre croissant (defaut : False)

		TABLE_DATA = [
			('Date', 'Domain', 'Publication', 'Localisation'),
		]

		for d in data:
			date = time.ctime(d)
			domain = data[d]['domain']
			
			if domain == "Twitter":
				tweet = data[d]['tweet'].replace("https://twitter.com", '')
				tuples = (date, domain, tweet, 'None')
				TABLE_DATA.append(tuples)
			
			else:
				publication = data[d]['urlMedia']
				publicationShort = shortCutUrl(publication)
				typePublication = data[d]['type']
				localisation = data[d]['location']
				
				if localisation:
					list_placeVisited.append(localisation)
				
				tuples = (date, domain, publicationShort, localisation)
				TABLE_DATA.append(tuples)

		tableLastPost = SingleTable(TABLE_DATA, " Last post ")

		print(tableLastPost.table)
		print("-------------")
		print("\n"+global_info)

		if len(list_news) > 0:
			newsItems = "; ".join(list_news)
			print("Nouveautés:\n"+newsItems)
		
		print("-------------")

		print(question+" Voulez-vous exporter les données récupérées dans '%s' ? " % (name_txt))

		while True:
			choix = input("\n [O/n]: ")

			if choix == '' or choix.upper() == 'O':
				f = pr.exportText(name_txt, path, global_info)
				if f:
					print("\n"+found+" Données exporté avec succès !")
					print(" %s" % (path_txt))
				else:
					print("\n"+warning+" Une erreur est survenue, les données n'ont pas pu être exporté !")
				break

			elif choix.upper() == 'N':
				break

		print("\n"+question+" Voulez-vous créer une copie de '%s' ? " % (name_txt))
		
		while True:
			choix = input("\n [o/N]: ")

			if choix.upper() == 'O':
				print("\n"+question+" Ou voulez-vous enregistrer la copie ?")
				path = input("\n Path: ")

				if path.endswith(".txt"):
					path = path_txt
				else:
					path = path+name_txt

				with open(path, 'w', encoding="utf-8") as f:
					f.write(global_info)
					f.close()

				print("\n"+found+" '%s' a été copié avec succès !" % (name_txt))
				break

			elif choix == '' or choix.upper() == 'N':
				break        

	else:
		print("\n"+warning+" Profile not found")