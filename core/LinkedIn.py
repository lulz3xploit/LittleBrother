import requests
from bs4 import BeautifulSoup

class searchLinkedIn:
	def __init__(self):
		server = "encrypted.google.com"
		limit = "100"        
		
		self.headers = {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    	    'referrer': 'https://google.com',
        	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        	'Accept-Encoding': 'utf-8',
        	'Accept-Language': 'en-US,en;q=0.9',
        	'Pragma': 'no-cache'
        }

		self.linkedin_list = ["| LinkedIn", "on LinkedIn", "- LinkedIn", "LinkedIn"]
		self.google_search = "https://"+server+"/search?num="+limit+"&q=%s %s insite:fr.linkedin.com/in"

	def search(self, searching, city):
		google_search = self.google_search % (searching, city)
		linkedin_list = self.linkedin_list

		employee_list = []
		pages_list = []

		req = requests.get(google_search, headers=self.headers)
		status_code = req.status_code

		if status_code == 200:
			html = BeautifulSoup(req.text, "html.parser")
			results = html.find_all('div', {'class': 'r' })

			for res in results:
				employee = res.find_all("h3", {"class":"LC20lb"})
				if employee:
					employee = employee[0].text.strip()
				
				if "LinkedIn" in employee:
					for l in linkedin_list:
						if l in employee:
							employee = employee.replace(l, "")
							employee_list.append(employee)

				page = res.find_all("cite", {'class':'iUh30'})
				for p in page:
					if "linkedin" in p.text.strip().lower():
						pages_list.append(p.text.strip().split("›")[1])

		if len(employee_list) > 0:
			found = len(employee_list)

		self.found = len(employee_list)
		self.employees = employee_list
		self.profiles = pages_list