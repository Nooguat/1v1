import importlib
#Gamer = importlib.import_module("Gameur")
try:
    t = Gamer.Gamer(-1) # Mock Gamer verifing if modules are well charged
except:
    print("des modules nécéssaires ne sont pas installés. Installation en cours...")
    os.system("py -m pip install bs4 --user")
    os.system("py -m pip install requests --user")
    os.system("py -m pip install importlib --user")
    print("modules installés")
    # importlib.reload("Gameur")
if __name__ == "__main__":
    if i:= input("Joueur 1 ou Joueur 2 ?") == "Joueur 1":
        #Gamer.Gamer(1)
    else if i:= input("Joueur 1 ou Joueur 2 ?") == "Joueur 2":
        #Gamer.Gamer(2)
    else:
        print("Input non pris en charge. Fin de l'execution...")
        exit(0)