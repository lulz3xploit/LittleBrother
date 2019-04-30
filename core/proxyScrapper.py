import re, requests

def scrappProxy():
	list_proxy = []

	req = requests.get("https://free-proxy-list.net")
	page = req.text
	info = re.findall(r"<td>([0-9\.]+)</td><td>([0-9]+)</td><td>([A-Z]+)</td><td class='hm'>([a-zA-Z_ - ]+)</td><td>([a-zA-Z_ ]+)</td><td class='hm'>([a-z]+)</td><td class='hx'>([a-z]+)</td><td class='hm'>", page)

	for proxy in info:
		types = proxy[4]

		if 'elite' in types:
			ip 	 = proxy[0]
			port = proxy[1]

			url = "http://"+ip+':'+port

			list_proxy.append(url)

	return(list_proxy)

proxyList = scrappProxy()