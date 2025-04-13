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

hissi = Hissi(0,10)
print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(5)
print(f"{hissi.kerros}")
hissi.siirry_kerrokseen(0)
print(f"{hissi.kerros}")