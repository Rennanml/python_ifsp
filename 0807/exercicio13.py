x = int(input('Digite o valor de X\n'))

while x != 1:

    if x % 2 == 0:
        x = x / 2
        print(x)
    elif x % 2 != 0:
        x = 3 * x + 1
        print(x)