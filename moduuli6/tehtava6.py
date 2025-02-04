import math
def pizza1():
    eurohinta=float(input("Anna ensimmäisen pizzan hinta"))
    halkaisija = float(input("Anna ensimmäisen pizzan halkaisija"))
    neliom=(halkaisija**2*(math.pi/4))/1000
    x=neliom/eurohinta
    return x
def pizza2():
    eurohinta2=float(input("Anna toisen pizzan hinta"))
    halkaisija2 = float(input("Anna toisen pizzan halkaisija"))
    neliom2=(halkaisija2**2*(math.pi/4))/1000
    x2=neliom2/eurohinta2
    return x2

pizza1=pizza1()
pizza2=pizza2()

if pizza2<pizza1:
    print("ensimmäinen pizza on edullisempi",pizza1)
else:
    print("toinen pizza on edullisempi", pizza2)
