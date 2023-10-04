A = int(input('Digite o primeiro número\n'))
B = int(input('Digite o segundo número\n'))
C = int(input('Digite o terceiro número\n'))
menor = 0
meio = 0
maior = 0

if A > B and A > C and B > C:
    print(f'A ordem correta é: {A} {B} e {C}')
    exit()

if B>A and B>C and A>C:
    maior = B
    menor = C
    meio = A
    A = maior
    B = meio
    C = menor
    print(f'{A}, {B} e {C}')
    exit()
if C>A and C>B and A>B:
    maior = C
    menor = B
    meio = A
    A = maior
    B = meio
    C = menor
    print(f'{A}, {B} e {C}')
    exit()
if C>A and C>B and B>A:
    maior =  C
    menor = A
    A = maior
    C = menor
    print(f'{A}, {B} e {C}')
    exit()
if A>B and A>C and C>B:
    maior = A
    menor = B
    meio = C
    A = maior
    B = meio
    C = menor
    print(f'{A}, {B} e {C}')
    exit()


        
