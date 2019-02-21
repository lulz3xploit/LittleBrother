LittleBrother
=

LittleBrother est un outil de collecte d'informations (OSINT) qui vise à éffectuer des recherches sur une personne française, suisse, luxembourgeois ou belge. Il fournit divers modules qui permettent des recherches éfficaces. LittleBrother ne requiert pas de clé API ni d'identifiant de connexion.

![](https://i.ibb.co/YdvfVPw/Capture.png)

Disclaimer
=
LittleBrother a été développé pour faire des recherches sur sois même et pour voir les informations privées et sensible qu'ont peux laisser derrière sois à cause des réseaux sociaux. Je n'encourage en aucun cas d'utiliser cet outil sur une autre personnes que sois même ou d'utiliser cet outil à mauvais escient.

Nouveautées version 6.0
=
- Choses en plus (+)
	- Un fichier 'requirements.txt' a été ajouté dans cette version
	- Une nouvelle interface.
	- Un nouveau module d'OSINT a été ajouté dans cette version, le module 'Profiler' remplace la base de donnée et de 'Dox maker' dans la version anterieur de LittleBrother. Ce module permet de créer un profil et de récupérer des informations sur les sites défini par l'utilisateur, de sauvegarder ces données et d'afficher les derniers post publié sur les réseaux (filtré selon les dates de publication).
	- De nouveau service de recherche (Annuaire) ont été ajouté selon la localisation de l'utilisateur. LittleBrother utilise votre IP pour déterminer le pays dans le quel vous vous trouvez. En aucun cas votre IP ou autre information privée sera partagé. Vous pourrez choisir un autre pays que le votre pour centraliser vos recherche.
	- Recherche Instagram et LinkedIn intégré à 'Personne Lookup'.
	- Un nouveau module de recherche 'Employés recherche' qui permet de faire des recherches de personne via une entreprise et une ville.
	- Le module de recherche d'information Instagram et Facebook ont été amélioré pour extraire plus d'information.  

- Choses en moin (-)
	- Certaines librairies python (dnspython, socket et smtplib) ont été supprimer pour cette version.
	- 'Social engineering tool' à été modifier pour 'Other tool' il ne comporte que le module de brute force d'un Hash.
	- Les modules 'Spam Email' et 'SMS' ont été retiré de LittleBrother.
	- Le module de création de Dox 'Dox maker' a été retiré de LittleBrother.


Compatible
=
- Windows
- MacOS
- Linux

Python version:
=
- Python3

Python Modules
=
- requests
- bs4 
- terminaltables
- colorama


Installation
=
    git clone https://github.com/Lulz3xploit/LittleBrother
    cd LittleBrother
    python -m pip install -r requirements.txt
    python littlebrother.py


Features 
=
 - Lookup:

	- Phone lookup
	- Email lookup
	- Last name / First name lookup
	- Surname lookup
	- Addresse lookup
	- Mail ip locator
	- Ip locator
	- Bssid locator
	- Exif read
	- Twitter
	- Instagram
	- Facebook

 - Autre outils:
 
	- Hash Bruteforce

