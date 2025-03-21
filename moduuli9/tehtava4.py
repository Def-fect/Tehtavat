import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kiihdytä, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kiihdytä = kiihdytä
        self.kuljettu_matka = kuljettu_matka


    #laitetaan ensin huippunopeus
    def randhuip(self):
        self.huippunopeus = random.randint(100,200)

    def kiiht(self):
        self.kiihdytä = random.randint(-10, 15)
        if self.kiihdytä > self.huippunopeus:
            self.kiihdytä = self.huippunopeus
        return



    def kulje(self, tunti):
        self.kiihdytä == autot.kiiht()
        valimatka= self.kiihdytä * tunti
        self.kuljettu_matka += valimatka




autot = []

for i in range(10):
    i+=1
    randhuip = random.randint(100, 200)
    randnope = random.randint(-10, 15)
    autot.append(Auto(f"ABC-{i}", randhuip, randnope, 0))




for auto in autot:
    print(f"{autot.rekisteritunnus} {auto.kiihdytä}")
print(autot)

#toimiva
autot.sort(key=lambda a: a.matka, reverse=True)
for auto in autot:
    print()

