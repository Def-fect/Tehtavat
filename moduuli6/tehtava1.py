import random
def heitto():
    return(random.randint(1,6))
while True:
    noppa=heitto()
    print(noppa)
    if noppa==6:
        break