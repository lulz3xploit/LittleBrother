import requests
from bs4 import BeautifulSoup
from terminaltables import SingleTable

def searchYellowLU(url):
	data = requests.get(url).content.decode("utf-8")

	soup = BeautifulSoup(data, "html.parser") 

	nameList = soup.find_all("h3", {"class": "search-result-title"})
	adresseList = soup.find_all("span", {"class": "street-address"})
	regionList = soup.find_all("span", {"class": "region"})
	phoneList = soup.find_all("span", {"class": "number contact-list_info"})

	nameList2 = []
	adresseList2 = []
	regionList2 = []
	phoneList2 = []

	for name in nameList:
		nameList2.append(name.getText())

	for adress in adresseList:
		adresseList2.append(adress.string)

	for region in regionList:
		regionList2.append(region.string)

	for phone in phoneList:
		phoneList2.append(phone.string)

	regroup = zip(nameList2,adresseList2, regionList2, phoneList2)

	TABLE_DATA = [
		("Name", "Adresse", "Region", "Telephone"),
	]

	for r in regroup:
		TABLE_DATA.append(r)

	table = SingleTable(TABLE_DATA, title="Yellow")
	print(table.table)