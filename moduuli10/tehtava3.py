import time


class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = 0

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"kerros {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"kerros {self.kerros}")

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros < kohdekerros:
            self.kerros_ylos()
        while self.kerros > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, lukumaara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(lukumaara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        hissi = self.hissit[hissin_numero]
        print(f"nro {hissin_numero} kerroS {kohdekerros}")
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        talo.aja_hissia(0, 0)
        talo.aja_hissia(1, 0)
        talo.aja_hissia(2, 0)




talo = Talo(0, 10, 3)
talo.aja_hissia(0, 5)
talo.aja_hissia(1, 3)
talo.aja_hissia(2, 4)
print("Nyt tulee palohälytys")
time.sleep(5)
talo.palohalytys()