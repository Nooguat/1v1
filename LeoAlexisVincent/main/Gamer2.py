import csv
import random


class Personnage:
    def __init__(self, vie):
        comp = ["feu", "glace", "air", "terre"]

        self.pv = vie
        self.comp1 = comp[random.randint(0, 3)]
    def get_comp(self):
        return self.comp1
    def get_pv(self):
        return self.pv


Test = Personnage(random.randint(15,20))
element = Test.get_comp()
print(element)
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






    if tour == "2" :
        fd = open("dmg.csv", "r")
        dtaken = int(fd.read())
        fd.close()
        pv = pv - dtaken
        print("Il vous reste " + str(pv))
        if pv <= 0 :
            print("VOUS ETES MORT !")
            break



        inp = int(input("1 -> 1d2, 2 -> 1d4, 3 -> 1d8"))


        if inp == 1 :
        #faire les dégats et les écires dans un nouveau csv
            print("Vous avez utilisé 1D2. Il vous en reste une infinité")
            dmg = random.randint(1,2)
            print("Vous avez infilgé " + str(dmg))
            f1 = open("dmg.csv","w")
            f1.write(str(dmg))
            f1.close()


        elif inp == 2 :
            d4 = d4-1
            print("Vous avez utilisé un 1D4. Il vous en reste "+ str(d4))
            dmg = random.randint(1,4)
            print("Vous avez infligé "+ str(dmg))
            f2 = open("dmg.csv","w")
            f2.write(str(dmg))
            f2.close()

        else :
            d8 = d8-1
            print("Vous avez utilisé un 1D8. Il vous en reste "+ str(d8))
            dmg = random.randint(0,9)

            if dmg == 0 :
                print("ECHEC CRITIQUE ! Vous perdez 3 PV")
                pv = pv - 3

            elif dmg == 9 :
                print("SUCCES CRITIQUE ! Vous gagnez 1D8")
                d8 = d8 +1
                f9 = open("dmg.csv", "w")
                f9.write()
                f9.close()

            else :
                print("Vous avez infligé "+ str(dmg))
                f3 = open("dmg.csv","w")
                f3.write(str(dmg))
                f3.close()



        fi = open('test.csv','w')
        fi.write('1')
        fi.close()





