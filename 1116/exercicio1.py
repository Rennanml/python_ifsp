import os

dic = {
    "sc3038123": ("jorge", (10, 10, 10, 10))
}

def incluir_aluno():
    nome = input('Digite o nome do aluno: ')
    pront = input('Digite o prontuário do aluno no estilo(SC0000000): ')
    lista_notas = []
    i = 0
    while i < 4:
        nota = float(input(f'Digite a nota {i+1} do aluno: '))
        lista_notas.append(nota)
        i += 1
    dic[pront] = nome, lista_notas

dic_medias = {
        
    }
def calcular_medias():
    for aluno in dic.keys():
        media = sum(dic[aluno][1]) / 4
        dic_medias[aluno] = media
    return dic_medias
    
lista_rec = []
def recuperacao():
    for ra in dic_medias.keys():
        if dic_medias[ra] < 6:
            nome = dic[ra][0]
            lista_rec.append((nome, dic_medias[ra]))
    
def maior_media():
    alunos_maior_media = {}
    medias = dic_medias.values()
    nota_max = max(medias)
    for ra in dic_medias:
        if dic_medias[ra] == nota_max:
            alunos_maior_media[ra] = dic_medias[ra]   
    return alunos_maior_media        
        
incluir_aluno()
print(dic)
print(calcular_medias())
recuperacao()
print(lista_rec)
print(maior_media())