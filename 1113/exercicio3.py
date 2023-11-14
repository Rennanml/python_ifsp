dic = {
    1: ["Camiseta", (19.99, 50)],
    2: ["Tênis", (49.99, 30)],
    3: ["Boné", (9.99, 100)],
}

def arquivar_dados():
    ref_arq = open("./1113/exercicio3.txt", 'w')
    for chave in dic:
        key = chave
        item = dic[chave][0]
        preco, qnt = dic[chave][1]
        linha = f'{key}\t{item}\t{preco}\t{qnt}\n'
        ref_arq.write(linha)
    ref_arq.close()

dic2 = {}
def mostrar_dados():
    ref_arq = open("./1113/exercicio3.txt", 'r')
    for linha in ref_arq:
        produto = linha.split("\t")
        key = produto[0]
        item = produto[1]
        preco = produto[2]
        qnt = produto[3]
        tuplinha = preco, qnt
        dic2[key] = [item, tuplinha]
    return dic2

print(mostrar_dados())

def inserir_produto(dic):
    try:
        key = int(input('Digite o número do código: '))
    except:
        return "O código digitado não é um número inteiro."
    keys = dic.keys()
    print(keys)
    if str(key) in keys:
        return "ERROR: O código já está na lista de produtos"
    else:
        item = input('Digite o nome do item: ')
        preco = float(input('Digite o preço do item: '))
        qnt = int(input('Digite a quantidade do produto: '))
        dic[key] = [item, (preco, qnt)]
        return "Produto adicionado com sucesso!"
    
print(inserir_produto(dic2))
print(dic2)
arquivar_dados()