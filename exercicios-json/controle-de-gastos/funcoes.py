import json

def carregarLista(caminho):

    try:
        with open(caminho, "r", encoding = "utf8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Arquivo corrompido.\n")
        exit()


def salvarLista(caminho, lista):
    # salva os novos valores
    with open(caminho, "w", encoding = "utf-8") as arquivo:
        json.dump(lista, arquivo, indent = 4, ensure_ascii = False)


def listarGastos(lista):

    if not lista:
        print("Não há gasto cadastrado.\n")
        return

    for index, gasto in enumerate(lista, start = 1):
        print(f"{index}. Descrição: {gasto['descricao']} - R${gasto['valor']:.2f}\n")


def adicionarGasto(caminho, lista):
    
    descricao = input("Descrição: ")
    if not descricao:
        print("Deve inserir uma descrição.\n")
        return

    try:
        valor = float(input("Valor: R$"))
    except ValueError:
        print("É preciso inserir um valor.\n")
        return

    lista.append({
        "descricao": descricao,
        "valor": valor
    })
    salvarLista(caminho, lista)


def excluirGasto(caminho, lista):

    if not lista:
        print("Não há gasto cadastrado.\n")
        return

    while True:
        try:
            posicao = int(input("Qual deseja excluir? "))
            break
        except ValueError:
            print("Digite apenas números")


    if 0 < posicao <= len(lista):
        lista.pop(posicao - 1)
        salvarLista(caminho, lista)
    else:
        print("Valor indisponível")
