def fatorial(numero):

    resultado = 1

    for i in range(numero):
        resultado *= (numero - i)

    return resultado

num = int(input("Digite um número: "))

print(fatorial(num))