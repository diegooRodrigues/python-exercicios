from classe import *

def main():
    c = ContaBancaria(1, "Diego")
    c.depositar(100)
    c.sacar(50)

    c.nome = "Diegooo"

    print(c)

    # print(c.__dict__)

if __name__ == "__main__":
    main()