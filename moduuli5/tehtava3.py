
num = int(input("Anna luku"))

if num > 1:
    for i in range(2, (num // 2) + 1):
        if (num % i) == 0:
            print(num, "ei ole alkuluku")
            break
    else:
        print(num, "luku on alkuuku")
else:
    print(num, "ei ole alkuluku")