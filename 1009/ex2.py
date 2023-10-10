def Inteiro(n='-123'):
    numeros = '1234567890'
    if n[0] == "-" or n[0] in numeros:
        for i in n:
            if i not in numeros:
                return False
        return True
print(Inteiro())