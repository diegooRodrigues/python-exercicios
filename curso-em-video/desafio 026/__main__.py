# DESAFIO 26

from classe import *

def main():
    f1 = Horista("Paulo", 12, 190)
    f2 = Mensalista("Amanda", 8500)

    print(f"{f1.nome} ganha R${f1.calc_sal():.2f}")
    print(f1.analisar_sal())

    print()

    print(f"{f2.nome} ganha R${f2.calc_sal():.2f}")
    print(f2.analisar_sal())


if __name__ == "__main__":
    main()