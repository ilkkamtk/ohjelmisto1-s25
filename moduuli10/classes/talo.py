from .hissi import Hissi

class Talo:
    def __init__(self, new_alin_kerros, new_ylin_kerros, new_hissien_lkm):
        self.alin_kerros = new_alin_kerros
        self.ylin_kerros = new_ylin_kerros
        self.hissit = []
        for i in range(new_hissien_lkm):
            self.hissit.append(Hissi(self.alin_kerros, self.ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohdekerros):
        print(f"Ajat hissillä {hissin_numero}.")
        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)
        print("--------------------------------")
