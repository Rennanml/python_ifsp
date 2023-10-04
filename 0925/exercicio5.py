linha = int(input('Digite o valor de linha: '))
coluna = int(input('Digite o valor de coluna: '))
mat1 = []
mat2 = []
matSoma = []


#Monta a matriz 1
for i in range(linha):
    mat1.append([])
    for j in range(coluna):
        x1 = int(input(f'Digite o valor de {i}{j} da matriz 1: '))
        mat1[i].append(x1)

#Monta a matriz 2       
for i in range(linha):
    mat2.append([])
    for j in range(coluna):
        x2 = int(input(f'Digite o valor de {i}{j} da matriz 2: '))
        mat2[i].append(x2)

#Faz a soma e monta a matrizSoma
for i in range(linha):
    matSoma.append([])
    for j in range(coluna):
        matSoma[i].append(mat1[i][j] + mat2[i][j])
        
#Printa mat1
print('Matriz 1: ')
for i in range(linha):
    for j in range(coluna):
        print(f'{mat1[i][j]}', end=" ")
    print()
    
#Printa mat2
print('Matriz 2: ')
for i in range(linha):
    for j in range(coluna):
        print(f'{mat2[i][j]}', end=" ")
    print()
    
#Printa matriz soma
print('Matriz resultante: ')
for i in range(linha):
    for j in range(coluna):
        print(f'{matSoma[i][j]}', end=" ")
    print()



       