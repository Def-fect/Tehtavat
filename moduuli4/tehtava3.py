max, min =0, None
while True:
    merkkijono =(input("Anna merkkijono"))
    if merkkijono == "":
        break
    merkkijono=int(merkkijono)
    if min is None or merkkijono < min:
        min=merkkijono
    if merkkijono > max:
        max = merkkijono
print(f"Pienin luku :{min}")
print(f"Pienin luku :{max}")