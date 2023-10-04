n = int(input('Digite o número de repetições que o laço terá: '))
lista = []

for i in range(n):
    nmr = int(input('Digite um número inteiro: '))
    lista.append(nmr)

print(lista[::-1])