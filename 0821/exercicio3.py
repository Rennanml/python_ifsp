text = input('Escreva um texto:\n')
j = 0
for letra in text:
    if letra == " ":
        j += 1
print(j+1)