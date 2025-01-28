luvut = []

luku = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while luku != "":
    luvut.append(luku)
    luku = input("Anna seuraava nimi tai lopeta painamalla Enter: ")
luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)
