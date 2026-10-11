lista = [4, 9, 2, 15, 7]
maior = lista[0]

for num in range(0, len(lista)):
    if lista[num] > maior:
        maior = lista[num]

print(maior)