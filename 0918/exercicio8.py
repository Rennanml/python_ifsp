n = int(input('Digite o número de vezes (inteiro) que lerá um número: '))
lista = []
indice_encontrada = -1
maior = float("-inf")
for i in range(n):
    nmr = int(input('Digite um número (inteiro) para ser adicionado à lista: '))
    lista.append(nmr)
    
for j in range(len(lista)):
    if lista[j] > maior:
        maior = lista[indice_encontrada]
        indice_encontrada = j
print(f'O maior número é {lista[indice_encontrada]} que está no índice {indice_encontrada}')