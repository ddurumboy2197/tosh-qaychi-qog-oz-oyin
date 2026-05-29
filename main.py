import random

class Toshqaychi:
    def __init__(self):
        self.sanalar = [1, 2, 3, 4, 5, 6]

    def qaychi(self):
        return random.choice(self.sanalar)

class Qogoz:
    def __init__(self):
        self.sanalar = [1, 2, 3, 4, 5, 6]

    def qogoz(self):
        return random.choice(self.sanalar)

class Oyni:
    def __init__(self):
        self.toshqaychi = Toshqaychi()
        self.qogoz = Qogoz()
        self.kompyuter_punkt = 0
        self.bosh_punkt = 0

    def oyna(self):
        while True:
            print(f"Kompyuterning qaychi: {self.toshqaychi.qaychi()}")
            print(f"Sizning qaychi: {self.qogoz.qogoz()}")
            if self.toshqaychi.qaychi() > self.qogoz.qogoz():
                self.kompyuter_punkt += 1
                print(f"Kompyuterning punkti: {self.kompyuter_punkt}")
            elif self.toshqaychi.qaychi() < self.qogoz.qogoz():
                self.bosh_punkt += 1
                print(f"Sizning punkti: {self.bosh_punkt}")
            else:
                print("Durrang!")
            javob = input("Qaychi qilishni xohlaysizmi? (ha/yoq): ")
            if javob.lower() != "ha":
                break
        if self.kompyuter_punkt > self.bosh_punkt:
            print("Kompyuter yutdi!")
        elif self.kompyuter_punkt < self.bosh_punkt:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")

oyna = Oyni()
oyna.oyna()
