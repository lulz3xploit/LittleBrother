def delAccent(chaine):
	accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
	sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
	
	chaine = chaine.upper()

	for i in range(0, len(accent)):
	    chaine = chaine.replace(accent[i].upper(), sans_accent[i].upper())
	 
	return(chaine.capitalize())