mat = []
aux = 0
soma = []
for i in range(3):
    mat.append([])
    for j in range(3):
        x = int(input(f'Digite o valor de ({i})({j}): '))
        aux += x
        mat[i].append(x)
for i in mat:
    aux2 = 0
    for j in i:
        aux2 += j
    soma.append(aux2)
    
for h in range(3):
    for i in range(3):
        print(f'{mat[h][i]}', end=" ")
    print()
for i in range(len(soma)):
    print(f'A soma da linha {i} é: {soma[i]}')
print(aux, 'É a soma dos termos da matriz')
