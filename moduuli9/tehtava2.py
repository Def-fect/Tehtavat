class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kiihdytä, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kiihdytä = kiihdytä
        self.kuljettu_matka = kuljettu_matka

    def kiiht(self):
        self.kiihdytä += 30
        self.kiihdytä += 70
        self.kiihdytä += 50
        if self.kiihdytä > 142:
            self.kiihdytä = 142

    def jarr(self):
        self.kiihdytä -=200
        if self.kiihdytä < 0:
            self.kiihdytä = 0






auto = Auto("ABC-123", 142, 0, 0)
auto.kiiht()
print(f"{auto.rekisteritunnus} ja {auto.huippunopeus} km/h ja {auto.kiihdytä}km/h ja {auto.kuljettu_matka}km")

auto.jarr()
print(f"{auto.rekisteritunnus} ja {auto.huippunopeus} km/h ja {auto.kiihdytä}km/h ja {auto.kuljettu_matka}km")