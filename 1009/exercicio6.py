def Inteiro(n='-123553'):
    numeros = '1234567890'
    if n[0] == "-":
        for i in n[1:]:
            if i not in numeros:
                return False
        return True

    for i in n:
        if i not in numeros:
            return False
    return True

def receber_2_listas_int():
    aux = True
    while aux:
        x = input('Digite um valor inteiro para a lista 1: ')
        aux = Inteiro(x)
        if aux:
            lista1.append(x)
    aux = True
    while aux:
        y = input('Digite um número inteiro para a lista 2: ')       
        aux = Inteiro(y)
        if aux:
            lista2.append(y)

def Uniao():
    for i in lista1:
        lista_uniao.append(i)
    for i in lista2:
        if i not in lista_uniao:
            lista_uniao.append(i)
           
lista1 = []
lista2 = []
lista_uniao = []

print(receber_2_listas_int())
print(Uniao())
print(lista_uniao)