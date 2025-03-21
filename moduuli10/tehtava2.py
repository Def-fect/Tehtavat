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
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin

    def aja_hissiä:


hissi = Hissi(0)
print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(5)
print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(0)
print(f"{hissi.kerros}")