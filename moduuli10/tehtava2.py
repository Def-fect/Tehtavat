class Hissi:
    def __init__(self, kerros):
        self.kerros = kerros



    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
        self.kerros -= 1

    def siirry_kerrokseen(self, siirry):
        while self.kerros < siirry:
            hissi.kerros_ylos()

        while self.kerros > siirry:
            hissi.kerros_alas()
class Talo:
    def __init__(self, alin_nro, ylin_nro, kerros):
        self.alin_nro = alin_nro
        self.ylin_nro = ylin_nro

    def aja_hissiä:

hissit = []
hissi = Hissi(0)

talo = Talo(0, 10, 3)

print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(5)
print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(0)
print(f"{hissi.kerros}")