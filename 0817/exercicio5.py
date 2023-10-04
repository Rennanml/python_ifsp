soma = 0
x = 1
y = 1
conta = ""

while x <= 99 and y <= 50:
    soma += x/y
    x += 2
    y += 1
    conta += f'{x}/{y} + '
conta = conta [:-3]
print(f'1/1 + {conta}')
print(f'O resultado é: {soma}')
