N = int(input('Digite o número de estações que existem:\n'))
C = int(input('Digite o número de comandos que o robo obedecerá\n'))
S = int(input('Digite o número da estação que houve problema\n'))
casa1 = 1 
contadorErro = 0
i = 0
if S == 1:
    contadorErro = contadorErro + 1

while i < C:
    comandos = int(input('Digite "1" para o robô avançar e "-1" para o robô regredir\n'))
    if comandos == 1 and casa1 >= 1:
        casa1 = casa1 + 1
        if casa1 > N:
            casa1 = 1
        if casa1 == S:
            contadorErro = contadorErro + 1

    elif comandos == (-1) and casa1 != 1:
        casa1 = casa1 - 1
        if casa1 == S:
            contadorErro = contadorErro + 1
    elif comandos == (-1) and casa1 == 1:
        casa1 = N
        if casa1 == S:
            contadorErro = contadorErro + 1
        
    i += 1
    

print(contadorErro)
