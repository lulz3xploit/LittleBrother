import re

class SplitAddress:

	def __init__(self, adresse):
		self.adresse = adresse

	def get_addressPageBlanche(self):
		dic = {}

		testingCodePostal = None
		testingVille	  = None
		testingDep        = None		
		testingNumero 	  = None
		testingRue    	  = None

		rueInfo   = re.findall(r"([0-9]*|[A-Z]*) ([A-Z\s]+),", comparing)
		villeInfo = re.findall(r", ([0-9]{5}) ([A-Z\s]+)", comparing)

		if rueInfo:
			rueInfo = rueInfo[0]
			
			testingNumero = rueInfo[0]
			testingRue    = rueInfo[1]

		if villeInfo:
			villeInfo = villeInfo[0]

			testingCodePostal = villeInfo[0]
			testingVille	  = villeInfo[1]
			testingDep        = testingCodePostal[:2]

			dic['rumero'] 	   = testingNumero
			dic['rue']   	   = testingRue
			dic['code_postal'] = testingCodePostal
			dic['departement'] = testingDep

		return(dic)

