lista = []
lista_pares = []
soma = 0
for i in range(10):
    entrada = float(input('Digite algo a ser adicionado na lista:\n'))
    lista.append(entrada)
    soma += entrada
    if entrada % 2 == 0:
        lista_pares.append(entrada)
print(f'Valores lidos: {lista}')
print(f'Soma dos termos: {soma}')
print(f'Números pares: {lista_pares}')