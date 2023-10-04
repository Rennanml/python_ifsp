n = int(input('Quantos termos terá sua lista? '))
lista = []
contador = 0
for i in range(n):
    nmr = int(input('Digite um número inteiro: '))
    lista.append(nmr)
x = int(input('Digite um número a ser procurado: '))
for j in range(len(lista)):
    if lista[j] == x:
        contador += 1
print(f'A letra {x} aparece {contador} vezes na lista.')