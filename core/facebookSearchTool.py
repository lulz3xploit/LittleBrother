import requests, re, json

class facebookSearchTool:

	def searchFacebook(self, nom):

		url = "https://www.facebook.com/public/%s"

		name = nom.replace(" ","%20")

		try:
			page = requests.get(url % (name)).content.decode('utf-8')
		except:
			print(warning+" Aucun résultat.")

		data = page

		urlsAccount = re.findall('http[s]?://www.facebook.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)
		# nameAccount = re.findall("width=\"100\" height=\"100\" alt=\"([a-zA-Z0-9_ é , ]+)", data)
		nameAccount = re.findall("width=\"72\" height=\"72\" alt=\"([a-zA-Z0-9_ é , ]+)\" />", data)
		# print(nameAccount)

		urlList = []

		for nbr in urlsAccount:
			c = urlsAccount.count(nbr)
			if c > 1:
				urlsAccount.remove(nbr)

		for x in urlsAccount:
			if x.endswith("s"):
				urlsAccount.remove(x)

		for u in urlsAccount:
			if "/public/" in u or "/login.php" in u or "/recover" in u or "/help/" in u:
				pass
			elif "directory/pages_variations/" in u:
				pass
			elif "login/" in u:
				pass
			elif "&" in u:
				pass
			elif "/pages/" in u:
				pass
			else:
				urlList.append(u)

		usersAccount = []

		accountsFound = []

		for url in urlList:
			try:
				url = url.replace("https://www.facebook.com/", '')
				c = url.count("/")
				if c == 1:
					pass  # un url avec 2 fois "/" signifie que c'est une page.
				else:
					usersAccount.append(url)

			except:
				pass

		regroup = zip(usersAccount, nameAccount)
	
		return(regroup)

	def getInfoProfile(self, profile):
		if not "http" in profile:
			url = "https://www.facebook.com/"+profile
			username = profile
		else:
			url = profile
			username = profile.split("/")
			username = [i for i in username if i != ''][-1]

		try:
			page = requests.get(url).content.decode('utf-8')
			findId = re.search(r"entity_id=([0-9]+)", page).group(0)

			if findId:
				facebookID = findId.replace("entity_id=", '')
			else:
				facebookID = None

		except:
			facebookID = None

		try:
			jsonData = re.findall(r"type=\"application/ld\+json\">(.*?)</script>", page)[0]
			values = json.loads(jsonData)

			list_affiliation = []
			name = values['name']
			
			if "jobTitle" in values.keys():
				job = values['jobTitle']
			else:
				job = None

			if "address" in values.keys():
				address = values['address']['addressLocality']
			else:
				address = None

			affiliationsName = values['affiliation']


			count_affiliation = len(affiliationsName)
			x = 0
			
			while x < int(count_affiliation):
				nameAffiliation = affiliationsName[x]['name']
				list_affiliation.append(nameAffiliation)
				x +=1

			self.facebookId = facebookID
			self.name = name
			self.profile = url
			self.username = username
			self.job = job
			self.address = address
			self.affiliations = list_affiliation
		
		except:
			self.facebookId = None
			self.name = None
			self.profile = None
			self.username = None
			self.job = None
			self.address = None
			self.affiliations = None


		# name = re.search(r'pageTitle\">(.*)</title>', page).group(0)
			
		# if name:
		# 	name = name.replace("pageTitle\">", '').replace("| Facebook</title>", '')
		# 	self.name = name

		# else:
		# 	self.name = "None"

		# works = re.findall(r"<div class=\"_2lzr _50f5 _50f7\"><a href=\"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\">([a-zA-Z0-9_ - à é è ê ù ç ô ò û]+)", page)

		# if works:
		# 	self.work = works
		# else:
		# 	self.work = "None"

		# locations = re.findall(u"<span class=\"_2iel _50f7\"><a href=\"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\">([a-zA-Z0-9_ - à é è ê ù ç ô ò û]+)", page)

		# if locations:
		# 	self.location = locations
		# else:
		# 	self.location = "None"

		# img = re.findall(r"<img class=\"_11kf img\" alt=\".*\" src=\"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)\"", page)
		
		# if img:
		# 	img = img[0].replace("amp;", "")
		# 	self.img = img
		# else:
		# 	self.img = None

	def searchPageLiked(self, profile):
		if not "http" in profile:
			profile = "https://www.facebook.com/"+profile

		nom = profile.replace("https://www.facebook.com/", '')

		page = requests.get(profile).content.decode('utf-8')
		
		urlsPages = re.findall('http[s]?://www.facebook.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', page)
		
		for nbr in urlsPages:
			c = urlsPages.count(nbr)
			if c > 1:
				urlsPages.remove(nbr)

		pagesLiked = []
		for url in urlsPages:
			if "/public/" in url or "/login.php" in url or "/recover" in url or "/help/" in url:
				pass
			else:
				if nom in url:
					pass
				else:
					pagesLiked.append(url)

		return(pagesLiked)