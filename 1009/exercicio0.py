escola = []
disciplinas = []
menu = True

def inserir_disciplina(nome_disciplina, disciplinas, escola):
    turma = []
    if nome_disciplina in disciplinas:
        print('Já existe uma disciplina com esse nome!')
    else:
        disciplinas.append(nome_disciplina)
        turma.append([])
        um_aluno = input("Digite ao menos um aluno para estar na lista dessa disciplina: ")
        idade_um_aluno = int(input(f'Digite a idade de {um_aluno}: '))
        turma[-1].append(um_aluno)
        turma[-1].append(idade_um_aluno)
        turma[-1].append([])
        while True:
            notas_um_aluno = float(input('Digite as notas do aluno até que um número negativo seja inserido: '))
            if notas_um_aluno < 0:
                break
            turma[-1][-1].append(notas_um_aluno)
        escola.append(turma)

def inserir_alunos(entrada, disciplinas):
    i_lista = None
    if entrada not in disciplinas:
        print('A disciplina digitada não foi encontrada!')
    else:
        i_lista = disciplinas.index(entrada)
        novo_aluno = input('Digite o nome do novo aluno: ')
        escola[i_lista].append([])
        escola[i_lista][-1].append(novo_aluno)
        idade_novo_aluno = int(input('Digite a idade do novo aluno: '))
        escola[i_lista][-1].append(idade_novo_aluno)
        escola[i_lista][-1].append([])
        while True:
            notas_novo_aluno = float(input('Digite as notas do novo aluno até que a entrada seja um número negativo: '))
            if notas_novo_aluno < 0:
                break
            escola[i_lista][-1][-1].append(notas_novo_aluno)

def remover_aluno(entrada, aluno, disciplinas, escola):
    if entrada in disciplinas:
        i_lista = disciplinas.index(entrada)
        nova_turma = []
        for turma in escola[i_lista]:
            if turma[0][0] != aluno:
                nova_turma.append(turma)
        escola[i_lista] = nova_turma
    else:
        print('A disciplina digitada não foi encontrada!')

def maior_media(disciplinas, escola):
    maior_media = -1
    for disciplina in escola:
        for turma in disciplina:
            for aluno in turma:
                notas_aluno = aluno[-1]
                if notas_aluno:
                    media_aluno = sum(notas_aluno) / len(notas_aluno)
                    if media_aluno > maior_media:
                        maior_media = media_aluno
    return maior_media

while menu:
    print("Opções:")
    print("1 - Inserir Disciplina")
    print("2 - Inserir Aluno em Disciplina")
    print("3 - Remover Aluno de Disciplina")
    print("4 - Mostrar Maior Média")
    print("5 - Sair")

    x = int(input("Digite uma opção (1-5): "))

    if x == 1:
        inserir_disciplina(input('Digite o nome da disciplina que deseja adicionar: '), disciplinas, escola)
    elif x == 2:
        inserir_alunos(input('Digite o nome da matéria a qual deseja adicionar um aluno: '), disciplinas)
    elif x == 3:
        disciplina = input('Digite o nome da disciplina onde o aluno está: ')
        aluno = input('Digite o nome do aluno que deseja remover: ')
        remover_aluno(disciplina, aluno, disciplinas, escola)
    elif x == 4:
        maior_media_valor = maior_media(disciplinas, escola)
        if maior_media_valor >= 0:
            print(f'A maior média entre todos os alunos é: {maior_media_valor:.2f}')
        else:
            print('Nenhum aluno com notas registradas.')
    elif x == 5:
        menu = False
    else:
        print("Opção inválida. Tente novamente.")
