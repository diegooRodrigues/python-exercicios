# DESAFIO 27

from classe import *

def main():

    g1 = Guerreiro("Diego", 200)
    m1 = Mago("Gandalf", 200)

    g1.atacar(m1, 100)
    g1.curar()
    m1.atacar(g1, 100)
    m1.curar()


if __name__ == "__main__":
    main()