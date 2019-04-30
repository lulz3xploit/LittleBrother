import settings
from terminaltables import SingleTable

def printInfo():
	dict_info = settings.personneInfo

	TABLE_DATA = [
	]

	for key in dict_info:
		info   = key.replace("_", " ")
		info   = info.capitalize()
		value = dict_info[key].capitalize()
		if value != '':
			TABLE_DATA.append([info, value])

	table = SingleTable(TABLE_DATA)
	table.inner_heading_row_border = False
	table.inner_row_border = True
	table.justify_columns = {0: 'left', 1: 'center'}

	print(table.table)