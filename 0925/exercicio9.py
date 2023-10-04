linhas = int(input('Digite o valor de linhas: '))
colunas = int(input('Digite o valor de colunas: '))
mat1 = []
mat2 = []

for i in range(linhas):
    mat1.append([])
    for j in range(colunas):
        x1 = int(input(f'Digite o valor de {i}{j} da matriz 1: '))
        mat1[i].append(x1)
        
for i in range(linhas):
    mat2.append([])
    for j in range(colunas):
        x2 = int(input(f'Digite o valor de {i}{j} da matriz 2: '))
        mat2[i].append(x2)

print('Matriz 1: ')       
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat1[i][j]}', end=" ")
    print()

print('Matriz 2: ')
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat2[i][j]}', end=" ")
    print()
   
mult_mat = []
print('Resultado da multiplicação: ')
for i in range(linhas):
    mult_mat.append([])
    for j in range(colunas):
        mult_mat[i].append(mat1[i][j] * mat2[i][j])

for i in range(linhas):
    for j in range(colunas):
        print(f'{mult_mat[i][j]}', end=" ")
    print()
            
        