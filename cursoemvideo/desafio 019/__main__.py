# DESAFIO 19

from classe import Livro


def main():
    l1 = Livro("10 coisas que aprendi", 20)
    l1.avancar_pag()
    l1.voltar_pag(1)
    l1.avancar_pag(10)
    l1.voltar_pag(5)
    l1.voltar_pag(15)


if __name__ == "__main__":
    main()
