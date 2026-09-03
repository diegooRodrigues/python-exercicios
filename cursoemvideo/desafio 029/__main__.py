from classe import *


def main():
    d = DiarioSecreto("123")

    d.escrever("Essa é a primeira mensagem")
    d.escrever("Estou aprendendo Python")

    try:
        # d.ler()       # Erro por não colocar a senha
        d.senha = "ola"
        # d.senha         # Erro ninguém pode ver a senha
        d.ler("ola")
    except Exception as e:
        print(f"ERRO: {e}")


if __name__ == "__main__":
    main()