from random import randint
class Des():
    def __init__(self, n_d8, n_d4):
        self.dice_type = ["d8", "d4", "d2"]
        self.d4 = n_d4
        self.d8 = n_d8
    
    def ThrowDice(d_type) -> int:
        if d_type = self.dice_type[0]:
            if self.d8 == 0:
                print("Vous auriez dû vous souvenir que vous aviez utilisé votre dernier d8. Dommage ! ")
                return 0
            self.d8 -= self.d8
            return randint(1,8)
        if d_type = self.dice_type[1]:
            if self.d4 == 0:
                print("Vous auriez dû vous souvenir que vous aviez utilisé votre dernier d4. Dommage ! ")
                return 0
            self.d4 -= self.d4
            return randint(1,4)
        print("Vous avez utilisé un d2, et ca tombe bien, on en a plein ! ")
        return randint(1,2)
        
