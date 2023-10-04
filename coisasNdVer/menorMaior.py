print('Esse programa irá analisar os 3 números inseridos e irá falar qual é o maior')
nmr1 = int(input('Digite o primeiro número: '))
nmr2 = int(input('Digite o segundo número: '))
nmr3 = int(input('Digite o terceiro número: '))
if nmr1 > nmr2 and nmr1 > nmr3:
    print('O primeiro número é o maior.')
if nmr2 > nmr3 and nmr2 > nmr1:
    print('O segundo número é o maior.')
if nmr3 > nmr1 and nmr3 > nmr2:
    print('O terceiro número é o maior')    
    
