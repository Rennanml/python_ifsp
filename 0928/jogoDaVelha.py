tabuleiro = []
aux = True
contador = 0

while aux:
    tabuleiro.append([])
    first_number = int(input('Digite o primeiro número: '))
    second_number = int(input('Digite o segundo número: '))
    letra = input('Digite a letra a ser jogada (O ou X): ')
    tabuleiro[contador].append(first_number, second_number, letra)
    for i in range(len(tabuleiro)):
        for j in range(tabuleiro[i]):
            if True:
                ...