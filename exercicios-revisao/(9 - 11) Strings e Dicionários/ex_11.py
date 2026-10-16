notas = {"Ana": 6, "Bruno": 4, "Diego": 9}
maior = -1
melhorAluno = ""


for nome in notas:
    if notas[nome] > maior:
        maior = notas[nome]
        melhorAluno = nome

print(melhorAluno, maior)