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
            xint = int(x)
            lista1.append(xint)
    aux = True
    while aux:
        y = input('Digite um número inteiro para a lista 2: ')       
        aux = Inteiro(y)
        if aux:
            yint = int(y)
            lista2.append(yint)
        

def Inter():
    for i in lista1:
        if i in lista2:
            lista_inter.append(i)
    
           
lista1 = []
lista2 = []
lista_inter = []

print(receber_2_listas_int())
print(Inter())
print(*lista_inter)