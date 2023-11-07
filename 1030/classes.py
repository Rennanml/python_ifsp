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
contatos = [] 

menu = 0
while menu != 6:
    print("Opções:")
    print("1. Adicionar contato")
    print("2. Exibir contato")
    print("3. Excluir contato")
    print("4. Alterar contato")
    print("5. Listar todos os contatos")
    print("6. Sair")

    menu = int(input('Digite a opção: '))

    if menu == 1:
        nome = input("Digite o nome do contato: ")
        contato = Contato(nome)
        contatos.append(contato)
        
    elif menu == 2:
        nome = input("Digite o nome do contato que deseja exibir: ")
        for contato in contatos:
            if contato.nome == nome:
                contato.exibir_contato()
                break
        else:
            print("Contato não encontrado.")
    
    elif menu == 3:
        nome = input("Digite o nome do contato que deseja excluir: ")
        for contato in contatos:
            if contato.nome == nome:
                contatos.remove(contato)
                print("Contato excluído com sucesso.")
                break
        else:
            print("Contato não encontrado.")
    
    elif menu == 4:
        nome = input("Digite o nome do contato que deseja modificar: ")
        for contato in contatos:
            if contato.nome == nome:
                novo_nome = input("Digite o novo nome: ")
                contato.alterar_nome(novo_nome)
                print("Nome alterado com sucesso.")
                break
        else:
            print("Contato não encontrado.")

    elif menu == 5:
        if contatos:
            print("Lista de Contatos:")
            for contato in contatos:
                contato.exibir_contato()
        else:
            print("Nenhum contato registrado.")
    
    elif menu == 6:
        print("Saindo do programa.")
    
    