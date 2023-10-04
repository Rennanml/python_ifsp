n = int(input('Digite o valor de N: '))
lista = []
for i in range(n):
    nmr = int(input('Digite um número: '))
    lista.append(nmr)
    
x = int(input('Digite um número: '))

j = 0
while j < len(lista):
    if lista[j] == x:
        del(lista[j])  
    else:
        j += 1
print(lista)