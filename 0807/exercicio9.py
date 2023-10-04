aux = 0
x = 1
while x > 0:
    x = int(input('Digite um número\n'))
    if x > aux:
        aux = x

print(aux)