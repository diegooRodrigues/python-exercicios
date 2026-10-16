# DESAFIO 18
from classe import Churrasco

def main():
    c1 = Churrasco("Churras dos Amigos", 15)
    c1.analisar()
    print()
    c2 = Churrasco("Churrasco de Natal", 25)
    c2.analisar()

if __name__ == "__main__":
    main()