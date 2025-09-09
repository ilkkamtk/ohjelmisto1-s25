import math

alkukorkeus = float(input("anna esineen korkeus: "))

PUTOAMISKIHTYVYYS = 9.81

kokonaisaika = math.sqrt(2 * alkukorkeus / PUTOAMISKIHTYVYYS)

aika = 0
while aika < kokonaisaika:
    matka = 0.5 * PUTOAMISKIHTYVYYS * aika ** 2
    print(f"aika: {aika:.2f}s, korkeus: {(alkukorkeus - matka):.2f}m")
    aika = aika + 1

print(f"kokonaisaika: {kokonaisaika:.2f}s")

