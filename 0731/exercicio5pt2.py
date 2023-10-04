import math
A = float(input('Digite o valor de A\n'))
B = float(input('Digite o valor de B\n'))
C = float(input('Digite o valor de C\n'))

delta = (B ** 2) - 4 * A * C

if delta < 0:
    print('A equação não tem raízes reais pois o delta é menor que zero!\n')
    exit()
          
x1 = (-B + math.sqrt(delta)) / 2*A
x2 = (-B - math.sqrt(delta)) / 2*A

if delta == 0:
    print(f'A raíz da expressão é: {x1}.\n')
    exit()
elif delta > 0:
    print(f'As raízes da expressão são {x1} e {x2}.\n')
    exit()
