class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiiht(self):
        self.nopeus += 30
        self.nopeus += 70
        self.nopeus += 50
        if self.nopeus > 142:
            self.nopeus = 142

    def jarr(self):
        self.nopeus -=200
        if self.nopeus < 0:
            self.nopeus = 0



    def kulje(self, tunti):
        self.nopeus += 60
        valimatka= self.nopeus * tunti
        self.kuljettu_matka += valimatka








auto = Auto("ABC-123", 142, 0, 2000)

auto.kulje(1.5)
print(f"{auto.rekisteritunnus} ja {auto.huippunopeus} km/h ja {auto.nopeus}km/h ja {auto.kuljettu_matka}km")
