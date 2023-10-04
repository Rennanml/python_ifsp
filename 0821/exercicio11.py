text = input('Digite um texto\n')
vogal = "aeiouAEIOU"
space = " "
nv = 0
ns = 0

for letra in text:
    if letra in vogal:
        nv += 1
    elif letra == space:
        ns += 1
print(f'O número de vogais é: {nv} e o número de espaços é: {ns}\n')