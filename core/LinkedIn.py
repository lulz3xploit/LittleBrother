import requests
from bs4 import BeautifulSoup

class searchLinkedIn:
	def __init__(self):
		server = "encrypted.google.com"
		limit = "100"

		self.linkedin_list = ["| LinkedIn", "on LinkedIn", "- LinkedIn", "LinkedIn"]
		self.google_search = "https://"+server+"/search?num="+limit+"&q=%s %s insite:fr.linkedin.com/in"

	def search(self, searching, city):
		google_search = self.google_search % (searching, city)
		linkedin_list = self.linkedin_list

		employee_list = []
		profile_list = []

		req = requests.get(google_search)
		status_code = req.status_code

		if status_code == 200:
			html = BeautifulSoup(req.text, "html.parser")
			results = html.find_all('div', { 'class' : 'g' })

			for res in results:
				employee = res.find('h3', { 'class' : 'r' }).text

				if "LinkedIn" in employee:
					for l in linkedin_list:
						if l in employee:
							employee = employee.replace(l, "")
							employee_list.append(employee)
					
					profile = res.find('cite').text
					profileSplit = profile.split("/")
					profile = "/in/"+profileSplit[len(profileSplit) -1]
					profile_list.append(profile)

				if len(employee_list) > 0:
					found = len(employee_list)
					employees = employee_list
					profiles = profile_list


		self.found = len(employee_list)
		self.employees = employee_list
		self.profiles = profile_list