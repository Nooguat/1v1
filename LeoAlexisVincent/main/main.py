import importlib
import os
from random import randint
#Gamer = importlib.import_module("Gameur")
try:
    t = Gamer.Gamer(-1) # Mock Gamer verifing if modules are well initiated
except:
    print("des modules nécéssaires ne sont pas installés. Installation en cours...")
    os.system("py -m pip install bs4 --user")
    os.system("py -m pip install requests --user")
    os.system("py -m pip install importlib --user")
    print("modules installés")
    # importlib.reload("Gameur")
if __name__ == "__main__":
    if file:=open("game"):
        file.read()
        print("Partie rejointe, merci de patienter...")
    else:
        print("Création de la partie, en attente de joueurs...")
        token = hex(radint(255,1024))
        print(token)
        i = input("Souhaitez vous rendre cette partie privée ? (pas d'input si non)")
        if i == '':
            open("game", 'w+')