import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self):
        self.nopeus += random.randint(-10, 15)
        self.matka += self.nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti


class Kilpailu:
    def __init__(self, kilpnimi, kmpit, autolista):
        self.kilpnimi = kilpnimi
        self.kmpit = kmpit
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            auto.kiihdyta()
            auto.kulje(1)

    def tulosta_tilanne(self):
        autot.sort(key=lambda a: a.matka, reverse=True)
        for auto in autot:
            print(f"{auto.rekisteritunnus} {auto.huippunopeus} {auto.nopeus} {auto.matka}")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.kmpit:
                for auto in autot:
                    print(f"{auto.rekisteritunnus} {auto.huippunopeus} {auto.nopeus} {auto.matka}")


autot = []

for i in range(10):
    i += 1
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:

        auto.kiihdyta()

        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_kaynnissa = False
            break

autot.sort(key=lambda a: a.matka, reverse=True)
for auto in autot:
    print(f"{auto.rekisteritunnus} {auto.huippunopeus} {auto.nopeus} {auto.matka}")
