lista = ["diego", "maria", "eduardo", "ana"]
nome = input("Digite um nome: ").lower()
estaNaLista = False

for i in range(len(lista)):
    if nome == lista[i]:
        estaNaLista = True
        break

if estaNaLista:
    print("O nome está na lista")
else:
    print("O nome não está na lista")