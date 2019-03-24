import re, requests

class receiveSms:

	def searchServer(self):
		url = "https://www.receive-sms-online.info/"

		req = requests.get(url)
		page = req.content

		serverList = re.findall(r"<a href=\"([0-9]+)-([a-zA-Z0-9_]+)", page.decode('utf-8'))
		serverOnline = []

		n = 1

		for server in serverList:
			numero = server[0]
			country = server[1]
			tupleServer = (str(n), numero, country)
			serverOnline.append(tupleServer)
			# print("[%s] %s - +%s" % (str(n), country, numero))
			n = n + 1

		self.server_list = serverOnline
		self.url_of_site = url
	
	def sms(self, url):

		req = requests.get(url)
		page = req.content.decode('utf-8')
		fromUsersList = re.findall(r"data-label=\"From   :\">([a-zA-Z0-9_ +]+)</td>", page)
		messagesList = re.findall(r"data-label=\"Message:\">(.*)</td>", page)
		timeAgoList = re.findall(r"data-label=\"Added:\">(.*)</td>", page)

		regroup = zip(fromUsersList, messagesList, timeAgoList)

		self.contentMessages = regroup
		self.messageText = messagesList[1]
		self.fromUser = fromUsersList[0] 
		self.count = int(len(fromUsersList))