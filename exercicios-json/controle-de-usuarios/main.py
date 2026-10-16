import funcoes

def main():
    caminho = "lista_de_usuarios.json"
    usuarios = funcoes.carregarLista(caminho)

    while True:
        print("(1) Adicionar usuario")
        print("(2) Ver lista de usuarios")
        print("(0) Sair")

        opc = input("> ")

        match opc:
            case "1":
                funcoes.adicionarUsuario(caminho, usuarios)
            case "2":
                funcoes.verUsuarios(usuarios)
            case "0":
                break
            case _:
                print("Opção inválida!\n")



if __name__ == "__main__":
    main()