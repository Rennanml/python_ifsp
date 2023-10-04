A = int(input('Digite a posição do carro A\n'))
B = int(input('Digite a posição do carro B\n'))
C = int(input('Digite a posição do carro C\n'))

if 0 >= A >= 500 or 0 >= B >= 500 or 0 >= C >= 500 or 0 >= D >= 500:
    print('O número não condiz com as restrições do exercício')
    exit()

if (B-A) < (C-B):
    print('1')
elif (B-A) > (C-B):
    print('-1')
elif (B-A) == (C-B):
    print('0')
        
