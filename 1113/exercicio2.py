def numero_char(texto):
    ref_arq = open("./1113/exercicio2.txt", 'w')
    numb_chars = 0
    for char in texto:
        if char != " ":
            numb_chars += 1
    ref_arq.write(f"{numb_chars}")
    ref_arq.close()


numero_char("o rennan é bem feraa")

def ler_char():
    ref_arq = open("./1113/exercicio2.txt", 'r')
    char = ref_arq.readline()
    return f"O número de caracteres presentes no texto é: {char}"

print(ler_char())