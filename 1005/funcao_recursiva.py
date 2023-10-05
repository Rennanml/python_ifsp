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

#Quando chamamos a própria lista no return, os resultados vão "empilhando", nesse exemplo os valores que se empilhão são: 
#1, 3, 5, 7, 9 respectivamente, no final há a soma.

"""
º Um algoritmo recursivo deve ter um caso básico (critério de
parada)
º Um algoritmo recursivo deve mudar o seu estado e se
aproximar do caso básico
º Um algoritmo recursivo deve chamar a si mesmo,
recursivamente
"""


