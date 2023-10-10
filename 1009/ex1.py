def InteiroPositivo(n='-123b'):
    numeros = '1234567890'
    if n[0] == "-":
        return False
    for i in n:
        if i not in numeros:
            return False
    return True
print(InteiroPositivo())