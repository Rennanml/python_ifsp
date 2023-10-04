text = input('Escreva um texto:\n')
encontrar = input('Escreva a letra que deseja eliminar na primeira ocorrência:\n')
i = 0
j = None
frase1 = ""
frase2 = ""
h = 0

for letra in text:
    i += 1
    if letra == encontrar:
            j = i
            frase1 = text[:j-1]
            frase2 = text[j:]
soma = frase1 + frase2
print(soma)
        