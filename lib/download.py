import requests

def download(url, path, filename):
	r = requests.get(url)
	f = open(path+filename,'wb');

	for chunk in r.iter_content(chunk_size=255): 
		if chunk:
			f.write(chunk)

	f.close()