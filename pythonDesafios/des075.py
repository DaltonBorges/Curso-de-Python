# Desenvolva um programa que leia quatro números pelo teclado e guarde-os e uma tupla. No final, mostre:
#* A) Quantas vezes apareceu o valor 9.
#* B) Em que posição foi digitado o primeiro valor 3.
#* C) Quais foram os números pares.
#----------------------------------------------------

num = (int(input('Primeiro número: ')),
        int(input('Segundo número: ')),
        int(input('Terceiro número: ')),
        int(input('Quarto número: ')))
print(f'Valores digitados: {num}')
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) +1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print(f'Números pares digitados:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

        
#? Resolvido
##----------------------------------------------------