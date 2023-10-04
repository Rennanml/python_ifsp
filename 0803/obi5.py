#A entrada é composta por três linhas. A primeira linha é um inteiro R, o melhor
#resultado obtido por um atleta numa prova das Olimpíadas. A segunda linha é um
#inteiro M, o recorde mundial para essa prova. A terceira linha é um inteiro L, o recorde
#olímpico para essa prova. Para as provas desta tarefa, quanto menor o valor melhor o
#resultado.

R = int(input('Escreva qual foi o recorde do atleta na prova\n'))
M = int(input('Escreva qual é o recorde mundial da prova\n'))
L = int(input('Escreva qual é o recorde olímpico da prova\n'))

if R < M and R < L:
    print('RM\nRO')
elif R > M and R < L:
    print('*\nRO')
elif R < M and R > L:
    print('RM\n*')
elif R > M and R > L:
    print('*\n*')
elif R == M and R == L:
    print('*\n*')
