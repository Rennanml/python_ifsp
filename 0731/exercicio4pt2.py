livros = int(input('Qual a quantidade de livros que você deseja comprar?\n'))

A = 0.25 * livros + 7.5
B = 0.5 * livros + 2.5

if A > B:
    print('O critério que melhor se encaixa para sua situação é o B!\n')
elif B > A:
    print('O critério que melhor se encaixa para sua situação é o A!\n')
