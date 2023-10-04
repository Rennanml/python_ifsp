text = input('Escreva um texto:\n')
encontrar = input('Escreva a letra que deseja eliminar:\n')
texto_final = ""

for letra in text:
    if letra != encontrar:
        texto_final += letra
        
print (texto_final)