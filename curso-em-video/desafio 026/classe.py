from abc import ABC, abstractmethod

class Funcionario(ABC):

    sal_min = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0


    def analisar_sal(self):
        return f"Isso é o equivalente à {self.calc_sal() / self.sal_min :.1f} salários mínimos"


    @abstractmethod
    def calc_sal():
        pass


class Horista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab


    def calc_sal(self):
        return self.sal_bruto * (1 - (Funcionario.inss/100))


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto


    def calc_sal(self):
        return self.sal_bruto * (1 - (Funcionario.inss/100))

