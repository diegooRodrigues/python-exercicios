from classe import *

def main():

    r = Retangulo(7, 4)

    try:
        # r.base = 12
        # r.altura = -2
        r.medidas = (3, 9)
    except Exception as e:
        print(f"Ocorreu um ERRO do tipo {type(e).__name__}: {e}")
    

    # r.medidas = 2
    print(r.medidas)
    # print(r.__dict__)


if __name__ == "__main__":
    main()