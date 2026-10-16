def eh_primo(numero):

    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

print(eh_primo(13))