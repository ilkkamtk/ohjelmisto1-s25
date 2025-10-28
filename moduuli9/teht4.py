from classes.auto import Auto
import random
from prettytable import PrettyTable

autot = []
tulostettavat = PrettyTable()
tulostettavat.field_names = ["Rekisteritunnus", "nopeus", "huippunopeus", "matka"]

for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        auton_nopeus = random.randint(-10, 15)
        auto.kiihdytä(auton_nopeus)
        auto.kulje(1)
        if auto.matka > kokonaismatka:
            kokonaismatka = auto.matka


autot.sort(key = lambda car: car.matka, reverse = True)

for auto in autot:
    tulostettavat.add_row([auto.rekisteritunnus, auto.nopeus, auto.huippunopeus, auto.matka])

print(tulostettavat)