import requests
from bs4 import BeautifulSoup
from terminaltables import SingleTable

def searchLocalCH(url):
	data = requests.get(url).content.decode("utf-8")

	soup = BeautifulSoup(data, "html.parser") 

	nameList = soup.find_all("span", {"class": "listing-title"})
	adresseList = soup.find_all("div", {"class": "listing-address small"})
	phoneList = soup.find_all("a", {"class": "btn btn-sm listing-contact-phone lui-margin-right-xs number phone-number"})

	nameList2 = []
	adresseList2 = []
	phoneList2 = []

	for name in nameList:
		nameList2.append(name.string.strip())

	for adress in adresseList:
		adresseList2.append(adress.string.strip())

	for phone in phoneList:
		phoneList2.append(phone.getText().replace("*", "").strip())

	regroup = zip(nameList2,adresseList2, phoneList2)

	TABLE_DATA = [
		("Name", "Adresse", "Telephone"),
	]

	for r in regroup:
		TABLE_DATA.append(r)

	table = SingleTable(TABLE_DATA, title="Yellow")
	print(table.table)