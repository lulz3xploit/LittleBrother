from bs4 import BeautifulSoup
from terminaltables import SingleTable
import requests, re

def searchCopainsdavant(nom, city):
	url = "http://copainsdavant.linternaute.com/s/?ty=1&prenom=%s&nom=%s&nomjf=&annee=&anneeDelta=&ville=%s"
	name = nom
	if " " in name:
		nom = name.split(" ")[1]
		prenom = name.split(" ")[0]
	else:
		prenom = ""
		nom = name

	data = requests.get(url % (prenom, nom, city)).content.decode('utf-8')

	soup = BeautifulSoup(data, "html.parser")

	nameList = soup.find_all("div", {"class": "grid_last"})
	addresseList = soup.find_all("span", {"class": "app_list--result__search__place"})
	urlList = soup.find_all("h3")
	birthdayList = []
	travailList = []

	urlList2 = []

	for url in urlList:
		url = url.find("a")
		urls = str(url)
		href = re.search(r"/p/([a-zA-Z0-9_-]+)", urls).group()
		urlList2.append(href)

	for url in urlList2:
		data = requests.get("http://copainsdavant.linternaute.com/%s" % (url)).content.decode('utf-8')
		soup = BeautifulSoup(data, "html.parser")
		birthdayList0 = soup.find_all("abbr", {"class": "bday"})
		item = len(birthdayList0)
		if item == 0:
		 	birthdayList0.append("None")
	
		for b in birthdayList0:
			birthdayList.append(str(b))

		travailList0 = soup.find_all("p", {"class": "title"})
		item = len(travailList0)
		if item == 0:
		 	travailList0.append("None")
	
		for t in travailList0:
			travailList.append(str(t))

	namesList2 = []
	addressesList2 = []
	birthdayList2 = []
	travailList2 = []

	for name in nameList:
		name = name.find("a")
		namesList2.append(name.string)
	for addr in addresseList:
		addressesList2.append(addr.string.strip())
	for date in birthdayList:
		date = date.replace("<abbr class=\"bday\" title=\"", "").replace("00:00:00\">", "- ").replace("</abbr>", "").replace("\">", "")
		birthdayList2.append(date)
	for travail in travailList:
		travail = travail.replace("<p class=\"title\">", "").replace("</p>", "")
		travailList2.append(travail)

	regroup = zip(namesList2, addressesList2, birthdayList2, travailList2, urlList2)

	title = " Copain D'avant "

	TABLE_DATA = [
		('Name', 'Adresse', 'Date', 'Work', 'url'),
	]


	count = 0

	for info in regroup:
		count += 1
		name = info[0]
		adresse = info[1]
		adresse = adresse.split(" - ")[0]
		dateBirthday = info[2]
		try:
			dateBirthday = dateBirthday.split(" - ")[1]
		except:
			pass
		travail = info[3]
		url = info[4]

		infos = (name, adresse, dateBirthday, travail, url)

		TABLE_DATA.append(infos)

	if count > 0:
		table_instance = SingleTable(TABLE_DATA, title)
		print(table_instance.table)