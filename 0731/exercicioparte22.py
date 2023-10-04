a = int(input('Digite o primeiro número\n'))
b = int(input('Digite o segundo número\n'))
aux = 0

if a > b:
    aux = b
    b = a
    a = aux

print(a,b)
