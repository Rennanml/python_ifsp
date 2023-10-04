n = int(input('Digite o valor de "N": '))
linhas = n
colunas = n
mat = []
for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f'Digite o valor de {i}{j}: '))
        mat[i].append(x)
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat[i][j]}', end=" ")
    print()
    
aux1 = 0
aux2 = 0

for i in range(len(mat)):
    print(mat[aux1][aux2], end=" ")
    aux1 += 1
    aux2 += 1