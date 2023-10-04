name = input('Escreva seu nome\n')
aux = ""

for i in range(len(name) -1, -1, -1):
    aux+=name[i]
print(aux.upper())
