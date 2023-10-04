import random

def teste():
    print('Isso é um teste!')

def soma(x, y):
    s = x + y
    j = x - y
    return s, j
    
print(2 + 4)
print('Olá!!')
teste()
# print(f'Soma: {round(soma(float(input()), float(input())), 2)}')
reult = soma(random(0, 100), random(0, 100))
print(reult)
print(f'{soma(1, 2)}')

