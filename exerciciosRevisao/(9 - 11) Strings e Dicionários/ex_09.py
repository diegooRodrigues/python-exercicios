palavra = input("Digite uma palavra: ").lower()
numVogais = 0

for i in range(len(palavra)):
    if palavra[i] in ('a', 'e', 'i', 'o', 'u'):
        numVogais += 1

print(f"O número de vogais em {palavra} é {numVogais}")