import os

def colher_dados(arquivo):
    sexo = input('Digite o sexo do(a) entrevistado(a) (m ou f): ').lower()
    idade = int(input('Digite a idade do(a) entrevistado(a): ')) 
    fuma = input('O(a) entrevistado(a) fuma? (sim ou não): ').lower()
    regiao = input('Digite a região que o(a) entrevistado(a) mora (sudeste, norte..): ')
    escolaridade = input('Digite o grau de escolaridade do(a) entrevistado(a): ')
    linha = f'{sexo}\t{idade}\t{fuma}\t{regiao}\t{escolaridade}\n'
    arquivo.write(linha)

def numero_mf():
    ref_arq = open('./1123/pesquisa.txt', 'r')
    m = 0
    f = 0
    for linha in ref_arq:
        if linha[0] == 'f':
            f += 1
        else:
            m += 1
    return (m, f)

def mf_fumantes():
    ref_arq = open('./1123/pesquisa.txt', 'r')
    fumante_feminino = 0
    fumante_homem = 0
    nfumante = 0
    for linha in ref_arq:
        campo = linha.strip().split('\t')

        if campo[2] == 'sim' and campo[0] == 'f':
            fumante_feminino += 1
        elif campo[2] == 'sim' and campo[0] == 'm':
            fumante_homem += 1    
        else:
            nfumante += 1
    return (fumante_homem, fumante_feminino)
ref_arq = open("./1123/pesquisa.txt", 'w')
menu = True
while menu:
    menu = input('Digite qualquer coisa para continuar ou "sair": ')
    if menu != 'sair':
        colher_dados(ref_arq)
        menu = True
    else:
        menu = False
ref_arq.close()  
mf = numero_mf()
print(mf)
fumantes = mf_fumantes()
total_entrevistados = mf[0] + mf[1]

porcentagem_homem_fumante = (fumantes[0] / total_entrevistados) * 100
porcentagem_mulher_fumante = (fumantes[1] / total_entrevistados) * 100

print(f'A porcentagem de homens fumantes é: {porcentagem_homem_fumante}%')
print(f'A porcentagem de mulheres fumantes é: {porcentagem_mulher_fumante}%')
