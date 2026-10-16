numPares = 0
lista = list()

for i in range(0,5):
    lista.append(int(input("Digite um número: ")))
    if lista[i] % 2 == 0:
        numPares += 1

print(f"Existem {numPares} números pares na lista.")