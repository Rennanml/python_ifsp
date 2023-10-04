#include <stdio.h>
#include <math.h>
#include <string.h>

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
vogais = 'aeiou'
consoante = ""

x = input('Digite a frase que deseja codificar:\n')

for encontrar_consoante in alfabeto:
     if encontrar_consoante not in vogais:
         consoante += encontrar_consoante
         

