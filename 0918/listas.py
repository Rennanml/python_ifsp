import os

lista = []
for i in range(10):
    lista.append(input('Digite os elementos que irão entrar na lista\n'))
for j in range(len(lista)):
    print(f'Posição {j}: {lista[j]}')
for valor in lista:
    print(valor, end=" ")
