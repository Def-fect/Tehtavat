import random
max=int(input("Anna nopan tahkojen määrä"))
def heitto():
    return(random.randint(1,max))
while True:
    noppa=heitto()
    print(noppa)
    if noppa==max:
        break