import requests
import json

class searchInfoNumero:

	def search(self, num):
		location = {
			"01": "Ile de France.",
			"02": "Nord-Ouest de la France.",
			"03": "Nord-Est de la France.",
			"04": "Sud-Est de la France.",
			"05": "Sud-Ouest de la France."
		}

		num = num.replace(" ","").replace("+33", "0")
		pfx = num[0:2]

		url = 'https://www.infos-numero.com/ajax/NumberInfo?num='
		page = requests.get(url+num).text
		data = json.loads(page)['info']

		self.phone_type = data['type_lang']['en']
		self.location = location.get(pfx)
		self.city = data['ville']
		self.operator = data['carrier']