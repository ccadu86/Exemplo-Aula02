class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calc_area(self):
        area = 3.14 * self.raio ** 2
        return area

    def calc_circo(self):
        circo = 6.28 * self.raio
        return circo
    
class Paralelepipedo:
    def __init__(self, comprimento, largura, altura):
        self.comprimento = comprimento
        self.largura = largura
        self.altura = altura

    def calc_volume(self):
        volume = self.comprimento * self.largura * self.altura
        return volume

class Cilindro:
    def __init__(self, raio, altura):
        self.raio = raio
        self.altura = altura
