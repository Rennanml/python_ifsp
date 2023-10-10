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
print(Inteiro())