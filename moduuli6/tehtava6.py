import math
def pizza1():
    eurohinta=float(input("Anna ensimmäisen pizzan hinta"))
    halkaisija = float(input("Anna ensimmäisen pizzan halkaisija"))
    neliom=(halkaisija**2*(math.pi/4))/1000
    print(neliom)
    return
print(pizza1())