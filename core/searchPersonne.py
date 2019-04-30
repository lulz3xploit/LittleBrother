import requests
# from colorama 		import Fore
from terminaltables	import SingleTable

# settings
import settings

# /core
from core.searchPJ 					import searchPJ
from core.searchInfoNumero 			import searchInfoNumero
from core.searchYellowLU 			import searchYellowLU
from core.searchLocalCH 			import searchLocalCH
from core.searchPageDor 			import searchPageDor
from core.facebookSearchTool 		import facebookSearchTool
from core.twitterSearchTool 		import twitterSearchTool
from core.instagramSearchTool 		import instagramSearchTool
from core.searchCopainsdavant 		import searchCopainsdavant
from core.searchPersonneLinkedin 	import searchPersonneLinkedin

# /utils
from utils.likeThis    import likeThis
from utils.departement import departement

def searchPersonne(prenom, nom, city):

	nomComplet = nom+' '+prenom

	# color
	personneTitle	 = settings.personneTitle
	particulierTitle = settings.particulierTitle
	copainTitle 	 = settings.copainTitle
	linkedinTitle 	 = settings.linkedinTitle
	facebookTitle 	 = settings.facebookTitle
	twitterTitle 	 = settings.twitterTitle
	instagramTitle 	 = settings.instagramTitle
	wait			 = settings.wait
	found 			 = settings.found
	info 			 = settings.information
	warning          = settings.warning
	msg 			 = personneTitle

	# get settings
	codemonpays  = settings.codemonpays
	verrou 		 = settings.verrou
	personneInfo = settings.personneInfo

	# Ajout des informations connues
	personneInfo['nom_complet'] = nomComplet
	personneInfo['prenom'] 		= prenom
	personneInfo['adresse'] 	= city 
	personneInfo['nom'] 		= nom 

	# Récupération des informations connues utile pour ce module de recherche
	prenomSaved 	  = personneInfo['prenom']
	nomCompletSaved   = personneInfo['nom_complet']
	telephoneSaved    = personneInfo['telephone']
	nomSaved		  = personneInfo['nom']
	adresseSaved 	  = personneInfo['adresse']
	facebookSaved 	  = personneInfo['facebook']
	twitterSaved 	  = personneInfo['twitter']
	instaSaved 		  = personneInfo['instagram']
	linkedinSaved 	  = personneInfo['linkedin']
	copainDavantSaved = personneInfo['copain_davant']

	nom = nomComplet
	nom = nom.strip()

	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
	    'referrer': 'https://google.com',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    	'Accept-Encoding': 'utf-8',
    	'Accept-Language': 'en-US,en;q=0.9',
    	'Pragma': 'no-cache'
    }

	msgParticulier = msg+particulierTitle

	with verrou:
		msg1 = wait+msgParticulier+" Recherche de '%s' à '%s'" % (nom, city)
		print(msg1)


	if codemonpays == 'FR':
		# Page Jaune search
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
		# url = url.replace("~", "")
		requete = requests.get(url.format(nom, city), headers=headers)
		regroup = searchPJ(requete)
		
		if regroup:
			for infos in regroup:
				nameFound 	   = infos[0]
				adresseFound   = infos[1].replace("\n", " ")
				phoneFound 	   = infos[2]
				operateurFound = infos[3]

				with verrou:
					msg1 = info+msgParticulier+" Un certain '%s' trouvé à '%s'" % (nameFound, adresseFound)
					msg2 = info+msgParticulier+" Vérification des similitudes entre '%s' et '%s'" % (nameFound, nomCompletSaved)
					msg3 = info+msgParticulier+" Vérification des similitudes entre '%s' et '%s'" % (adresseFound, adresseSaved)
					
					print(msg1)
					print(msg2)
					print(msg3)

				Lt = likeThis(nomCompletSaved, nameFound)
				sameName = Lt.sameString()

				Lt = likeThis(adresseSaved, adresseFound)
				sameAdresse = Lt.sameStringAdresse() 

				if sameName and sameAdresse :
					personneInfo['nom_complet'] = nameFound
					personneInfo['adresse'] 	= adresseFound
					personneInfo['operateur'] 	= operateurFound
					personneInfo['prenom']		= prenomSaved.replace("~", "")
					personneInfo['nom']			= nomSaved.replace("~", "")
				
					if telephoneSaved:
						phoneFound = telephoneSaved +', '+ phoneFound
				
					personneInfo['telephone'] = phoneFound
					
					with verrou:
						msg1 = found+msgParticulier+" Information retrouvé: %s" % (nameFound)
						msg2 = found+msgParticulier+" Information retrouvé: %s" % (adresseFound)
						msg3 = found+msgParticulier+" Information retrouvé: %s" % (phoneFound)
						msg4 = found+msgParticulier+" Information retrouvé: %s" % (operateurFound)
						msg5 = info+msgParticulier+" Recherche terminé avec succès"

						print(msg1)
						print(msg2)
						print(msg3)
						print(msg4)
						print(msg5)

					# Quand on à récupéré toute les infos on peut quitter la verification.
					break
				
				else:
					with verrou:
						msg1 = warning+msgParticulier+" Aucune similitudes trouvé pour '%s'" % (nameFound)
						msg2 = warning+msgParticulier+" Aucune similitudes trouvé pour '%s'" % (adresseFound)

						print(msg1)
						print(msg2)

	elif codemonpays == 'BE':
		# Page D'or search
		url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
		requete = requests.get(url.format(nom, city), headers=headers)
		searchPageDor(requete)

	elif codemonpays == 'CH':
		# Suisse search
		url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
		searchLocalCH(url.format(city, nom))

	elif codemonpays == 'LU':
		# Luxembourg search
		url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
		searchYellowLU(url.format(nom))

	else:
        # Recherche FR
		url = "https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={}&ou={}"
		requete = requests.get(url.format(nom, city), headers=headers)
		searchPJ(requete)

		# Recherche BE
		url = "https://www.pagesblanches.be/chercher/personne/{}/{}/"
		requete = requests.get(url.format(nom, city), headers=headers)
		searchPageDor(requete)

		# Recherche CH
		url = "https://tel.local.ch/fr/q?area={}&city=&company=&ext=1&name={}&phone=&rid=455h&street=&typeref=res"
		searchLocalCH(url.format(city, nom))

		# Recherche LU
		url = "https://www.yellow.lu/fr/pages-blanches/recherche?query={}"
		searchYellowLU(url.format(nom))

