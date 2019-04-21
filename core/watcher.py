import requests, re, json, time

class watcher:

	def twitterWatcher(self, user):
		dicTweet = {}

		if not user.startswith('http'):
			urlAccount = "https://twitter.com/"+user
		else:
			urlAccount = user

			req = requests.get(urlAccount)
			page = req.text

			if req.status_code == 200:
				try:
					tweets = re.findall(r"href=\"/.*/status/([0-9]+)\" .* data-time=\"([0-9]+)\" ", page)
					countX = len(tweets)

					for t in tweets:
						tweet = urlAccount+"/status/"+t[0]
						timestamp = int(t[1])
						date = time.ctime(int(timestamp))

						dicTweet[timestamp] = {"domain":"Twitter", "tweet":tweet, "date":date}
						countX += 1
				except:
					dicTweet = {}

		self.tweet = dicTweet

	def instagramWatcher(self, user):
		if not user.startswith('http'):
			urlAccount = "https://instagram.com/"+user
		else:
			urlAccount = user

		picturesList = []

		req = requests.get(urlAccount)

		if req.status_code == 200:
			page = req.content.decode('utf-8')
			jsonData = re.findall(r"<script type=\"text/javascript\">(.*);</script>", page)
			jsonDataFound = jsonData[0].replace("window._sharedData = ", "")

			private = re.findall(r"is_private\":(true|false)", page)
				
			values = json.loads(jsonDataFound)
			
			nbMedia = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']

			if nbMedia > 11:
				nbMedia = 11

			MediaDic = values['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
			countX = 0

			picturesList = {}

			if not private:
				while countX <= nbMedia:
					displayMedia = MediaDic[countX]['node']['display_url']
					legende = MediaDic[countX]['node']['edge_media_to_caption']['edges'][0]['node']['text']
					isVideo = MediaDic[countX]['node']['is_video']
					location = MediaDic[countX]['node']['location']
					timestamp = MediaDic[countX]['node']['taken_at_timestamp']
					date = time.ctime(timestamp)

					try:
						infoMedia = MediaDic[countX]['node']['accessibility_caption']
					except:
						infoMedia = ""

					if isVideo:
						typeMedia = "Video"
					else:
						typeMedia = "Photo"

					picturesList[timestamp] = {"domain":"Instagram", "urlMedia":displayMedia, "type":typeMedia, "legende":legende, "info":infoMedia, "location":location, "date":date, "timestamp":timestamp}

					countX += 1
			else:
				picturesList = {}

		self.medias = picturesList