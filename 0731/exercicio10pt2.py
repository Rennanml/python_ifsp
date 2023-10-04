precoInicial = float(input('Digite o valor inicial da compra:\n'))
valorFinal = 0

if precoInicial <= 100:
    valorFinal = precoInicial * 0.95
elif precoInicial>100 and precoInicial<200:
    valorFinal = precoInicial * 0.9
elif precoInicial>=200:
    valorFinal = precoInicial * 0.8

print(f'O valor final a ser pago é: R${valorFinal}')
