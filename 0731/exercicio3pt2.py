print('Responda se as portas estão na posição 1 ou 0\n')
portaP = int(input('Qual a posição da porta "P"?\n'))

if portaP == 0:
    print('A bolinha chegou no destino C\n')
    exit()
portaR = int(input('Qual a posição da porta "R"?\n'))
if portaP == 1:
    if portaR == 0:
        print('A bolinha chegou no destino B\n')
    elif portaR == 1:
        print('A bolinha chegou no destino A\n')
