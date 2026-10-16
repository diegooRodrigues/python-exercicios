# DESAFIO 25

from classe import *

def main():
    dist = 10
    modo1 = Moto(dist)
    modo2 = Caminhao(dist)
    modo3 = Drone(dist)

    print(f"""
Distância: {dist} km

Tipo       Valor (R$)
{type(modo1).__name__}     | {modo1.calc_frete()}
{type(modo2).__name__} | {modo2.calc_frete()}
{type(modo3).__name__}    | {modo3.calc_frete()}
""")
    


if __name__ == "__main__":
    main()