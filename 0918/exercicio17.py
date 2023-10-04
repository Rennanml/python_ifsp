agenda =  []

menu = True
while menu:
    print('1 - Incluir novo contato \n')
    print('2 - Alterar um telefone \n')
    print('3 - Excluir um telefone \n')
    print('4 - Consultar os telefones de um contato \n')
    print('5 - Listar os contatos \n')
    print('6 - Sair \n')
    opc = input('Escolha uma opçaõ: ')
    if opc == '1':
        nome = input('Nome do contato: ')
        if nome in agenda:
            print('Candidato ja cadastrado!')
        else:
            tel = input('Telefone: ')
            while tel == '':
                tel = input('O contato precisa ter pelo menos um número')
            telefones = []
            telefones.append(tel)
            while tel != '':
                telefones.append(tel)
            agenda.append(nome)
            agenda.append(telefones)
        print(agenda)
    elif opc == '2':
        ...
    elif opc == '3':
        ...
    elif opc == '4':
        ...
    elif opc == '5':
        for indice in range(0, len(agenda), 2):
            print(f'\nNome: {agenda[indice]}')
            print('Telefones: ', end=" ")
            for tel in agenda[indice+1]:
                print(f'{tel} ', end=" ")
    elif opc == '6':
        menu = False