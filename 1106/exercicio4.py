agenda = {
    
}

def incluirNovoNome(nome, telefones):
    agenda[nome] = telefones
def incluirTelefone(nome, telefone):
    if nome not in agenda:
        print('O nome não está na lista, deseja incluir?')
        yon = input('S ou N: ')
        if yon == 'S':
            agenda[nome] = telefone
    else:    
        agenda[nome].append(telefone)
def excluirTelefone(nome, telefone):
    if not agenda[nome]:
        del agenda[nome]
    else:
        agenda[nome].remove(telefone)
def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
    else:
        return "O nome não está na agenda!"
def consultarTelefone(nome):
    return agenda[nome]

incluirNovoNome("João", ["123-456-789", "987-654-321"])
incluirNovoNome("Maria", ["123-456-789", "987-654-321"])
incluirTelefone("João", "555-555-555")
excluirTelefone("João", "123-456-789")
excluirNome("Maria")
print(consultarTelefone("João"))
print(agenda)