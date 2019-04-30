class GuessUsername:

	def __init__(self, name):
		self.name = name

	def usernamesGuessed(self):
		name = self.name
		usernameGuessed = ''
		list_usernameGuessed = []
		vowel = list("aeiou")
		otherLetter = list("lmnr")

		# usernameGuessed:		Nom dépourvu de voyelle. (sauf si premier caractere)
		# usernameGuessed_2:	usernameGuessed avec une voyelle à la fin si le nom en comporte une.
		# usernameGuessed_3:	Première 'Syllabe' du nom.
		# usernameGuessed_4:	usernameGuessed2 dépourvu de lettre successive.
		# usernameGuessed_5:	usernameGuessed dépourvu de 'L, M, N, R'
		# usernameGuessed_6:	usernameGuessed_2 dépourvu de 'L, M, N, R'

		# Si le nom comporte 6 caractères ou moin, il peut être considéré comme un pseudo, ou en faire partie
		if len(name) <= 6:
			list_usernameGuessed.append(name)

		# Récupère la première lettre du nom si celle ci et une voyelle
		startsLetter = [l for l in vowel if name.startswith(l)]
		# Récupère la dernière lettre du nom si celle ci et une voyelle
		endsLetter = [l for l in vowel if name.endswith(l)]
		
		# Si le nom commence par une voyelle, on l'incremente dans 'usernameGuessed' (à la première position)
		if startsLetter:
			usernameGuessed += startsLetter[0]

		# Enlève toute les voyelles du nom
		usernameUnvoweled = [world for world in name if world not in vowel]
		usernameGuessed += ''.join(usernameUnvoweled)

		list_usernameGuessed.append(usernameGuessed)
		
		usernameGuessed_2 = usernameGuessed
		
		# Si le nom fini par une voyelle, on rajoute celle ci a la fin de 'usernameGuessed_2'
		if endsLetter:
			usernameGuessed_2 += endsLetter[0]

		list_usernameGuessed.append(usernameGuessed_2)

		# Récupérer les 2 premiers caractères du nom
		usernameGuessed_3 = name[:2]

		# Récupérer tout les voyelles contenu dans le nom (sauf les 2 premiers cacarctères)
		lastVowel = [l for l in name[2:] if l in vowel]

		# Si le nom comporte des autres voyelles
		if lastVowel:
			for letter in name[2:]:
				# Si la lettre du nom testé et égal à la première voyelle récupéré
				if letter == lastVowel[0]:
					# Et si le dernier caractère de 'usernameGuessed_3' est une voyelle
					if usernameGuessed_3[-1] in vowel:
						# On incrémente la lettre à 'usernameGuessed_3'
						usernameGuessed_3 += letter
					# Sortir de la boucle si la lettre du nom testé et égal a la première voyelle récupéré
					break

				else:
					usernameGuessed_3 += letter

		list_usernameGuessed.append(usernameGuessed_3)

		usernameGuessed_4 = usernameGuessed_2

		# Supprimer les lettres succesive dans le nom
		cleanUsername= ''
		for letter in usernameGuessed_4:
			if cleanUsername == '' or letter != cleanUsername[-1]:
				cleanUsername += letter

		usernameGuessed_4 = cleanUsername
		list_usernameGuessed.append(usernameGuessed_4)

		# Supprimer les 'R, L, M, N' contenu dans 'usernameGuessed'
		usernameGuessed_5 = [world for world in usernameGuessed[1:-1] if not world in otherLetter]
		usernameGuessed_5 = usernameGuessed[0] + ''.join(usernameGuessed_5) + usernameGuessed[-1] 
		list_usernameGuessed.append(usernameGuessed_5)

		# Supprimer les 'R, L, M, N' contenu dans 'usernameGuessed_2'
		usernameGuessed_6 = [world for world in usernameGuessed_2[1:-1] if not world in otherLetter]
		usernameGuessed_6 = usernameGuessed_2[0] + ''.join(usernameGuessed_6) 
		list_usernameGuessed.append(usernameGuessed_6)
	
		# Supprimer les doublons dans la liste des noms d'utilisateurs généré
		list_usernameGuessed_2 = []
		for username in list_usernameGuessed:
			if not username in list_usernameGuessed_2:
				list_usernameGuessed_2.append(username)

		return(list_usernameGuessed_2)

u = GuessUsername("dupont")
print(u.usernamesGuessed())
