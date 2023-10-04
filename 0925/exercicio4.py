n = int(input('Digite a ordem de uma matriz quadrada: '))
linha = n
coluna = n
mat = []

for i in range(linha):
    mat.append([])
    for j in range(coluna):
        x = int(input(f'Digite o valor de {i}/{j}: '))
        mat[i].append(x)

print('Matriz Natural: ')
for i in range(linha):
    for j in range(coluna):
        print(f'{mat[i][j]}', end=" ")
    print()


for i in range(linha):
    for j in range(coluna):
        if i == j:
            mat[i][j] = 1
        else:
            mat[i][j] = 0
            
print('Matriz Identidade: ')
for i in range(linha):
    for j in range(coluna):
        print(f'{mat[i][j]}', end=" ")
    print()
