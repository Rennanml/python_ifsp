idade = int(input('Digite sua idade:\n'))

if idade>=16 and idade<=17 or idade>65:
    print('O seu voto é facultativo!\n')
elif idade>=18 and idade<=65:
    print('O seu voto é obrigatório\n')
elif idade<16:
    print('Você ainda não pode votar!\n')

            
