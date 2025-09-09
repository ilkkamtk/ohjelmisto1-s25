import random

total= 0

simulaatiot = 0
while simulaatiot < 100000:
    noppa1 = noppa2 = heitot = 0
    while noppa1 != 6 or noppa2 != 6:
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1
    total = total + heitot
    simulaatiot = simulaatiot + 1


print(f"Tarvittiin {total:d} heittoa. keskiarvo: {total/100000}")
