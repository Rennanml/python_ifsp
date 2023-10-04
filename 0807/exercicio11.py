maioSeis = 0
EntreQuatroESeis = 0
menorQuatro = 0
i = 1

while i >= 0:
    i = int(input('Digite a nota do aluno:\n'))
    if i >= 6:
        maioSeis += 1
    elif i >=4 and i < 6:
        EntreQuatroESeis += 1
    elif i < 4 and i > 0:
        menorQuatro += 1
print(f'Maiores ou igual a 6: {maioSeis}\nEntre 4 e 6: {EntreQuatroESeis}\nMenor que 4: {menorQuatro}\n')