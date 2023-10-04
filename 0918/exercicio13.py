n = int(input('Digite o valor de N: '))
lista = []
y = 0
for i in range(n):
    nmr = int(input('Digite um número: '))
    lista.append(nmr)
    
x = int(input('Digite um número: '))

for j in lista[::-1]:
    if j == x and y == 0:
        del(lista[j])
        y += 1   
print(lista)