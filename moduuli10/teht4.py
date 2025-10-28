from classes.auto import Auto
from classes.kilpailu import Kilpailu
import random

autot = []

for i in range(1, 11):
    huippunopeus = random.randint(150, 200)
    autot.append(Auto("ABC-" + str(i), huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        print(f"\n--- Tilanne {tunti}. tunnin jälkeen ---")
        kilpailu.tulosta_tilanne()

print(f"\n--- Kilpailu päättyi {tunti}. tunnin jälkeen ---")
kilpailu.tulosta_tilanne()


