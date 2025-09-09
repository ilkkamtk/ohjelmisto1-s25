luku = int(input("Anna positiivinen kokonaisluku: "))

if luku > 0:
    check = 0

    while luku > check:
        if check % 2 == 0:
            print(check)

        check = check + 1
else:
    print('virhe: luku on nolla tai negatiivinen')


