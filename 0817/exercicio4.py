i = 10
nVolta = 1
melhorTempo = 999999999
voltaMelhor = 0
aux = 0

while i != 0:
    volta = float(input(f'Digite o tempo da volta número {nVolta}\n'))
    nVolta += 1
    aux += volta
    if volta < melhorTempo:
        melhorTempo = volta
        voltaMelhor = nVolta
    i -= 1
print(f'O melhor tempo foi: {melhorTempo} segundos\n')
print(f'A volta do melhor tempo foi: {voltaMelhor}\n')
print(f'O tempo médio das 10 voltas foi: {aux/10} segundos\n')
