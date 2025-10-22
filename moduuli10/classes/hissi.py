class Hissi:
    def __init__(self, new_alin_kerros, new_ylin_kerros):
        self.alin_kerros = new_alin_kerros
        self.ylin_kerros = new_ylin_kerros
        self.kerros = new_alin_kerros

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Olet kerroksessa: {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Olet kerroksessa: {self.kerros}")

    def siirry_kerrokseen(self, numero):
        if numero < self.alin_kerros or numero > self.ylin_kerros:
            print(f"Kerrosta {numero} ei ole")
            return
        while self.kerros != numero:
            if numero > self.kerros:
                self.kerros_ylös()
            elif numero < self.kerros:
                self.kerros_alas()
