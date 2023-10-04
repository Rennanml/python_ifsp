text = input('Escreva um texto:\n')
encontrar = input('Escreva a letra que deseja encontrar:\n')
j = 0
posicao = 0
for letra in text:
    posicao += 1
    if letra == encontrar:
        j = posicao
        
print(j)