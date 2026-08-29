# DESAFIO 21

from classe import Caneta

def main():
    
    c1 = Caneta("azul")

    c1.escrever("Olá")
    c1.destampar()
    c1.destampar()
    c1.escrever("Olá, Mundo!")
    c1.escrever("Eu meu chamo Diego!")
    c1.quebrar_linha(2)
    c1.escrever("Estou aprendendo POO.")
    c1.tampar()
    c1.tampar()


if __name__ == "__main__":
    main()