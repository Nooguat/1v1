import csv
import random
import sys
import 
from main.generateur_nom import Generator

class Personnage:
    def __init__(self, vie):
        comp = ["feu", "glace", "air", "terre"]
        self.name = Generator()
        self.pv = vie
        self.comp1 = comp[random.randint(0, 3)]
    def get_comp(self):
        return self.comp1
    def get_pv(self):
        return self.pv

Test = Personnage(random.randint(15,20))
pv = Test.get_pv()

fd = open("dmg.csv", "w")
fd.write("0")
fd.close()


d4 = 3
d8 = 1


while True :

    f = open('test.csv','r')
    tour = f.read()
    f.close()



    if tour == "1" :
        fd = open("dmg.csv", "r")
        dtaken = int(fd.read())
        fd.close()

        pv = pv - dtaken
        print("Il vous reste " + str(pv))
        if pv <= 0 :
            print("Game Over")
            break


        inp = int(input("1 -> 1d2, 2 -> 1d4, 3 -> 1d8"))

        if inp == 1 :
            print("vous avez utilisé 1d2 !, il vous en reste une infinité !")
            dmg = random.randint(1,2)
            print("Vous avez infligé " + str(dmg))
            f1 = open("dmg.csv", "w")
            f1.write(str(dmg))
            f1.close()

        elif inp == 2 :
            d4 = d4 - 1
            print("vous avez utilisé 1d4 !, il vous en reste " + str(d4))
            dmg = random.randint(1,4)
            print("Vous avez infligé " + str(dmg))
            f2 = open("dmg.csv", "w")
            f2.write(str(dmg))
            f2.close()
        else :
            d8 = d8 - 1
            print("vous avez utilisé 1d8 !, vous n'en avez plus !")
            dmg = random.randint(0,9)
            if dmg == 0 :
                print("Echec critique ! vous perdez 3 pv !")
                pv = pv - 3
            elif dmg == 9 :
                print("Succès critique ! vous gagnez 1d8 !")
                d8 = d8 +1
                f9 = open("dmg.csv", "w")
                f9.write(str(dmg))
                f9.close()
            else :
                print("vous avez infligé " + str(dmg))
                f3 = open("dmg.csv", "w")
                f3.write(str(dmg))
                f3.close()


        fi = open('test.csv','w')
        fi.write('2')
        fi.close()










