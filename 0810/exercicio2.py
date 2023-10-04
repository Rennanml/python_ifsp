soma = int(input('Qual a soma que você deseja?\n'))
num1 = int(input('Digite o primeiro número do intervalo desejado\n'))
num2 = int(input('Digite o segundo número do intervalo desejado\n'))

contador = 0

if num1 >= 1 and num1 <= 36 and num2 >= 1 and num2 <= 36:
    while num1 <= num2:
        a = num1 // 1 % 10
        b = num1 // 10 % 10
        if a + b == soma:
            contador += 1
        num1 += 1   
        
else:
    print('Número inválido\n')
    
print(contador)
