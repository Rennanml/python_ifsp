text = input('Escreva seu texto:\n')
find = input('Escreva a letra que deseja encontrar:\n')
i = 0

for letra in text:
    if letra == find:
        i+=1
        
print(i)