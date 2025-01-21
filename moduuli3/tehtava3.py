sukupuoli = input("Sukupuoli? : ")
if sukupuoli == ('mies') or ('nainen'):
    hemoglobiiniarvo = int(input("Hemoglobiiniarvo? : "))

if sukupuoli == ('mies'):
    if (195< hemoglobiiniarvo):
        print("hemoglobiiniarvo korkea")
    if (134 > hemoglobiiniarvo):
            print("hemoglobiiniarvo alhainen ")
    if (195<hemoglobiiniarvo>134):
        print('normaali')
if sukupuoli == ('nainen'):
    if (175< hemoglobiiniarvo):
        print("hemoglobiiniarvo korkea")
    if (117 > hemoglobiiniarvo):
            print("hemoglobiiniarvo alhainen ")