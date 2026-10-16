numeros = list()
soma = 0

for i in range(0, 5):
    numeros.append(int(input("Digite um número: ")))
    soma += numeros[i]

print(f"A soma dos números é {soma}")
print(f"A média dos números é {soma / len(numeros)}")