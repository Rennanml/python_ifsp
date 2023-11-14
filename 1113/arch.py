import os
def Existe_arquivo():
    import os
    if os.path.exists("arch.txt"):
        return True
    else:
        return False

dicionario = {
    '1': ('aluno 1', 'aluno1@ifsp'),
    '2': ('aluno 2', 'aluno1@ifsp'),
    '3': ('aluno 3', 'aluno1@ifsp'),
}

if len(dicionario):
    ref_arq = open("./1113/arch.txt", 'w')
    for aluno in dicionario:
        RA = aluno
        nome, email, = dicionario[aluno]
        linha = RA + "\t" + nome + "\t" + email + "\n"
        ref_arq.write(linha)
        print(linha)
    ref_arq.close()
    print("Arquivo gravado com sucesso!")

dic = {}
ref_arq = open("./1113/arch.txt", 'r')
for linha in ref_arq:
    linha = linha[:len(linha)-1]
    aluno = linha.split("\t")
    chave = aluno[0]
    nome = aluno[1]
    email = aluno[2]
    dic[chave] = [nome, email]
ref_arq.close()
print(dic)

dic2 = {}
ref_arq = open("./1113/arch.txt", 'r')
linha = ref_arq.readline()
while linha != "":
    linha = linha[:len(linha)-1]
    aluno = linha.split("\t")
    chave = aluno[0]
    nome = aluno[1]
    email = aluno[2]
    dic2[chave] = nome, email
    linha = ref_arq.readline()
ref_arq.close()
print(dic2)