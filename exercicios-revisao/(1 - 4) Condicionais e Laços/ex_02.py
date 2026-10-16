nota = float(input("Digite sua nota (0 - 10): "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
elif nota >= 0:
    print("Reprovado")
else:
    print("Nota inválida")
