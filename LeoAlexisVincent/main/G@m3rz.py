import csv
import random
import sys
import importlib
import os
#Gen = importlib.import_module("generateurs")
Dices = importlib.import_module("Des")

class Gamer:
    def __init__(self, vie):
        comp = ["feu", "glace", "air", "terre"] # Not yet implemented
        self.name, self.race = Gen.GeneratorInit()
        self.items = Gen.GeneratorItems
        self.pv = vie
        self.des = Dices.Des(1,3)
        
        # self.comp1 = comp[random.randint(0, 3)]
    # def get_comp(self):
    #     return self.comp1
    def get_pv(self):
        return self.pv
    def attack(self, file):

