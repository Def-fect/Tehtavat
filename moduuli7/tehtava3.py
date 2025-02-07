lentoasema=set()

while True:
    userinput=input("syötä uusi, tulosta tai lopettaa")
    if userinput=="tulosta":
        print(lentoasema)
    if userinput=="uusi":
        userinput1=input("syötä uusi lentoasema")
        lentoasema.add(userinput1)
    if userinput=="lopeta":
        break

