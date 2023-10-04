n = int(input('Digite o número de vezes (inteiro) que lerá um número: '))
lista = []
indice_encontrada = -1

for i in range(n):
    nmr = int(input('Digite um número (inteiro) para ser adicionado à lista: '))
    lista.append(nmr)
    
x = int(input('Digite um número a ser procurado: '))
for j in range(len(lista)):
    if lista[j] == x:
        indice_encontrada = j
if indice_encontrada != -1:
    print(f'O número {x} foi encontrado na posição {indice_encontrada} da lista...')
else: 
    print(indice_encontrada)