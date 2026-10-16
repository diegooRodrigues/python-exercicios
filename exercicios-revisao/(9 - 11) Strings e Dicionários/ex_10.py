palavra = input("Digite uma palavra: ")
inverso = ""

for letra in palavra:
    inverso = letra + inverso   # coloca a letra NA FRENTE

if palavra == inverso:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")