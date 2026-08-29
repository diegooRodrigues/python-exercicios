from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, dist):
        self.dist = dist
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, dist):
        super().__init__(dist)
        

    def calc_frete(self):
        self.frete = Moto.fator * self.dist
        return self.frete


class Caminhao(Transporte):
    fator = 1.20
    
    def __init__(self, dist):
        super().__init__(dist)
        

    def calc_frete(self):
        if self.dist < 50:
            return f"A distância mínima deve ser de 50Km."
        self.frete = Caminhao.fator * self.dist
        return self.frete


class Drone(Transporte):
    fator = 9.50
    
    def __init__(self, dist):
        super().__init__(dist)
        

    def calc_frete(self):
        if self.dist > 10:
            return f"A distância máxima é 10Km." 
        self.frete = Drone.fator * self.dist
        return self.frete



