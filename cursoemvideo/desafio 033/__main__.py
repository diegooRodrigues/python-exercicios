from classe import *

def main():

    # p = Pessoa("Diego", 2003)

    # try:
    #     # p.nascimento = 1111
    #     p.idade = 18

    # except Exception as e:

    #     print(f"Erro: {e}")

    # print(p.idade)
    # print(p.__dict__)


    a = Aluno("Diego", 2003, "SI")

    a.add_curso("ADM")

    print(a.__dict__)
    print(Aluno.cursosOficiais)

if __name__ == "__main__":
    main()