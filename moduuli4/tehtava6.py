import random
import math

N = 0 #kaikkien arvottujen pisteiden lukumäärä
n = 0 #Yksikköympyrän sisään osuneiden pisteen lkm
lkm = 10000000

while N<lkm:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2<1:
         n+=1
    N+=1

piin_likiarvo=4*n/N
print(f'Piin likiarvo on{piin_likiarvo} ja ero tarkkaan {math.pi- piin_likiarvo}')