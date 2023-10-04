lista_A = []
lista_impar = []
lista_par = []

for i in range(15):
    lista_A.append(float(input('Digite um número: ')))
for j in range(len(lista_A)):
    if lista_A[j] % 2 == 0:
        lista_par.append(lista_A[j])
    else:
        lista_impar.append(lista_A[j])
print(f'{lista_impar=}\n {lista_par=}')
