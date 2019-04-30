# /txt
from txt.departement import dict_departement

class departement:
	def __init__(self, code):
		self.code = code

	def isDepartement(self):
		codeTested = False
		if str(self.code) in dict_departement:
			codeTested = True
		
		return(codeTested)

	def get_departement(self):
		dep = None

		if self.isDepartement():
			dep = dict_departement[str(code)]
		
		return(dep)

	def get_codeDepartement(self):
		dep = self.code.capitalize()
		
		try:
			code = list(dict_departement.keys())[list(dict_departement.values()).index(dep)]
		except:
			code = None

		return(code)
