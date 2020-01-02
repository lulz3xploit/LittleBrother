# -*- coding: utf-8 -*-
import re

class Url:
	def __init__(self, url):
		self.url = url
		self.encodeDic = {
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

	def decode(self):
		encodeDic = self.encodeDic
		url = self.url
		
		while '%' in url:
			for char in encodeDic:
				if char in url:
					charDecode = encodeDic.get(char)
					url = url.replace(char, charDecode)
		return(url)

	def encode(self):
		encodeDic = self.encodeDic
		url = self.url
		not_char = ".%:/"

		for char in encodeDic.values():
			if not char in not_char:
				charEncode = [key for key, value in encodeDic.items() if value == char][0]
				if char in url:
					url = url.replace(char, charEncode)

		return(url)