# Copain d'avant search
	with verrou:
		print(wait+personneTitle+copainTitle+" Recherche '%s' à '%s'" % (nom, city))	
	searchCopainsdavant(nom, city)

#########################


# LinkedIn search
	# with verrou:
	# 	print(wait+personneTitle+linkedinTitle+" Recherche '%s' à '%s'" % (nom, city))	
	
	# regroup = searchPersonneLinkedin(nom, city)

	# if regroup:
	# 	for infos in regroup:
	# 		nameFound = infos[0]
	# 		urlFound  = infos[1]

	# 		if not '+ profils' in nameFound:
	# 			if not 'Top ' in nameFound:
	# 				with verrou:
	# 					msg1 = info+personneTitle+linkedinTitle+" Un '%s' trouvé" % (nameFound)
	# 					msg2 = info+personneTitle+linkedinTitle+" Vérification des similitudes entre '%s' et '%s'" % (nameFound, nomCompletSaved)
	# 					print(msg1)
	# 					print(msg2)
						
	# 				Lt = likeThis(nomCompletSaved, nameFound)
	# 				same = Lt.sameStringAdresse() 
					
	# 				if same:
	# 					with verrou:
	# 						msg1 = found+personneTitle+linkedinTitle+" Information retrouvé : %s ( %s )" % (nameFound, urlFound)	 	
	# 						print(msg1)

	# 					personneInfo['linkedin'] = nameFound

	# 				else:
	# 					msg1 = warning+personneTitle+linkedinTitle+" Aucune similitudes trouvé pour '%s'" % (nameFound)
	# 					print(msg1)
