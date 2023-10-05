n = int(input("Digite o número que deseja saber o fatorial: "))
aux = 1


while n != 1:
    aux *= n
    n -= 1
print(aux)