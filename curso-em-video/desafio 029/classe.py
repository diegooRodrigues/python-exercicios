class DiarioSecreto:

    def __init__(self, senha):
        self.__senha = senha
        self.__segredos = []


    def escrever(self, mensagem):
        self.__segredos.append(mensagem)


    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("Senha INVÁLIDA! Você não tem permissão para ler o diário.")
        else:
            print("DIÁRIO LIBERADO!")
            for mensagem in self.__segredos:
                print(mensagem)

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha!")

    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha
        print(f"Senha alterada com SUCESSO!")