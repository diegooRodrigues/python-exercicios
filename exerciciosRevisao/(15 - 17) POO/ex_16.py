class ContaBancaria:

    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
            return False
        
        self.saldo += valor
        print(f"O valor de R${valor:.2f} foi depositado.")
        return True

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return False

        if valor <= 0:
            print("O valor do saque deve ser maior que R$00,00")
            return False

        self.saldo -= valor
        print(f"O valor de R${valor:.2f} foi sacado! Saldo atual R${self.saldo:.2f}")
        return True

    def mostrar_saldo(self):
        print(f"O saldo de {self.titular} é R${self.saldo:.2f}")


c1 = ContaBancaria("Diego")

c1.depositar(1000)
c1.depositar(0)
c1.depositar(-10)
c1.sacar(500)
c1.sacar(-500)
c1.sacar(0)

c1.mostrar_saldo()