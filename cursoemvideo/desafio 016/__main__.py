# DESAFIO 16
from classe import Funcionario


def main():

    f1 = Funcionario("Maria", "Administração", "Diretora")
    f2 = Funcionario("Pedro", "TI", "Programador")

    print(f1.apresentar())
    print(f2.apresentar())



if __name__ == "__main__":
    main()