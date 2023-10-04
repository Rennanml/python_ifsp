A = int(input('Insira o nível do primeiro jogador\n'))
B = int(input('Insira o nível do segundo jogador\n'))
C = int(input('Insira o nível do terceiro jogador\n'))
D = int(input('Insira o nível do quarto jogador\n'))

if A < 0 or B < 0 or C < 0 or D < 0 or A > 10000 or B > 10000 or C > 10000 or D > 10000:
    print('Os números não respeitam as regras de entrada\n')
    exit()

X = A + D
Y = B + C

diferenca = X - Y

print(diferenca)
