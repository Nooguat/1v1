import requests
from bs4 import BeautifulSoup
from enum import Enum



class GenTypeUrl(Enum):
        NAME = 'https://www.generation-jdr.fr/index.php?page=nomsmodernes'
        NAME_RACE = 'https://www.generation-jdr.fr/index.php?page=nomevolue' 
        ITEMS = 'https://www.generation-jdr.fr/index.php?page=obm'
        


class Generator:
    """
    Virtual implementation of a Generator.
    Contains two simples methods : init 
    """
    def __init__(self, url, data=None):  
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

class GeneratorInit(Generator):
    def __init__(self, sexe):
        self.url = GenTypeUrl["NAME_RACE"]
        print(self.url)
        self.data = {}
        self.data['qtt'] = '1'
        self.data['race'] = '0'
        self.data['sexe'] = sexe

    def request(self, nbr):
        r = requests.post(
            self.url, data=self.data)
        soup = BeautifulSoup(r.text, features="html.parser")
        mydivs = soup.findAll("div", {"class": "articles"})
        names = str(mydivs).split("\n")[3].split('<br/>')
        for i in range(int(nbr_name)):
            print(names[i])
