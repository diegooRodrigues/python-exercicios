from math import pi
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        print(f"O perímetro do quadrado é {self.lado * self.qtd_lados}cm")

    def area(self):
        print(f"A Área do quadrado é {self.lado * self.lado}cm²")


class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(1)
        self.raio = raio

    def perimetro(self):
        print(f"O perímetro do círculo é {2 * pi * self.raio :.2f}cm")

    def area(self):
        print(f"A área do círculo é {pi * self.raio**2 :.2f}cm²")

