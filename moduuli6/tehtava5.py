numerot=[1,2,3,4,5,6,7,8,9]
pari=[]

def perus(numerot):
    return numerot
def parilliset(numerot):
    for luku in numerot:
        if luku % 2==0:
            pari.append(luku)
    return pari
print(f"numerot: {perus(numerot)}")
print(f"parilliset numerot: {parilliset(numerot)}")
