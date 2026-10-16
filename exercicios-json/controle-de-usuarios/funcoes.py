import json

def carregarLista(caminho):
    try:
        with open(caminho, "r", encoding = "utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        # retorna uma lista vazia quando é executado o código pela primeira vez
        return []

    except json.JSONDecodeError:
        print("Arquivo corrompido.")
        exit()


def verUsuarios(lista_de_usuarios):

    if not lista_de_usuarios:
        print("Não há usuario cadastrado.\n")
        return

    for index, usuario in enumerate(lista_de_usuarios, start = 1):
        print(f"{index}. Nome: {usuario["nome"]}\nIdade: {usuario["idade"]}\nCidade: {usuario["cidade"]}\n")


def adicionarUsuario(caminho, lista_de_usuarios):

    nome = input("Nome: ").strip()
    if not nome:
        print("É preciso inserir um nome.\n")
        return

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("É preciso inserir um número.\n")
        return

    cidade = input("Cidade: ").strip()
    if not cidade:
        print("É preciso inserir um nome.\n")
        return

    lista_de_usuarios.append({
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    })

    # reescreve o arquivo com as adições
    with open(caminho, "w", encoding = "utf-8") as arquivo:
        json.dump(lista_de_usuarios, arquivo, indent = 4, ensure_ascii = False)