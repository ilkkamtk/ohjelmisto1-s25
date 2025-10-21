from classes.auto import Auto

autot = []

auto1 = Auto("ABC-123", 142)
auto2 = Auto("ASD-154", 156)
auto3 = Auto("OIS-203", 180)

autot.append(auto1)
autot.append(auto2)
autot.append(auto3)

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekisteritunnus}
    Huippunopeus: {auto.huippunopeus}
    Nopeus: {auto.nopeus}
    Matka: {auto.matka}
    """)