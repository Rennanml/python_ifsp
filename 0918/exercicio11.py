n = int(input('Digite o valor de N: '))
lista = []
contador = 0
nmr_encontrado = ""
mais_vezes = float("-inf")
for i in range(n):
    nmr = int(input('Digite um número: '))
    lista.append(nmr)
    
for j in lista:
    vezes = 0
    for h in lista:
        if h == j:
            vezes += 1
        if vezes > mais_vezes:
            mais_vezes = vezes
            nmr_encontrado = h
        
print(f'O elemento que mais apareceu foi: {nmr_encontrado}, que apareceu {mais_vezes} vezes...')