entrada = ""
lista = []

while entrada != "fim":
    entrada = input('Digite uma string: ')
    lista.append(entrada)
    
x = input('Digite uma letra que deseja remover: ')

for i in range(len(lista)):
    if x in lista[i]:
        lista[i] = lista[i].replace(x, '', 1)
for string in range(len(lista)):
    if lista[string] == "":
        del(lista[string])
print(lista)
        