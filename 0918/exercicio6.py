n = int(input('Digite um número (inteiro) de vezes que o programa vai ler um número: '))
lista = []

for i in range(n):
    nmr = int(input('Leia um número (inteiro) que será adicionado a uma lista: '))
    lista.append(nmr)
x = int(input('Digite um número (inteiro) para saber se está ou não na lista: '))

saida = 'Não!'
for j in lista:
    if j == x:
        saida = 'Sim!'
        
print(saida)