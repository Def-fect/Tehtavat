luoti, naula, leiviskä = float(input("Anna luotien määrä: ")), float(input("Anna naulojen määrä: ")), float(input("Anna leiviskien määrä: "))

luoti_g = (13.3)
naula_g = (32 * luoti_g)
leiviskä_g = (20 * naula_g)

massa_grammoina = leiviskä_g * leiviskä + naula_g * naula + luoti_g * luoti
luku1 = 1000

tulos = (massa_grammoina % luku1)
tulos4 = (massa_grammoina // 1000)
print(f"kiloina {(tulos4):.0f}",(f"ja grammoina {(tulos):.2f}"))