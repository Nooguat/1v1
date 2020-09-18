import importlib
import os
from random import randint
#Gamer = importlib.import_module("Gameur")
Utils = importlib.import_module("Utils")
"""
Some of the code is used from Gameur.py made by Léo Gautier and Vincent Maccaeli
under their strict authorization.
"""
try:
    pass
    #t = Gamer.Gamer(-1) # Mock Gamer verifing if modules are well initiated
except:
    print("des modules nécéssaires ne sont pas installés. Installation en cours...")
    os.system("py -m pip install bs4 --user")
    os.system("py -m pip install requests --user")
    os.system("py -m pip install importlib --user")
    print("modules installés")
    # importlib.reload("Gameur")
if __name__ == "__main__":
    try :
        file = open("game")
        file.read()
        file.close()
        print("Partie rejointe, merci de patienter...")
        token = str(hex(randint(255,1024)))
        player = Gamer.Gamer()
        while player.get_life >= 0:
            if Utils.FileExists("open") == False:
                print("Vous avez gagné ! ")
                exit(0)
            Utils.GameFileWrite(token)
            pass
        os.remove('game')
    except FileNotFoundError:
        print("Création de la partie, en attente de joueurs...")
        # token = hex(randint(255,1024)) #TODO Login system
        # print("Demandez à vos amis d'entrer ce token pour arriver dans la partie" + str(token))
        open("game", 'w+')