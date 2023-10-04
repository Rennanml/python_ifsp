i = 0
auxAge = 0
auxB = 0
auxC = 0

while i < 10:
    age = int(input('Digite a idade\n'))
    kg = int(input('Digite o peso (em quilos)\n'))
    tamanho = int(input('Digite o tamanho (em centímetros\n)'))
    
    auxAge += age
    if kg > 90 and tamanho < 150:
        auxB += 1
    elif age < 30 and age > 10 and tamanho > 190:
        auxC += 1
    i += 1

print(f'A média das idade é: {auxAge/10}')
print(f'A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 m é: {auxB}')
print(f'a percentagem de pessoas com idade entre 10 e 30 anos que medem mais de 1,90 m é: {(auxC/100) * 10}')
