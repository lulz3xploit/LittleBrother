import requests, re

def searchGoogle(requete='', requete2=''):

	# encodeList = [
	# 	"%21","%23","%24","%26","%27","%28","%29","%2A","%2B","%2C","%2F","%3A","%3B","%3D","%3F","%40","%5B","%5D",
	# 	"%20","%22","%25","%2D","%2E","%3C","%3E","%5C","%5E","%5F","%60","%7B","%7C","%7D","%7E"
	# ]

	encodeDic = {
		"%21": "!",
		"%23": "#",
		"%24": "$",
		"%26": "&",
		"%27": "'",
		"%28": "(",
		"%29": ")",
		"%2A": "*",
		"%2B": "+",
		"%2C": ",",
		"%2F": "/",
		"%3A": ":",
		"%3B": ";",
		"%3D": "=",
		"%3F": "?",
		"%40": "@",
		"%5B": "[",
		"%5D": "]", 
		"%20": " ",
		"%22": "\"",
		"%25": "%",
		"%2D": "-",
		"%2E": ".",
		"%3C": "<",
		"%3E": ">",
		"%5C": "\\",
		"%5E": "^",
		"%5F": "_",
		"%60": "`",
		"%7B": "{",
		"%7C": "|",
		"%7D": "}",
		"%7E": "~",
	}

	if requete2 != '':
		content = requete2.text #.content.decode('utf-8')
		urls = re.findall('url\\?q=(.*?)&', content)
		for url in urls:
			for char in encodeDic:
				find = re.search(char, url)
				if find:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
			if not "googleusercontent" in url:
				if not "/settings/ads" in url:
					if not "/policies/faq" in url:
					# if "insta" in url or "twitter" in url or "facebook" in url:
						print("[++] Possible connection: "+url)
	else:
		pass

	content = requete.text
	urls = re.findall('url\\?q=(.*?)&', content)
	for url in urls:
		for char in encodeDic:
			find = re.search(char, url)
			if find:
				charDecode = encodeDic.get(char)
				url = url.replace(char, charDecode)
		if not "googleusercontent" in url:
			if not "/settings/ads" in url:
				if not "/policies/faq" in url:
				# if "insta" in url or "twitter" in url or "facebook" in url:
					print("[+] Possible connection: "+url)