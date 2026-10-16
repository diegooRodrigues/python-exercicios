class Churrasco:
    """
Recebe o título do churrasco e a quantidade de pessoas que participarão e imprime as informações
    """
    
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada kg de carne custa R$82.40

    def __init__(self, titulo, qnt):
        self.titulo = titulo
        self.participantes = qnt


    def analisar(self) -> str :
        print(f"Cada participante comerá {Churrasco.consumo_padrao}kg e cada kg custa R${Churrasco.preco_kg}")
        print(f"Recomendo comprar {self.participantes * Churrasco.consumo_padrao:,.3f}kg de carne")
        print(f"O custo será de R${self.participantes * Churrasco.consumo_padrao * Churrasco.preco_kg:,.2f}")
        print(f"Cada pessoa pagará R${(self.participantes * Churrasco.consumo_padrao * Churrasco.preco_kg)/self.participantes:,.2f} para participar.")