# Facebook search
	with verrou:
		print(wait+personneTitle+facebookTitle+" Recherche '%s'" % (nom))		
	fbtool = facebookSearchTool()
	accountsFb = fbtool.searchFacebook(nom)

	for account in accountsFb:
		nameFound	  = account[1]
		usernameFound = account[0]
		
		fbtool.getInfoProfile(usernameFound)
		locFound = fbtool.address

		if not locFound:
			locFound = ''

		with verrou:
			msg1 = info+personneTitle+facebookTitle+" Un certain '%s' alias '%s' à '%s' trouvé" % (nameFound, usernameFound, locFound)
			msg2 = info+personneTitle+facebookTitle+" Vérification des similitudes entre '%s' et '%s'" % (nameFound, nomCompletSaved)
			msg3 = info+personneTitle+facebookTitle+" verification des similitudes entre '%s' et '%s'" % (locFound, adresseSaved)

			print(msg1)
			print(msg2)
			print(msg3)

		Lt       = likeThis(nomCompletSaved, nameFound)
		sameName = Lt.sameString()

		if locFound:
			Lt          = likeThis(adresseSaved, locFound)
			sameAdresse = Lt.sameStringAdresse()
		else:
			sameAdresse = True

		if sameName and sameAdresse:
			with verrou:
				msg1 = found+personneTitle+facebookTitle+" Information trouvé : %s" % (nameFound)
				msg2 = found+personneTitle+facebookTitle+" Information trouvé : %s" % (usernameFound)
				msg3 = found+personneTitle+facebookTitle+" Information trouvé : %s" % (locFound)

				print(msg1)
				print(msg2)
				print(msg3)

			personneInfo['facebook'] = usernameFound
			personneInfo['pseudos']  = usernameFound
			personneInfo['lieux']    = locFound

			break

		else:
			with verrou:
				msg1 = warning+personneTitle+facebookTitle+" Aucune similitudes trouvé pour '%s'" % (nameFound)
				msg2 = warning+personneTitle+facebookTitle+" Aucune similitudes trouvé pour '%s'" % (locFound)

				print(msg1)
				print(msg2)

	
# Twitter Search
	with verrou:
		print(wait+personneTitle+twitterTitle+" Recherche '%s'" % (nom))		

	twitool = twitterSearchTool()
	accountTwitter = twitool.searchTwitter(nom)

	for account in accountTwitter:
		nameFound 	  = account[1]
		usernameFound = "@" + account[0]

		twitool.getInfoProfile(account[0])
		
		location = twitool.location
		date 	 = twitool.birth
		bio 	 = twitool.description
		url 	 = twitool.url

		with verrou:
			msg1 = info+personneTitle+twitterTitle+" Un certain '%s' alias '%s' à '%s'" % (nameFound, usernameFound, date)
			print(msg1)

		Lt 		 = likeThis(nomCompletSaved, nameFound)
		sameName = Lt.sameString()

		if locFound:
			Lt 			= likeThis(adresseSaved, locFound)
			sameAdresse = Lt.sameStringAdresse() 
		else:
			sameAdresse = True

		if sameName and sameAdresse:
			with verrou:
				msg1 = found+personneTitle+twitterTitle+" Information trouvé : %s" % (nameFound)
				msg2 = found+personneTitle+twitterTitle+" Information trouvé : %s" % (usernameFound)
				msg3 = found+personneTitle+twitterTitle+" Information trouvé : %s" % (locFound)
				msg4 = found+personneTitle+twitterTitle+" Information trouvé : %s" % (bio)
				msg5 = found+personneTitle+twitterTitle+" Information trouvé : %s" % (date)

				print(msg1)
				print(msg2)
				print(msg3)
				print(msg4)
				print(msg5)

		else:
			pass



# Instagram search
	with verrou:
		print(wait+personneTitle+instagramTitle+" Recherche '%s'" % (nom))	
	title = " Instagram "

	instatls = instagramSearchTool()
	instatls.searchInsta(nom)

	accounts = instatls.accounts

	count = len(accounts)

	TABLE_DATA = [
		('Name', 'User'),
	]

	x = 0

	for account in accounts:
		url = "https://instagram.com/"+account
		i = instagramSearchTool()
		i.getInfo(url)

		name = i.name

		tuples = (name, account)
		TABLE_DATA.append(tuples)
		
		x +=1

		if count > 0:
			table = SingleTable(TABLE_DATA, title)
			# print(table.table)
