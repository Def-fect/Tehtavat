import random
oikea_luku = random.randint(1, 10)
arvaus = None
print("Tietokone on arvonut luvun 1-10")
while arvaus != oikea_luku:
    arvaus = input("Anna arvauksesi: ")

    if not arvaus.isdigit():
        print("Anna kokonaisluku")
        continue
    arvaus = int(arvaus)
    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein")