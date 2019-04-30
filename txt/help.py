helpMain = """
	Name                    Action
	----                    ------
	set <name> <value>      Ajouter une valeur.
	show option             Voir les valeurs inscrit.
	show country            Voir quel pays disponible pour l'utilisation des services.
	show info				Afficher les résultats obtenu suite à une recherche éfféctué.
	more option             Voir des options supplémentaire.
	coutry <name>           Selectionner un pays via son CODE.
	exit                    Quitter le logiciel.
	help                    Affiche se message.
	clear                   Efface l'ecran.
"""

helpCountry = """
	Name        Action
	----        ------
	FR          Utiliser les services Francais.
	BE          Utiliser les services Belge.
	CH          Utiliser les services Suisse.
	LU          Utiliser les services Luxembourgeois.
	XX          Utiliser tout les services.
"""

moreOption = """
 Vous pouvez utiliser le symbole '~' devant une valeur (nom, prenom, localisation...) 
 si la syntaxe de celle ci peut etre différente.
 
 Ex:
 | set nom ~Zuckerberg
 | [!] Not found 'Zuckerberg' in Twitter.
 | [+] Twitter name found: Suckerberg

 Ceci peut être utile si jamais la valeur donnée n'a pas été trouvé et que vous aimerez avoir un resultat ressemblant.
 Ou si vous n'êtes pas certain de l'orthographe de cette valeur. 

 L'absence de se symbole aura pour effet de récupérer le resultat seulement si l'orthographe est identique à la valeur, sinon ne rien récupérer.
"""