class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.altura * self.largura

    def perimetro(self):
        return self.altura * 2 + self.largura * 2


re1 = Retangulo(2, 5)
re2 = Retangulo(3, 10)

print(re1.area())
print(re2.area())
print(re1.perimetro())
print(re2.perimetro())