from classes.auto import Auto

autot = []

for i in range(10):
    # arvo huippunopeus 100-200
    huippunopeus = 0
    autot.append(Auto("ABC-" + str(i + 1), huippunopeus))

kokonaismatka = 0
while kokonaismatka < 10000:
    for auto in autot:
        # arvo nopeuden muutos -10 - 15
        # kutsu kiihdytä
        auto.kulje(1)
        # hae matkan arvo, jos yli 10000, lopeta kisa asettamalla auton matka
        # kokonaismatkaksi

# googlaa joku taulukkokirjasto tulostamiseen