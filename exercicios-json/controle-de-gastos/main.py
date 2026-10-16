import funcoes

def main():
    caminho = "lista_de_gastos.json"
    lista_de_gastos = funcoes.carregarLista(caminho)

    while True:
        print("1. Adicionar gasto")
        print("2. Listar gastos")
        print("3. Excluir gasto")
        print("0. Sair")

        opc = input("> ")

        match opc:
            case "1":
                funcoes.adicionarGasto(caminho, lista_de_gastos)
            case "2":
                funcoes.listarGastos(lista_de_gastos)
            case "3":
                funcoes.excluirGasto(caminho, lista_de_gastos)
            case "0":
                break
            case _:
                print("Valor inválido.\n")



if __name__ == "__main__":
    main()