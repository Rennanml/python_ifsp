def inserir_reais_na_lista(n):
    for i in range(n):
        x = input('Digite um número Real para ser adicionado na lista: ')
        aux = Real(x)
        if aux:
            nmr_real = float(x)
            lista.append(nmr_real)
        else:
            print('O número digitado não é um número real!')
    return lista
        

def Real(x):
    numeros = '1234567890'
    dot_counter = 0
    for i in x:
        if i == ".":
            dot_counter += 1
    if dot_counter > 1:
        return False
    if x[0] == "-":
        for i in x[1:]:
            if i not in numeros and i != ".":
                return False
        return True
    for i in x:
        if i not in numeros and i != '.':
            return False
    return True       

lista = []
print(inserir_reais_na_lista(int(input('Digite o valor de n: '))))