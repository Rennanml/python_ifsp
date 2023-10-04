n = int(input('Digite o valor de N: '))
linhas = n
colunas = n
mat = []
for i in range(linhas):
    mat.append([])
    for j in range(colunas):
        x = int(input(f'Digite o valor de {i}{j}: '))
        mat[i].append(x)
        
print('Matriz normal: ')
for i in range(linhas):
    for j in range(colunas):
        print(f'{mat[i][j]}', end=" ")
    print()
    
mat_transposta = []

for i in range(colunas):
    mat_transposta.append([])
    for j in range(linhas):
        mat_transposta[i].append(mat[j][i])
print('Matriz transposta: ')
for i in range(colunas):
    for j in range(linhas):
        print(f'{mat_transposta[i][j]}', end=" ")
    print()
aux = True   
for i in range(linhas):
    for j in range(colunas):
        if mat[i][j] != mat_transposta[i][j]:
            aux = False
            break    
            
if aux:
    print('A matriz é simétrica!!')
else:
    print('A matriz não é simétrica!!')            