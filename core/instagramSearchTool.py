import requests, re, json, time, random

# /core
from core.getUrlGoogleSearch import getUrlGoogleSearch
from core.RegexTool 		 import RegexTool
from core.shortCutUrl 		 import shortCutUrl

# /lib
from lib.download import download

class instagramSearchTool:
		
	def _getJsonData(self, page):
		jsonData 	  = re.findall(r"<script type=\"text/javascript\">(.*);</script>", page)
		
		if jsonData:
			jsonDataFound = jsonData[0].replace("window._sharedData = ", "")
			values 		  = json.loads(jsonDataFound)

		else:
			values = None

		return(values)

	def _getNameById(self, ownerId):
		username = None
		name 	 = None
		
		urlApi  = "https://i.instagram.com/api/v1/users/"
		urlApi += str(ownerId)
		urlApi += "/info/"
		
		req = requests.get(urlApi)

		if req.status_code == 200:
			value = json.loads(req.text)
			value = value['user']

			username = value['username']
			name 	 = value['full_name']

		return((username, name))

	def _scrapperInstaExplorer(self, page):
		dict_postMedia = {}

		values = self._getJsonData(page)
		
		try:
			medias = values['entry_data']['LocationsPage'][0]['graphql']['location']['edge_location_to_media']['edges']
		except:
			medias = values['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']

		count  = len(medias)
		
		x = 0
		while x < count:
			try:
				description = medias[x]['node']['edge_media_to_caption']['edges'][0]['node']['text']
			except:
				description = None

			ownerId = medias[x]['node']['owner']['id']
			media 	= medias[x]['node']['display_url']
			media 	= shortCutUrl(media)

			profile  = self._getNameById(ownerId)
			username = profile[0]
			name     = profile[1] 
				
			dico = {
				username: {
					"name" : name,
					"media": media,
					"id"   : ownerId,
				}
			}

			dict_postMedia.update(dico)

			x += 1

		return(dict_postMedia)


	def downloadPictures(self, url, path, filename):
		if not path.endswith("/"):
			path += "/"
		
		download(url, path, filename)


	def getInfo(self, username):
		profilId 	= None
		profilPicHd = None
		bio			= None
		user		= None
		name		= None
		private		= None
		follower	= None
		friend		= None
		media		= None
		urlAccount	= None
		email		= None
		url 		= None
		adresse 	= None
		phone 		= None

		if username.startswith("http"):
			urlSite = username
		else:
			urlSite = "https://instagram.com/"+username

		req = requests.get(urlSite)
		
		if req.status_code == 200:

			page = req.content.decode('utf-8')
			
			values = self._getJsonData(page)

			try:
				values = values['entry_data']['ProfilePage'][0]['graphql']['user']
			
				urlAccount 	= url
				profilId 	= values['id']
				bio 		= values['biography']
				user 		= values['username']
				name 		= values['full_name']
				private 	= values['is_private']
				follower 	= values['edge_followed_by']['count']
				friend 		= values['edge_follow']['count']
				media 		= values['edge_owner_to_timeline_media']['count']
				profilPicHd = values['profile_pic_url_hd']

				if not private:
					jsonData2 = re.findall(r"script type=\"application/ld\+json\">\n(.*)", page)
					
					if jsonData2:
						jsonDataFound2 = jsonData2[0]
						
						values = json.loads(jsonDataFound2)

						try:
							url = values['url']
						except:
							url = None

						try:
							email = values['email']
						except:
							email = None

						try:
							adresse = values['adresse']['addressLocality']
						except:
							adresse = None

						try:
							phone = values['telephone']
						except:
							phone = None
			except:
				pass		

		self.id 		  	= profilId
		self.profi_pic_hd 	= profilPicHd
		self.biography 		= bio
		self.username		= user
		self.name 			= name
		self.private 		= private
		self.followers 		= follower
		self.friends 		= friend
		self.medias 		= media
		self.urlAccount 	= urlAccount
		self.email 			= email
		self.url 			= url
		self.adresse 		= adresse
		self.phone 			= phone

	def searchInsta(self, nom):
		accountsList = []

		url  = "https://encrypted.google.com/search?num=20&q=\\%s site:instagram.com\\" % (nom)
		page = requests.get(url).text
		
		urls = getUrlGoogleSearch(page)

		for url in urls:
			if not "www.instagram.com/p/" in url:
				account = re.findall(r"instagram\.com/(.*?)/", url)
				if account:
					accountsList.append(account[0])
							
		self.accounts = accountsList

	def get_picturesInfo(self, url):
		if url.startswith("http"):
			url = url
		else:
			url = "https://instagram.com/"+url

		dict_picturesInfo = {}

		page = requests.get(url).content.decode('utf-8')

		values = self._getJsonData(page)
		
		try:
			nbMedia = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']

			if nbMedia > 11:
				nbMedia = 11

			MediaDic = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
			
			countX = 0
			while countX <= nbMedia:
				displayMedia = MediaDic[countX]['node']['display_url']
				isVideo = MediaDic[countX]['node']['is_video']
				date = MediaDic[countX]['node']['taken_at_timestamp']
				date = time.ctime(int(date))

				try:
					infoMedia = MediaDic[countX]['node']['accessibility_caption']
				except:
					infoMedia = ""

				try:
					location = MediaDic[countX]['node']['location']['name']
				except:
					location = None

				if isVideo:
					typeMedia = "Video"
				else:
					typeMedia = "Photo"


				dic = {
					countX: {
						"display"	   : displayMedia,
						"type_media"   : typeMedia,
						"date"		   : date,
						"info"		   : infoMedia,
						"localisation" : location
					}
				}

				countX += 1

				dict_picturesInfo.update(dic)

		except:
			pass

		return(dict_picturesInfo)


	def getMediaWithLoc(self, location):
		urlCity = []
		profilVisitedCity = {}

		url  = "https://encrypted.google.com/search?q=site:instagram.com inurl:/locations inurl:/"
		url += location

		page = requests.get(url).text

		urls = getUrlGoogleSearch(page)

		for url in urls:
			if "instagram.com/explore/locations/" in url:
				find = re.search(r"[0-9]+/", url)
				if find:
					place = re.findall(r"[0-9]+/(.*)", url)[0]
					place = place.replace("-", " ").replace("/", ", ").strip()
					
					if "?" in place:
						place = place.split("?")[:-1][0]

					urlCity.append(url)

		for url in urlCity:
			req = requests.get(url)
			
			if req.status_code == 200:
				profilVisitedCity = self._scrapperInstaExplorer(req.text)
				
				data = {"place":place}
				
				profilVisitedCity.update(data)

		return(profilVisitedCity)

	def searchByTag(self, tag):
		url = "https://www.instagram.com/explore/tags/"
		url += tag

		req = requests.get(url)

		if req.status_code == 200:
			profils = self._scrapperInstaExplorer(req.text)

			data = {"tag":tag}

			profils.update(data)

		return(profils)
