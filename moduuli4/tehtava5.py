salasana1 = "rules"
tunnus = "python"


yritys=0


while yritys<5:
    käyttäjätunnus=input("Anna käyttäjätunnus:")
    salasana = input("Anna salasana:")

    if käyttäjätunnus == tunnus and salasana == salasana1:
        print("Tervetuloa ")
        break
    else:
        yritys = yritys + 1
if yritys==5:
    print("Pääsy evätty")
