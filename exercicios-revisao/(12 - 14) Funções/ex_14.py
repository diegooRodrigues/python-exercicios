def contar_palavras(texto):
    return len(texto.split())

texto = input("Digite uma frase: ")

print(contar_palavras(texto))