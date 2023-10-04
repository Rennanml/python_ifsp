soma = 0
lista = []
contador_acima_media = 0

for i in range(7):
    print(f'Digite a temperatura do dia {i + 1}')
    temp = float(input())
    lista.append(temp)
    soma += temp

media = soma / 7

for j in lista:
    if j > media:
        contador_acima_media += 1
        
print(f'Apenas em {contador_acima_media} dias a temperatura foi acima da média! ({media})')
