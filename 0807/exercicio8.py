N = int(input('Insira um número e veja seu fatorial\n'))
fatorial = 1
while N >= 1:
    fatorial =  fatorial * N
    N = N-1
print(fatorial)