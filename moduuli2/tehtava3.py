import math

kanta = input("mikä on kannan pituus?: ")
korkeus = input("mikä on korkeus?: ")

kanta=float(kanta)
korkeus =float(korkeus)

piiri = int((korkeus * 2) +(kanta * 2))

pintaala = int(korkeus * kanta)

piiri = ((korkeus * 2) +(kanta * 2))

pintaala = (korkeus * kanta)

print("suorakulmion pinta-ala on: " + str(piiri))
print("suorakulmion pinta-ala on: " + str(pintaala))
