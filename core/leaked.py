import requests, json, re
from core.getUrlGoogleSearch import getUrlGoogleSearch

class leaked:

	def hash(self, hash):
		text = requests.get("https://hashtoolkit.com/reverse-hash/?hash="+hash).text
		passw = re.findall(r"/generate-hash/\?text=(.*?)\"", text)

		if len(passw) != 0:
			passw = passw[0]
		else:
			passw = None

		return(passw)

	def email(self, email):
		dataList = []

		try:
			req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/"+email, headers={"Content-Type":"application/json", "Accept":"application/json", "User-Agent":"LittleBr0ther"})
			print(req.status_code)
			if req.status_code == 200:
				data = json.loads(req.text)
				for d in data:
					name = d['Title']
					domain = d['Domain']
					date = d['BreachDate']
					dataDic = {'Title':name, 'Domain':domain, 'Date':date}
					dataList.append(dataDic)

				return(dataList)

		except:
			return(None)

	def password(self, password):
		encodeDic = self.encodeDic
		list_dataFound = []
		list_pastebinUrl = []
		req = requests.get("https://encrypted.google.com/search?num=100&q=site:pastebin.com intext:%s" % (password))
		content = req.text
		urls = getUrlGoogleSearch(content)

		for url in urls:
			if "pastebin.com" in url:
				list_pastebinUrl.append(url)

		nbUrl = len(list_pastebinUrl)
		print(nbUrl)

		for url in list_pastebinUrl:
			req = requests.get(url)
			content = req.text

			dataFound = re.findall(r"(([a-zA-Z0-9 _ - \.]+@[a-zA-Z0-9 _ - \.]+)(:|\|))"+password, content)
			
			for data in dataFound:
				data = data[0].strip()
				data = data.replace(":", "")
				data = data.replace("|", "")
				if not data in list_dataFound and not ' ' in data:
					list_dataFound.append(data)

		return(list_dataFound)