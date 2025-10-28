import random
from tabulate import tabulate

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auton_nopeus = random.randint(-10, 15)
            auto.kiihdytä(auton_nopeus)
            auto.kulje(1)

    def tulosta_tilanne(self):
        self.autot.sort(key=lambda car: car.matka, reverse=True)
        tulostettavat = []
        for auto in self.autot:
            tulostettavat.append([auto.rekisteritunnus, auto.nopeus, auto.huippunopeus, auto.matka])

        print(tabulate(tulostettavat, ["rekisteritunnus", "nopeus", "huippunopeus", "matka"]))

    def kilpailu_ohi(self):
        return any(auto.matka >= self.pituus for auto in self.autot)

        """
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False
        """


