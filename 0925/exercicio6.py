linhas = int(input('Digite o valor de linhas: '))
colunas = int(input('Digite o valor de colunas: '))
mat = []
for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f'Digite o valor de {i}{j}: '))
        mat[i].append(x)

print('Matriz Normal: ')
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat[i][j]}', end=" ")
    print()
    
print('Matriz Transposta: ')
for i in range(colunas):
    for j in range(linhas):
        print(f'{mat[j][i]}', end=" ")   
    print()
    