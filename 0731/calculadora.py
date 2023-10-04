print('Digite a operação que você deseja fazer: (soma, subtracao, divisao ou multiplicacao)')
operation = input()
if operation == 'soma':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 + numero2
    print('O resultado da soma é:',resultado)
if operation == 'subtracao':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 - numero2
    print('O resultado da subtração é:',resultado)
if operation == 'divisao':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 / numero2
    print('O resultado da divisão é:',resultado)
if operation == 'multiplicacao':
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    resultado = numero1 * numero2
    print('O resultado da multiplicação é:',resultado)

    