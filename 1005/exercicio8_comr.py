def exibir_algarismos(numero):
    if numero < 10:
        print(numero)
    else:
        exibir_algarismos(numero // 10)
        print(numero % 10)

print(exibir_algarismos(123))