i = 1
menor = 10
maior = 0
aluno = 0

while i >= 0:
    i = int(input('Digite a nota do aluno:\n'))
    if i < 0:
        print(f'O número de alunos é: {aluno}\nA maior nota é: {maior}\nE a menor nota é: {menor}')
        exit()
    if i >= maior:
        maior=i
    elif i < menor and i >= 0:
        menor=i
    aluno +=1
print(f'O número de alunos é: {aluno}\nA maior nota é: {maior}\nE a menor nota é: {menor}')