num1 = int(input('Digite o primeiro número\n'))
num2 = int(input('Digite o segundo número\n'))

if num1 > num2:
    print(f"O primeiro número ({num1}) é o maior\n")
elif num2 > num1:
    print(f'O segundo número ({num2}) é o maior\n')
else:
    print("Os números são iguais\n")
