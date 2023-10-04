n = int(input('Digite o número de pessoas: \n'))
menor_altura = float("inf")
lista = []
indice_menor = 0
for i in range(n):
    alturas = float(input('Digite a altura respectiva à pessoa: \n'))
    lista.append(alturas)
    if alturas < menor_altura:
        menor_altura = alturas
        indice_menor = i
        
print(f'As alturas lidas foram: {lista}\n\
A menor altura foi: {menor_altura}\n\
que se encontrava no índice: {indice_menor}')