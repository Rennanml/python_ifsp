x = 0
alunos = 0
menor = 10
maior = 0
aux = 0

while x >= 0:
    x = int(input('Digite a nota\n'))
    if x >=0:
        alunos += 1
        aux += x
    if x > maior:
        maior = x
    elif x < menor and x >= 0:
        menor = x

print(f'O número de alunos é: {alunos}\n')
print(f'A maior nota foi: {maior}\n')
print(f'A menor nota foi: {menor}\n')
print(f'A média geral da sala foi: {aux/alunos}\n')
