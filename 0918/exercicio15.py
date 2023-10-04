contador = 0
maior = 0
maior_string = ""
menor = float('inf')
menor_string = ""
lista = []
entrada = ""

while entrada != "fim":
    entrada = input('Digite uma string: ')
    lista.append(entrada)
    if len(entrada) > maior:
        maior_string = entrada
        maior = len(entrada)
    if len(entrada) < menor:
        menor_string = entrada
        menor = len(entrada)
print(f'A menor string é: {menor_string} e a maior string é: {maior_string}')
print(lista)