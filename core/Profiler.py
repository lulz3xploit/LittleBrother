import os, sys, json
from terminaltables import SingleTable

class Profiler:

	def exportText(self, fileName='', path='', data=''):
		try:
			file = path+'\\'+fileName
			
			with open(file, 'w', encoding='utf-8') as f:
				f.write(data)
				f.close()
				
			return(True)
		except:
			return(False)

	def readProfile(self, fileName='', path=''):
		# try:
		if not path.endswith("/"):
			path += "/"

			if not fileName.endswith(".prfl"):
				fileName = fileName.replace(' ', '_')
				fileName += '.prfl'
		
			path += fileName
			data_prfl = ''

		with open(path) as f:
			data = f.read()
			
			if data != "":
				data = json.loads(data)
			else:
				data = None
			
			f.close()
			return(data)
		
		# except:
		# 	return(False)

	def writeProfile(self, fileName='', path='', info=''):
		if not path.endswith("/"):
			path += "/"

		fileName = fileName.replace(' ', '_')

		if not fileName.endswith(".prfl"):
			fileName += '.prfl'

		data_prfl = ''
		path += fileName

		try:
			with open(path, 'r') as prfl_data:
				data = prfl_data.read()
				prfl_data.close()
				
				if data != '':				
					data_prfl = json.loads(data)
					data_prfl.update(info)

		except FileNotFoundError:
			pass

		try:
			with open(path, 'w') as f:
				if data_prfl:
					data = json.dumps(data_prfl)
				else:
					data = json.dumps(info)	
				
				f.write(data)
				f.close()
			
			return(True)
		except:
			return(False)


	# def createProfile(name='', path='', **info):
	# 	try:
	# 		f = open(path+""+name, 'w')
			
	# 		for domain in info:
	# 			url = info.get(domain)
	# 			if url != "":
	# 				f.write("[URL] %s" % (url))

	# 		f.close()	
	# 		return(True)

	# 	except:
	# 		return(False)


			
	def loadDatabase(self, path):
		ProfilesDic = {}
		x = 1
	
		datas = os.listdir(path)
		size = os.path.getsize(path)
		sizeOfDB = size / 1000

		for data in datas:
			if not data.endswith(".ini") and data.endswith(".prfl"):
				ProfilesDic[data] = x
				x +=1

		self.database = ProfilesDic
		self.count = x -1
		self.size = sizeOfDB

	def timeSort(self, data, reverse=False):
		dictsJoined = {}
		dicts = {}
		keysList = []
		count = len(data)
		x = 0

		while int(x) < int(count):
			dico = data[x]

			for d in dico:
				if d in dicts and d != '':
					_d = int(d) +1
					dico[_d] = dico.get(d)
					del dico[d]

			dicts.update(dico)

			for key in dico:
				keysList.append(key)

			x +=1

		keysList.sort(reverse=reverse)

		for key in keysList:
			dictsJoined[key] = dicts.get(key)

		return(dictsJoined)
		
	def showAllProfiles(self, database=''):
		ProfilesDic = database
		table_data = [
			('ID', 'Name'),
		]

		for p in ProfilesDic:
			name = p
			num = ProfilesDic.get(name)
			name = name.replace("_", " ").replace(".prfl", "")

			tuples = (str(num), name)
			table_data.append(tuples)

		table = SingleTable(table_data)
		print(table.table)

	def searchDatabase(self, profile, database=''):
		def nameToFile(name):
			nameSplit = name.split(" ")
			nameCapital = []
			
			for n in nameSplit:
				nameCapital.append(n.capitalize())

			if len(nameSplit) == 1:
				nameFile = nameCapital[0]+'.prfl'

			elif len(nameSplit) > 1:
				nameFile = ""
				x = 0
			
				# while x < len(nameSplit):
				# 	nameFile += nameCapital[x]
					
				# 	if x == len(nameSplit) -1:
				# 		nameFile += '.prfl'
				# 	else:
				# 		nameFile += '_'

				# 	x +=1

				nameFile = "_".join(nameCapital)
				nameFile += ".prfl"

			else:
				nameFile = None

			return(nameFile)

		def reverseName(name):
			nameSplit = name.split(" ")
			if nameSplit == 2:
				nameReversed = "%s %s" % (nameSplit[1], nameSplit[0])
				return(nameReversed.capitalize())
			return name.capitalize()
		# def searchProfiles(profile, database=''):
		name = profile
		nameType = ''
		ProfilesDic = database

		try:
			int(name)
			nameType = 'ID'
		except:
			pass

		if nameType == 'ID' :
			numId = name

			for p in ProfilesDic:
				num = ProfilesDic.get(p)
				if num == int(numId):
					nameFile = p
					break
				else:
					nameFile = None

			if nameFile is None:
				dic = None
			else:

				# TABLE_DATA = [
				# 	("ID", 'Name'),
				# ]

				name = nameFile.replace("_", " ").replace(".prfl", "")
				# print(found+" Profil '%s' found." % (name))
				# print("[ID] %s" % (numId))
				# tuples = (numId, name)
				# TABLE_DATA.append(tuples)
				# table = SingleTable(TABLE_DATA, " Database ")
				# print(table.table)
				dic = {'id':numId, 'name':name, 'file':nameFile}


		else:
			nameFile = nameToFile(name)
			find = ProfilesDic.get(nameFile)

			dic = {'id':find, 'name':name, 'file':nameFile}

			if not find:
				if len(name.split(" ")) < 2:
					nameReversed = reverseName(name)
					nameReversedFile = nameToFile(nameReversed)
					find = ProfilesDic.get(nameReversedFile)

					if not find:
						dic = None

					else:
						num = ProfilesDic.get(nameReversedFile)

						dic = {'id': num, 'name':nameReversed, 'file':nameReversedFile}
						# TABLE_DATA = [
						# 	("ID", 'Name'),
						# ]

						# tuples = (num, nameReversed)
						# TABLE_DATA.append(tuples)
						# table = SingleTable(TABLE_DATA, " Database ")
						# print(table.table)
				else:
					dic = None
			else:
				num = find
				nameFile = [key for key,value in ProfilesDic.items() if value==num][0]
				name = nameFile.replace("_", " ").replace(".prfl", "")
				# TABLE_DATA = [
				# 	("ID", "Name"),
				# ]
				# tuples = (num, name)
				# TABLE_DATA.append(tuples)
				# table = SingleTable(TABLE_DATA, " Database ")
				# print(table.table)

				dic = {'id':num, 'name': name, 'file':nameFile}
		
		return(dic)
