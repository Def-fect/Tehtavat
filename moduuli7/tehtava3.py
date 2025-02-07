airport_data = {}

while True:
    syöttö = input("syötä uusi, tulosta tai lopeta: ")

    if syöttö == "tulosta":
        userinput = input("Anna lentokenttä, jonka ICAO-koodin haluat tietää: ")
        if userinput in airport_data:
            print(f"ICAO koodi {userinput} kuuluu lenttokenttälle: {airport_data[userinput]}.")
        else:
            print("Lentokenttää ei löydy.")

    if syöttö == "uusi":
        airport = input("Anna lentokenttä: ")
        ICAO = input("Anna ICAO-koodi: ")
        airport_data[ICAO] = airport
    if syöttö == "lopeta":
        break
