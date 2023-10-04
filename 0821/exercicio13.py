# a) Todas as letras em maiúsculo;
# b) Somente a primeira letra em maiúsculo;
# c) Todas as iniciais em maiúsculo;
# d) Troque os espaços em branco do início por “#” ;
# e) Troque os espaços do final por “*”;
# f) Retire todos os espaços em branco do início e do fim;
# g) Mostre o índice da primeira ocorrência do caractere “a”:
# h) Mostre o índice da última ocorrência do caractere “a”;
# i) Mostre a quantidade de letras “e”;
# j) Mostre a inversão de todos os caracteres (maiúsculas/minúsculas).

string = ' Iracema - a lenda do Ceará ' 
print('a)', string.upper())
print('b)', string[1].upper())
print('c)', string[1].upper() + string[2:11] + string[11].upper() + string[12].upper() + string[13].upper() + string[14:])
print('d)', string[1 == '#'])
contador = 0
i = ""
while i != 'a':
    for i in string:
        contador += 1
        if i == 'a':
            i = contador
print (i)

