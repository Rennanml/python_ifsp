disciplinas = {}
dic_alunos = {}
def adicionar_aluno():
    ra = input('Digite o RA do aluno: ')
    nome = input('Digite o nome do aluno: ')
    nascimento = input('Digite a data de nascimento do aluno: ')
    email = input('Digite os emails do aluno: ').split(' ')
    x = True
    disciplina_notas = []
    while x:
        sigla = input('Digite a sigla da disciplina ou dê enter para parar: ')
        if sigla != "":
            nome_disciplina = input('Digite o nome da disciplina: ')
            carga_horaria = input('Digite a carga horária da disciplina: ')
            disciplinas[sigla] = [nome_disciplina, carga_horaria]
            nota = float(input(f'Digite a nota na disciplina {sigla}: '))
            key = (sigla, nota)
            disciplina_notas.append(key)
        else:
            x = False
        dic_alunos[ra, nome] = (nascimento, (email), disciplina_notas)
def alterar_Aluno(ra):
    for keys in dic_alunos:
        if ra in keys:
            dic_alunos.pop(keys)
            ra = input('Digite o novo RA do aluno : ')
            nome = input('Digite o novo nome do aluno: ')
            nascimento = input('Digite a nova data de nascimento do aluno: ')
            email = input('Digite os emails do aluno: ').split(' ')
            x = True
            disciplina_notas = []
            while x:
                sigla = input('Digite a sigla da disciplina ou dê enter para parar: ')
                if sigla != "":
                    nome_disciplina = input('Digite o nome da disciplina: ')
                    carga_horaria = input('Digite a carga horária da disciplina: ')
                    disciplinas[sigla] = [nome_disciplina, carga_horaria]
                    nota = float(input(f'Digite a nota na disciplina {sigla}: '))
                    key = (sigla, nota)
                    disciplina_notas.append(key)
                else:
                    x = False
                    return 0
                dic_alunos[ra, nome] = (nascimento, (email), disciplina_notas)
def remover_aluno(ra):
    for keys in dic_alunos:
        if ra in keys:
            aluno_removido = dic_alunos[keys][1] 
            dic_alunos.pop(keys)
            return aluno_removido
def consultar_um_aluno(ra, nome):
    key = ra, nome
    aluno_encontrado = dic_alunos.get(key)
    if aluno_encontrado:
        return key, aluno_encontrado
def mostrar_alunos():
    for key, info in dic_alunos.items():
        ra, nome = key
        print(f'Nome: {nome}\nRA: {ra}')
        data, pemails, pdisciplina_nota = info
        print(f"Data de nascimento: {data}")
        print('Emails: ')
        for i in pemails:
            print(i)    
        for disciplina, nota in pdisciplina_nota:
            print(f'Disciplina: {disciplina} Nota: {nota}')
def adicionar_disc_notas(ra):
    for key in dic_alunos:
        if ra in key:
            aux = True
            while aux:
                disciplina = input('Digite o nome da disciplina que deseja adicinar ou tecle enter para sair: ')
                if disciplina != "":
                    nota = input(f'Digite a nota na disciplina {disciplina}')
                    tuplinha = disciplina, nota
                    dic_alunos[key][2].append(tuplinha)
                else:
                    aux = False


aux = True
while aux:
    print('Menu: \n1-Adicionar aluno\n2-Alterar aluno\n3-Remover aluno\n4-Consultar um aluno pela chave completa\n5-Mostrar todos os alunos\n6-Adicionar disciplinas e notas ao aluno\n7-Fim')
    menu = int(input(' '))
    if menu == 1:
        adicionar_aluno()
    elif menu == 2:
        ra = input('Digite o RA do aluno que deseja alterar: ')
        if ra in list(dic_alunos.keys()):
            alterar_Aluno(input(ra))
        else:
            print('RA não encontrado.')
    elif menu == 3:
        aluno_removido = remover_aluno(input('Digite o RA do aluno a ser removido: '))
        print(f'Aluno {aluno_removido} removido.')
    elif menu == 4:
        if printar: 
            printar = consultar_um_aluno(input('Digite o RA do aluno a ser consultado: '), input('Digite o nome do aluno a ser consultado: '))
            print(printar)
            dados, info = printar
            ra, nome = dados
            print(f'Nome do aluno: {nome}\nRA do aluno: {ra}')
            data, email, diciplinas_notas = info
            print(f'Data de nascimento: {data}')
            print('Emails:')
            for emails in email:
                print(emails)
            for disciplina, nota in diciplinas_notas:
                print(f'Disciplina: {disciplina} Nota: {nota}')
        else: 
            print('Aluno não encontrado.')
    elif menu == 5:
        if dic_alunos != {}:
            mostrar_alunos()
        else:
            print('Dicionário vazio.')
    elif menu == 6:
        ra = input('Digite o RA do aluno para adicionar as diciplinas e notas: ')
        if ra in list(dic_alunos.keys()):   
            adicionar_disc_notas(ra)
        else:
            print('RA não encontrado.')
    elif menu == 7:
        print('Encerrando programa...')
        aux = False
