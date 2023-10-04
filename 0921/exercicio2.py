tipos_balas = int(input('Digite o número de tipos de balas que a empresa tem: '))
lista_rotulos = []
menor = 9999999

for i in range(tipos_balas):
    rotulos = int(input(f'Digite o número de rótulos que Aldo possui da bala número {i + 1}: '))
    lista_rotulos.append(rotulos)
for j in lista_rotulos:
    if j < menor:
        menor = j

print(menor)