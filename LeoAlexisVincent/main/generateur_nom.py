import requests
from bs4 import BeautifulSoup
from enum import Enum

class GenTypeUrl(Enum):
        NAME = 'https://www.generation-jdr.fr/index.php?page=nomsmodernes'
        


class Generator:
    def __init__(self, data, url):  
        self.data = data
        self.url = url
    def request(self, nbr):
        r = requests.post(
            self.url, data=self.data)
        soup = BeautifulSoup(r.text, features="html.parser")
        mydivs = soup.findAll("div", {"class": "articles"})
        names = str(mydivs).split("\n")[3].split('<br/>')
        for i in range(int(nbr_name)):
            print(names[i])


nbr_name = input("Nombre de noms a generer :")
Generator(data = {
        'sexe':	"2",
        'ethnie':	"0",
        'nbr':	nbr_name
    }, url='https://www.generation-jdr.fr/index.php?page=nomsmodernes')
