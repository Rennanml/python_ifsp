A = int(input('Insira o número de moedas que há na arca\n'))

if A < 3 or A > 10000:
    print('O número de moedas não condiz com o intervalo determinado\n')
    exit()

N = int(input('Insira o número de marinheiros, sem contar o capitão, que estão no barco\n'))

if N < 0 or N > 1000:
    print('O número de marinheiros não condiz com o intervalo determinado\n')
    exit()

marinheiros = A / (N + 2)
capitao = marinheiros * 2

print(capitao)
