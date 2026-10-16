class Termostato:

    def __init__(self):
        self.__temperatura = 24


    @property
    def temperatura(self): # Método GETTER
        return self.__temperatura


    @temperatura.setter
    def temperatura(self, valor): # Método SETTER

        if valor > 30:
            self.__temperatura = 30
        elif valor < 16:
            self.__temperatura = 16
        elif valor % 0.5 == 0:
            self.__temperatura = valor
        else:
            raise ValueError(f"A temperatura {valor}ºC é INVÁLIDA!")


    @property
    def ftemperatura(self):
        return f"{self.__temperatura}ºC"