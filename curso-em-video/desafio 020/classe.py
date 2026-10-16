class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []


    def add_jogos(self, nome_jogo):
        self.jogos_favoritos.append(nome_jogo)


    def ficha(self):
        print(f"******** {self.nick} ********")
        print(f"Nome real: {self.nome}")

        for jogo in self.jogos_favoritos:
            print(jogo)
        

