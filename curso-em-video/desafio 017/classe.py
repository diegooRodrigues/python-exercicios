class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        print(f"--- {self.nome} ---")
        print(f"R${self.valor:,.2f}")
        print()
