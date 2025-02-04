nimet = set()

while True:
    userinput = input("Anna nimi: ")
    if userinput == "":
        break
    if userinput in nimet:
        print("Aiemmin syötetty nimi", nimet)
    elif userinput not in nimet:
        nimet.add(userinput)
        print("Uusi nimi", userinput)
print("Annetut nimet")
for userinput in nimet:
    print(userinput)
