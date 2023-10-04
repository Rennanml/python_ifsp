print('Olá!! essa máquina fará a soma de todos os números que você inserir até que a entrada seja "0".')
i = 1
aux = 0
while i != 0:
    i = int(input('insira um número '))
    if i == 0:  
        print('O programa foi encerrado.')
        exit()
    aux += i
    print(aux)