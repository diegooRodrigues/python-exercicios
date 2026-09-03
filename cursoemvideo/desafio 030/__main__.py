from classe import *

def main():

    c = Credencial()

    c.senha = "CeV!@"

    print(c.senha)

    c.validar('Teste123')
    c.validar('CeV!@')


if __name__ == "__main__":
    main()