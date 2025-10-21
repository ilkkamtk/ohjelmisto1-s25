class Auto:
    def __init__(self, new_rekisteritunnus, new_huippunopeus):
        self.rekisteritunnus = new_rekisteritunnus
        self.huippunopeus = new_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, arvo):
        pass
        # lisää arvo self nopeuteen
        # tarkasta ettei nopeus ole yli huippunopeus.
        #Jos on, aseta nopeus = huippunopeus
        # tarkasta ettei nopeus ole alle 0
        # Jos on, aseta nopeus = 0

    def kulje(self, aika):
        pass
        # laske kuinka paljon auto on kulkenut annetussa ajassa tietyllä nopeudella
        # lisää kuljettu matka kokonaismatkaan

    # ehkä metodi, joka palauttaa ominaisuudet sanakirjana