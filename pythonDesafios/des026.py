# Faça um programa que leia uma frase pelo teclado e mostre:
#? Quantas vezes aparece a letras "a"
#? Em que posição ela aparece a primeira vez
#? Em que posição ela aparece a última vez

frase = str(input('Escreva uma frase:\n')).strip().upper()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(frase.rfind('A')+1))