def ex4(a):
    if a > 0:
        j = 1
    elif a < 0: 
        j = -1
    else:
        j = 0
    return j

def ex5(string):
    i = len(string)
    return i

def ex6(frase):
    contador = 0
    for i in range(len(frase)):
        if (frase[i] == " ") and (frase[i + 1] != " "):
            contador += 1
    return contador + 1
def ex7(string):
    string.upper()
    string_invertida = string[::-1]
    if string_invertida == string:
        return "A palavra é um palíndromo"
    else:
        return "A palavra não é um palíndromo"
def ex8(x):
    contador = 0
    numeros = "1234567890"
    x = str(x)
    for i in range(len(x)):
        if x[i] in numeros:
            contador += 1
    return contador
def ex9(data):
    mes = ["_", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro" , "Outubro", "Novembro", "Dezembro"]
    mes_int = int(data[3] + data[4])
    string_formatada = data[:2] + " de " + mes[mes_int] + " de " + data[6:]
    return string_formatada
def ex10(numero):
    unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
    dezenas = ["", "Dez", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return "Onze" if numero == 1 else dezenas[1] + " e " + unidades[numero % 10]
    else:
        if numero % 10 == 0:
            return dezenas[numero // 10]
        else:
            return dezenas[numero // 10] + " e " + unidades[numero % 10]
def ex11(string1, string2):
    string_formatada = ""
    for i in range(len(string1)):
        string_formatada += string1[i] + string2[i]
    return string_formatada
def ex12(base, expoente):
    x = base ** expoente
    return x
def ex13():
    i = True
    lista = []
    x = None
    soma = 0
    while i:
        x = float(input('Digite um valor real.\nPara cancelar digite "0": '))
        if x != 0:
            lista.append(x)
        else: 
            i = False
    for i in lista:
        soma += i
    return soma 
def ex14():
    i = True
    lista = []
    x = None
    mult = 1
    while i:
        x = float(input('Digite um valor real.\nPara cancelar digite "0": '))
        if x != 0:
            lista.append(x)
        else: 
            i = False
    for i in lista:
        mult *= i
    return mult
def ex15():
    maior = 0
    indice = None
    lista = []
    i = True
    while i:
        x = float(input('Digite um número, caso queira sair digite "0": '))
        if x != 0:
            lista.append(x)
        else:
            i = False
            
    for i in range(len(lista)):
            if maior is None or lista[i] > maior:
                maior = lista[i]
                indice = i
    return lista, maior, indice
def ex16():
    lista = []
    i = True
    while i:
        x = float(input('Digite um número, caso queira sair digite "0": '))
        if x != 0:
            lista.append(x)
        else:
            i = False

    j = True
    while j:
        j = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                j = True
    return lista
def ex19():
    lista = []
    i = True
    while i:
        x = float(input('Digite um número, caso queira sair digite "0": '))
        if x != 0:
            lista.append(x)
        else:
            i = False

    j = True
    while j:
        j = False
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                j = True
    return lista
def ex17():
    lista = []
    i = True
    x = None
    soma = 0
    while i:
        x = float(input('Digite um número e caso queira sair digite "0": '))
        if x != 0:
            lista.append(x)
        else:
            i = False
    for i in lista:
            soma += i
    media = soma / len(lista)
    return media
def ex20(a, b):
    i = True
    for j in a:
        if j in b:
            continue
        else:
            return('Não é um anagrama!')
    return('É um anagrama!')
        
    
            
    
                    

def main():
    print(ex4(int(input("Digite um número inteiro: "))))
    print(ex5(input('Digite uma String: ')))
    print(ex6(input('Digite uma frase: ')))
    print(ex7(input('Digite uma palavra para verificar se é ou não um palíndromo: ')))
    print(ex8(int(input('Digite um número inteiro: '))))
    print(ex9(input('Digite sua data de nascimento no formato (DD/MM/AAAA): ')))
    print(ex10(int(input('Digite um número inteiro de 0 a 99:  '))))
    print(ex11(input('Digite uma string: '), input('Digite outra string: ')))
    print(ex12(int(input('Digite o valor da base: ')), int(input('Digite o valor do expoente: '))))
    print(ex13())
    print(ex14())
    print(ex15())
    print(ex16())
    print(ex17())
    # ex18()
    print(ex19())
    print(ex20(input('Digite uma palavra: '), input('Digite outra palavra: ')))
main()