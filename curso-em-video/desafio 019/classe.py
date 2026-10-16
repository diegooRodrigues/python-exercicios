class Livro:
    
    pag_atual = 1

    def __init__(self, titulo, total_pag):
        self.titulo = titulo
        self.total_pag = total_pag

        print(f"Você acabou de abrir o livro '{self.titulo}'. Página atual: {Livro.pag_atual}")


    def avancar_pag(self, num_pag = 1):

        if num_pag + Livro.pag_atual > self.total_pag:
            print(f"Você passou {self.total_pag - Livro.pag_atual} páginas. Página atual {self.total_pag}")
            print(f"Você chegou ao final do livro '{self.titulo}'")
            Livro.pag_atual = self.total_pag
            
        else:
            Livro.pag_atual += num_pag

            print(f"Você passou {num_pag} páginas. Página atual: {Livro.pag_atual}")
            


    def voltar_pag(self, num_pag = 1):

        if num_pag >= Livro.pag_atual: 
            print(f"Você voltou {Livro.pag_atual - 1} páginas. Página atual 1")
        else:
            Livro.pag_atual -= num_pag

            print(f"Você voltou {num_pag} páginas. Página atual: {Livro.pag_atual}")


