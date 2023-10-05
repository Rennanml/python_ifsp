#Função recursiva é aquela que "chama" ela mesmo


#Função normal
def somalista(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

L = [1, 3, 5, 7, 9]
S = somalista(L)
print(S)

#Função recursiva
def sum(lista):
    print(lista)
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sum(lista[1:]) #Essa chamada da lista faz com que a lista vá diminuindo
print(sum([1, 3, 5, 7, 9]))