lista = []
i = True
while i:
    x = float(input('Digite um número, caso queira sair digite "0": '))
    if x != 0:
        lista.append(x)
    else:
        i = False

j = True
while j:
    j = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            j = True
print(lista)