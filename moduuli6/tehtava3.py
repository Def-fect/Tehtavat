def gallons():
    return gal * 3.785

while True:
    gal = float(input("anna galloonat"))
    if gal>0:
        print(gallons())
    else:
        break


