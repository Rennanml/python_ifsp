lista_A = [1, 2, 3, 4, 5]
lista_B = [6, 7, 8, 9, 10]
lista_C = []
lista10 = []
soma_c = 0
for i in range(10):
    entrada = float(input('Digite um número: '))
    lista10.append(entrada)
lista_A += lista10[:4]
lista_B += lista10[5:]

for j in range(5):
    soma_a = lista_A[j]
    soma_b = lista_B[j]
    soma_c = soma_a + soma_b
    lista_C.append(soma_c)
    j += 1
print(f'Lista A: {lista_A}\n\
    Lista B: {lista_B}\n\
        Lista C: {lista_C}')
