import requests, bs4, terminatables
from bs4 import BeautifulSoup
from terminaltables import SingleTable

def skype_search(name):
    r = requests.get('https://www.skypli.com/search/'+urllib.parse.quote(name))
    soup = BeautifulSoup(r.text,"lxml")
    skype_name = []
    skype_username = []
    profiles = soup.find_all("div",{"class":"search-results__block"})
    for i in profiles: 
        username = i.find("span",{"class":"search-results__block-info-username"}).getText()
        name_sk  = i.find("span",{"class":"search-results__block-info-fullname"}).getText()
        skype_name.append(name_sk)
        skype_username.append(username)
    regroup = zip(skype_name,skype_username)
    TITLE      = (' Skype ')
    TABLE_DATA = [('Full Name','Username')]
    table      =    SingleTable(TABLE_DATA, title=TITLE)
    for infos in regroup:
        try:
            TABLE_DATA.append(infos)
        except AttributeError:
            pass
    print(table.table)
