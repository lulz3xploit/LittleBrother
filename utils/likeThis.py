import re

# /utils
from utils.delAccent   import delAccent
from utils.departement import departement

# /lib
from lib.SplitAddress import SplitAddress

class likeThis:

	def __init__(self, compared, comparing):
		self.compared  = delAccent(compared)
		self.comparing = delAccent(comparing)
		if '~' in compared:
			tild = True
			compared = compared.strip("~")
		else:
			tild = None

		self.tild = tild

	def sameString(self):
		compared  = self.compared
		comparing = self.comparing

		same = None

		compared  = compared.upper()
		comparing = comparing.upper()
		compared  = compared.strip("-")
		comparing = comparing.strip("-")

		compared  = compared.split(" ")
		comparing = comparing.split(" ")

		lenComparing = len(comparing)

		count = 0
		for comparedChar in compared:
			if comparedChar in comparing or self.tild:
				count += 1
				
		if count == lenComparing:
			same = True

		return(same)

	def sameStringAdresse(self):
		compared  = self.compared.upper()
		comparing = self.comparing.upper()
		comparing = comparing.strip("-")

		same = None

		comparedSplited  = compared.split(" ")

		# Information retrouvée
		rueInfo   = re.findall(r"([0-9]*|[A-Z]*) ([A-Z\s]+),", comparing)
		villeInfo = re.findall(r", ([0-9]{5}) (.*)", comparing)

		if rueInfo:
			rueInfo = rueInfo[0]
			
			testingNumero = rueInfo[0]
			testingRue    = rueInfo[1]
		else:
			testingNumero = None
			testingRue    = None

		if villeInfo:
			villeInfo = villeInfo[0]

			testingCodePostal = villeInfo[0]
			testingVille	  = villeInfo[1]
			testingDep        = testingCodePostal[:2]
		else:
			testingCodePostal = None
			testingVille	  = None
			testingDep        = None		

		if len(comparedSplited) == 1:
			# La localisation entrée par l'utilisateur et peut être un département/région ou une ville

			# Vérification si c'est un département
			dep = departement(compared)
			check = dep.get_codeDepartement()

			if check:
				codeDepartementSaved = check

				# Si c'est bien un département on le vérifie avec celui obtenue.
				if str(codeDepartementSaved) == str(testingDep):
					# On retournera 'True' Pour confirmer la similitude entre l'entrée de l'utilisateur et de l'adresse obtenue 
					same = True 

			# Vérification si c'est une ville
			# On vérifie si l'entrée de l'utilisateur est égal à la ville obtenue 
			if compared == testingVille:
				# On retournera 'True' Pour confirmer la similitude entre l'entrée de l'utilisateur et de l'adresse obtenue 
				same = True

		# Si l'entrée utilisateur est une ville suivi du département ou inversement
		elif len(comparedSplited) == 2:
			for arg in comparedSplited:
				dep  = departement(arg)
				code = dep.get_codeDepartement()

				if arg == testingVille:
					same = True
				else:
					same = None

				if code == testingDep:
					same = True
				else:
					code == None

		# On verifie quand meme si l'entrée de l'utilisateur équivaut à la ville
		if compared == testingVille:
			same = True

		# Verifie si l'utilisateur à rentré un numéro de rue
		foundNumeroSaved = re.search(r"^[0-9]+ ", compared)

		# Si l'utilisateur à utilisé un numéro de rue
		if foundNumeroSaved:
			# On vérifie si le numéro de rue défini par l'utilisateur est égal au numéro obtenu ou si c'est une approximation
			if numeroSaved.group() == testingNumero or self.tild:
				same = True

		# Sinon la seul entrée que l'utilisateur aurait pu entrer serait le nom de la rue
		else:
			# On vérifie si le nom de la rue défini par l'utilisateur est égal au numéro obtenu ou si c'est une approximation
			if compared == testingRue or self.tild:
				same = True

		return(same)