linhas = int(input('Digite o valor de "linhas": '))
colunas = int(input('Digite o valor de "colunas:": '))
mat = []
for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f'Digite o valor de {i}{j}: '))
        mat[i].append(x)
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat[i][j]}', end="  ")
    print('\n')

        