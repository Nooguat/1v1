import importlib
import os
from random import randint
#Gamer = importlib.import_module("Gameur")
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
        token = hex(randint(255,1024))
        player = Gamer.Gamer()
        while player.get_life >= 0:
            
            pass
        os.remove('game')
    except FileNotFoundError:
        print("Création de la partie, en attente de joueurs...")
        # token = hex(randint(255,1024)) #TODO Login system
        # print("Demandez à vos amis d'entrer ce token pour arriver dans la partie" + str(token))
        open("game", 'w+')