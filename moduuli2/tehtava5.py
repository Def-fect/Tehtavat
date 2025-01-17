luoti, naula, leiviskä = float(input("Anna luotien määrä: ")), float(input("Anna naulojen määrä: ")), float(input("Anna leiviskien määrä: "))





luoti_g = (13.3)
naula_g = (32 * luoti_g)
leiviskä_g = (20 * naula_g)

tulos1 = (luoti * luoti_g)
tulos2 = (naula * naula_g)
tulos3 = (leiviskä * leiviskä_g)

tuloksientulos = (tulos3 + tulos1 + tulos2)
luku1 = 1000

print(luoti_g)
tulos = (tuloksientulos % luku1)
tulos4 = (tuloksientulos // 1000)
print(f"kiloina {(tulos4):.0f}",(f"ja grammoina {(tulos):.0f}"))