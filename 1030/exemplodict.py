# IGNORE = ' .,;:?!\t\n'
# def main():
#     frase = input('Digite uma frase: ')
#     letra = {}
#     for c in frase:
#         if c not in IGNORE:
#             if c in letra:
#                 letra[c] += 1
#             else:
#                 letra[c] = 1
#     print(letra)
#     keylist = list(letra.keys())
#     keylist.sort()
#     for i in keylist:
#         print(i, ": ", letra[i])



d1 = {"Joao": 10, "Maria":20}
d2 = d1.copy()
d2["Pedro"] = 30
d1["Joao"] = 40
print(d1)
# saída: {"Joao": 40,"Maria": 20}
print(d2)
# saída: {"Pedro": 30,"Joao": 10,"Maria": 20}


#Nesse exemplo, as listas sempre apontam o mesmo dado
d1 = {"Joao":[1,2], "Maria":[3,4]}
d2 = d1.copy()
d2["Pedro"]=[5,6]
d1["Joao"] += [3]
print(d1)
# saída: {"Joao": [1, 2, 3], "Maria": [3, 4]}
print(d2)
# saída{"Pedro": [5, 6],"Joao": [1, 2,3],"Maria": [3, 4]}  


#Limpar dics
idades = {"Joao":10, "Maria":12}
idadesCriancas = idades
idades.clear()
print(idades)
# saída: {}
print(idadesCriancas)
# saída: {}

idades = {"Joao":10, "Maria":12}
idadesCriancas = idades
idades={}
print(idades)
# saída: {}
print(idadesCriancas)
# saída: {"Joao":10, "Maria":12}



#Atributo Update
x = {"a":1, "b":2, "c":3}
y = {"z":9, "b":7}
x.update(y)
print(x)
# saída: {"a":1, "c":3, "b":7, "z":9}
x.update(a=7,c="xxx")
print(x)
# saída: {"a":7, "c":"xxx", "b":7, "z":9}



#Atributos pop
notas = {"Joao":[9.0,8.0], "Maria": [10.0]}
print(notas.pop("Joao"))
# saída: [9.0,8.0]
print(notas)
# saída: {"Maria":[10.0]}

notas = {"Joao":[9.0,8.0],"Maria":[10.0]}
print(notas)
# saída: {'Joao': [9.0, 8.0], 'Maria': [10.0]}
print(notas.popitem())
# saída: ("Maria":[10.0])
print(notas)
# saída: {"Joao":[9.0, 8.0]}


#Iterar as keys
notas = {"Joao":[9.0,8.0], "Maria":[10.0]}
for nome in notas:
    media = sum(notas[nome])/len(notas[nome])
    print("A média de ", nome, " é: ", media)
    
    
    
#Usar o dict para criar um dic através de tuplas
produtos = dict([(10, 4.5), (20, 5.99)])
valorProd = produtos[10]
print(valorProd)
# saída: 4.5
valorProd = produtos[20]
print(valorProd)
# saída 5.99



#Pegar as chaves e criar outra lista
dic1={}.fromkeys([2,3])
print("dic1=",dic1)
# saída: {2: None, 3: None}
dic2=dict.fromkeys(["Joao","Maria"],20) # Valor 20 vai como padrão
print("dic2=",dic2)
# saída: {"Joao": 20, "Maria": 20}


#Matriz com vários zeros
mat = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(mat.get((0,3)))
print(mat.get((1, 3), 0))



#Keys de tuplas
cad_pessoa={} #cria um dicionário vazio
cad_pessoa['12345678901']=('Maria da Silva', '09/07/1991', 'F', 'maria@gmail.com')
cad_pessoa.update({'98765432101':('Judite dos Santos', '25/04/1996', 'F',
'judite@gmail.com')})
# inclusão com variáveis
chave='23415678901'
tupla=('Manuel Oliveira', '07/03/1995', 'M', 'manuel@gmail.com')
cad_pessoa.update({chave:tupla})
for i in cad_pessoa:
    print(i,":",cad_pessoa[i],"\n")