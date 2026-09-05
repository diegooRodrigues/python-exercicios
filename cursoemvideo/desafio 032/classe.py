from hashlib import sha256

class ContaBancaria:

    def __init__(self, id:int, titular:str = None, senha:str = None, saldo:float = 0):

        self._id = id                                                   # Atributo Protegido
        self._titular = titular                                         # Atributo Protegido
        self.__saldo = abs(saldo)                                       # Atributo Privado
        
        if senha == None:
            senha = self.pedir_senha()

        self.__hash = sha256(senha.encode("utf-8")).hexdigest()         # Atributo Privado
        print(f"Conta {self._id} criada com SUCESSO. Saldo atual da conta de {self._titular} é de R${self.__saldo:,.2f}")


    def __str__(self) -> str:
        return f"Estado atual da conta: \nID: {self._id} \nTitular: {self._titular} \nSaldo: R${self.__saldo:,.2f}"


    def pedir_senha(self) -> str:

        while True:
            senha = str(input("Senha: ")).strip()
            if len(senha) >= 6:
                break
            print("A senha deve conter pelo menos 6 dígitos.")
        return senha


    def validar_senha(self, senha:str) -> bool:

        usuario = sha256(senha.encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False
    

    def sacar(self, valor:float, senha:str = None):

        if senha is None:
            senha = self.pedir_senha()

        if self.validar_senha(senha):

            if abs(valor) > self.__saldo:
                print(f"Saldo INSUFICIENTE para o saque do valor de R${valor:,.2f}")
            else:
                self.__saldo -= abs(valor)
                print(f"Saque APROVADO na conta {self._id} no valor de R${valor:,.2f}")

        else:
            print("Senha INVÁLIDA! O saque não foi autorizado.")


    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito REALIZADO na conta {self._id} no valor de R${valor:,.2f} \nSaldo atual: R${self.__saldo:,.2f}")


    @property
    def nome(self) -> str:
        return self._titular


    @nome.setter
    def nome(self, novoNome:str = None):
        senha = self.pedir_senha()

        if self.validar_senha(senha):
            if len(novoNome) >= 5:
                self._titular = novoNome
        else:
            print("Senha INVÁLIDA! Não foi possível alterar o nome.")