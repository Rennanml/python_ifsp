n = int(input('Digite o valor de N: '))
k = int(input('Digite o valor de K: '))
alunos = []
alunos2 = []
numeros_alunos = []
menor = 99999999999999999

for i in range(n):
    entrada_aluno = input('Digite o nome do aluno: ')
    alunos.append(entrada_aluno)

abc = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alunos)):
    contador = 0
    for w in abc:
        if alunos[i][0] != w:
            contador += 1
        else:
            numeros_alunos.append(contador)
            alunos2.append(alunos[i])
for j in range(len(numeros_alunos)):
    if numeros_alunos[j] < menor:
        menor = numeros_alunos[j]
        alunos[j] = alunos2[0]
        
n = len(alunos2)
for i in range(n):
    for j in range(0, n-i-1):
        if alunos2[j] > alunos2[j+1]:
            alunos2[j], alunos2[j+1] = alunos2[j+1], alunos2[j]
        
        
print(alunos2[k - 1])
