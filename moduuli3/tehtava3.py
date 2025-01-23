sukupuoli = input("Sukupuoli? : ")
hemoglobiiniarvo = int(input("Hemoglobiiniarvo? : "))

if sukupuoli == 'mies':
    if 195< hemoglobiiniarvo:
        print("hemoglobiiniarvo korkea")
    elif (134 > hemoglobiiniarvo):
            print("hemoglobiiniarvo alhainen ")
    else:
        print('hemoglobiiniarvo normaali')
if sukupuoli == 'nainen':
    if (175< hemoglobiiniarvo):
        print("hemoglobiiniarvo korkea")
    elif (117 > hemoglobiiniarvo):
            print("hemoglobiiniarvo alhainen ")
    else:
        print('hemoglobiiniarvo normaali')