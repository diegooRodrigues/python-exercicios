from classe import *


def main():
    t1 = Termostato()
    t1.temperatura = 22.5
    try:
        t1.temperatura = 25.4
    except Exception as e:
        print(f"Houve um problema: {e}")
        
    print(f"A temperatura atual é {t1.ftemperatura}")




if __name__ == "__main__":
    main()