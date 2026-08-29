class Caneta:

    estado = False

    def __init__(self, cor):
        self.cor = cor

    def destampar(self):

        if self.estado == True:
            print("A caneta já está destampada!")
        else:
            self.estado = True
            print("A caneta foi destampada!")


    def tampar(self):

        if self.estado == False:
            print("A caneta já está tampada!")
        else:
            print("\nA caneta foi tampada!")
            self.estado = False


    def escrever(self, texto):

        if self.estado == False:
            print("A caneta está tampada. Não é possível escrever!")
        else:
            print(texto, end=" ")

    def quebrar_linha(self, qtd_linha=1):
        for linha in range(qtd_linha):
            print()



