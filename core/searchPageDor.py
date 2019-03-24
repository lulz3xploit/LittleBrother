from bs4 import BeautifulSoup
from core.searchInfoNumero import searchInfoNumero
from terminaltables import SingleTable


def searchPageDor(requete='', num=''):
	def testResponse(requete):
		if 'Aucun résultat' in requete.text:
			return 1
			# print("[!] Aucun resultattttt pour votre recherche... o_o' ")

	page = requete.text #content.decode('utf-8')
	soup = BeautifulSoup(page, "html.parser")
	rep = testResponse(requete)
	if rep == 1:
		print(warning+" Aucun résultat pour votre recherche... o_o'")
		if num != '':
			# phoneNumber(num)
			pass
		else:
			pass
	else:
		pass

	try:
		nameList = soup.find_all("h2", {"class": "result-item-title"})
		# print(nameList)
		addressList = soup.find_all("li", {"class": "address"})
		# print(addressList)
		numList = soup.find_all("li", {"class": "phone"})
		# input(numList)
		# name = name.string.strip()
		# adresse = adresse.string.strip()
		# num = num.string.strip()
		# printResult(name, adresse, num)
	except AttributeError:
		pass

	namesList2 = []
	addressesList2 = []
	numesList2 = []
	operatorList = []

	# try:
	for name in nameList:
		namesList2.append(name.text.strip())
	for addresse in addressList:
		addressesList2.append(addresse.text.strip())
	for num in numList:
		phone = searchInfoNumero()
		phone.search(num.text.strip())
		operator = phone.operator
		operatorList.append(operator) 
		numesList2.append(num.text.strip())
	# except:
	# 	pass
	# 	print("[!] Aucun resultat pour votre recherche... o_o'")

	regroup = zip(namesList2,addressesList2,numesList2, operatorList)
	
	title = " Particulier "

	TABLE_DATA = [
		('Name', 'Adresse', 'Phone', 'Operateur'),
	]

	listeInfos = []

	for infos in regroup:
		
		try:

			TABLE_DATA.append(infos)

		except AttributeError:
			pass

	if rep != 1:
		table_instance = SingleTable(TABLE_DATA, title)
		print("\n"+table_instance.table)