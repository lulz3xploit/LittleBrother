import re, requests, json

class twitterSearchTool():

	def searchTwitter(self, nom):

		nom = nom.replace(" ", "%20")

		page = requests.get("https://twitter.com/search?f=users&vertical=default&q=%s" % (nom)).text #.content.decode('utf-8')
		datas = re.findall(r"data-screen-name=\"(.*) ", page)
		# data = data.replace("\"", '').replace("data-screen-name=", '').replace("data-name=", '')
		
		usernamesList = []
		namesList = []
		
		for d in datas:
			d = d.split("data-name=")
			usernamesList.append(d[0].replace("\" ", ''))
			namesList.append(d[1].replace("\"", ''))

		regroup = zip(usernamesList, namesList)

		return(regroup)

	def getInfoProfile(self, username):
		if username.startswith('http'):
			urlSite = username
		else:
			urlSite = "https://twitter.com/"+username

		profilId = None
		name = None
		username = None
		location = None
		url = None
		description = None
		protected = None
		followers = None
		friends = None
		create = None
		geo = None
		verified = None
		status = None
		langue = None
		urlAccount = None

		req = requests.get(urlSite)

		if req.status_code == 200:

			page = req.content.decode('utf-8')
			page0 = req.text

			jsonData = re.findall(r"<input type=\"hidden\" id=\"init-data\" class=\"json-data\" value=\"(.*)\">", page)
			data =  jsonData[0].replace("&quot;", "\"")

			values = json.loads(data)

			urlAccount = url
			birthDate = re.findall(r"ProfileHeaderCard-birthdateText u-dir\" dir=\"ltr\"><span class=\"js-tooltip\" title=\"Publique\">(.*)", page0)
			profilId = values['profile_user']['id_str']
			name = values['profile_user']['name']
			username = values['profile_user']['screen_name']
			location = values['profile_user']['location']
			url = values['profile_user']['url']
			description = values['profile_user']['description']
			protected = values['profile_user']['protected']
			followers = values['profile_user']['followers_count']
			friends = values['profile_user']['friends_count']
			favoris = values['profile_user']['favourites_count']
			create = values['profile_user']['created_at']
			geo = values['profile_user']['geo_enabled']
			verified = values['profile_user']['verified']
			status = values['profile_user']['statuses_count']
			langue = values['profile_user']['lang']

			if birthDate:
				self.birth = birthDate
			else:
				self.birth = "None"

		self.id = profilId
		self.name = name
		self.username = username
		self.location = location
		self.url = url
		self.description = description
		self.protected = protected
		self.followers = str(followers)
		self.friends = str(friends)
		self.create = create
		self.geo = geo
		self.verified = verified
		self.status = str(status)
		self.langue = langue
		self.urlAccount = urlAccount