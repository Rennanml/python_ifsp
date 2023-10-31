# class MeuExemplo:
#     def __init__(self, valor):
#         self.valor = valor

# objeto1 = MeuExemplo(33)
# objeto2 = MeuExemplo(49.5)
# objeto3 = MeuExemplo("Teste de Classe")
# objeto4 = MeuExemplo([2,6.7,"Lista em Classe"])

# print(objeto1.valor)
# print(objeto2.valor)
# print(objeto3.valor)
# print(objeto4.valor)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def saudacao(self):
        return f"Olá! meu nome é {self.nome} e tenho {self.idade} anos."
    
class Contato:
    nome = ""
    telefones = []
    
    def adicionar_telefone(self, nome, numeros):
        self.nome = nome
        self.telefones = numeros
        
    def alterar_nome(self, nome):
        self.nome = nome
        
    def alterar_telefones(self, numeros):
        self.telefones = numeros
        
    def exibir_contato(self):
        print(f'Nome: {self.nome}')
        if self.telefones != []:
            print('Telefones: ')
            for tel in self.telefones:
                print(f'{tel}', end="")
        else:
            print('Nenhum telefone registrado para este contato.')
class Agenda:
    contatos = []

    def incluir_contato(self, contato):
        self.contatos.append(contato)

    def buscar_contato(self, nome):
        for c in self.contatos:
            if nome == c.nome:
                return(c)
        return -1
    def excluir_contato(self, contato):
        for i in range(len(self.contatos)):
            if self.contatos[i] == contato:
                pos = i
        del self.contatos[pos]

menu = 0
while menu != 6:
    menu = int(input('Digite a opção: '))
    if menu == 1:
        ...
    