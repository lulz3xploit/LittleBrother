import requests, re, json, time

class instagramSearchTool:

	def getInfo(self, username):
		if username.startswith("http"):
			url = username
		else:
			url = "https://instagram.com/"+username

		page = requests.get(url).content.decode('utf-8')

		jsonData = re.findall(r"<script type=\"text/javascript\">(.*);</script>", page)
		jsonDataFound = jsonData[0].replace("window._sharedData = ", "")
		values = json.loads(jsonDataFound)
		
		urlAccount = url
		profilId = values['entry_data']['ProfilePage'][0]['graphql']['user']['id']
		bio = values['entry_data']['ProfilePage'][0]['graphql']['user']['biography']
		user = values['entry_data']['ProfilePage'][0]['graphql']['user']['username']
		name = values['entry_data']['ProfilePage'][0]['graphql']['user']['full_name']
		private = values['entry_data']['ProfilePage'][0]['graphql']['user']['is_private']
		follower = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
		friend = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']
		media = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
		profilPicHd = values['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']

		if not private:
			jsonData2 = re.findall(r"script type=\"application/ld\+json\">\n(.*)", page)
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
		else:
			url = None
			email = None
			adresse = None
			phone = None


		self.id = profilId
		self.profi_pic_hd = profilPicHd
		self.biography = bio
		self.username = user
		self.name = name
		self.private = private
		self.followers = follower
		self.friends = friend
		self.medias = media
		self.urlAccount = urlAccount

		self.email = email
		self.url = url
		self.adresse = adresse
		self.phone = phone

	def searchInsta(self, nom):
		encodeDic = {
			"%21": "!",
			"%23": "#",
			"%24": "$",
			"%26": "&",
			"%27": "'",
			"%28": "(",
			"%29": ")",
			"%2A": "*",
			"%2B": "+",
			"%2C": ",",
			"%2F": "/",
			"%3A": ":",
			"%3B": ";",
			"%3D": "=",
			"%3F": "?",
			"%40": "@",
			"%5B": "[",
			"%5D": "]", 
			"%20": " ",
			"%22": "\"",
			"%25": "%",
			"%2D": "-",
			"%2E": ".",
			"%3C": "<",
			"%3E": ">",
			"%5C": "\\",
			"%5E": "^",
			"%5F": "_",
			"%60": "`",
			"%7B": "{",
			"%7C": "|",
			"%7D": "}",
			"%7E": "~",
		}

		accountsList = []

		url = "https://encrypted.google.com/search?num=20&q=\\%s site:instagram.com\\" % (nom)
		page = requests.get(url).text
		urls = re.findall('url\\?q=(.*?)&', page)
		
		for url in urls:
			for char in encodeDic:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "/policies/faq" in url:
						if not "www.instagram.com/p/" in url:
							account = re.findall(r"instagram\.com/(.*?)/", url)[0]
							accountsList.append(account)
							
		self.accounts = accountsList

	def downloadPictures(url, path):
		if not path.endswith("/"):
			path += "/"

		def download(url, path, filename):
			r = requests.get(url)
			f = open(path+filename,'wb');
		
			for chunk in r.iter_content(chunk_size=255): 
				if chunk:
					f.write(chunk)

			f.close()

		page = requests.get(url).content.decode('utf-8')
		jsonData = re.findall(r"<script type=\"text/javascript\">(.*);</script>", page)
		jsonDataFound = jsonData[0].replace("window._sharedData = ", "")
			
		values = json.loads(jsonDataFound)
		
		nbMedia = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']

		if nbMedia > 11:
			nbMedia = 11

		MediaDic = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
		countX = 0

		while countX <= nbMedia:
			displayMedia = MediaDic[countX]['node']['display_url']
			isVideo = MediaDic[countX]['node']['is_video']
			location = MediaDic[countX]['node']['location']
			date = MediaDic[countX]['node']['taken_at_timestamp']
			date = time.ctime(int(date))

			try:
				infoMedia = MediaDic[countX]['node']['accessibility_caption']
			except:
				infoMedia = ""

			filename = url.split("/")
			filename = [i for i in filename if i != '']
			filename = filename[-1] + "_Picture_"+str(countX)+".png"

			if isVideo:
				typeMedia = "Video"
			else:
				typeMedia = "Photo"

			download(displayMedia, path, filename)
			print("[*] (%s) [%s] %s '%s' " % (str(countX), date, typeMedia, infoMedia))

			countX += 1
