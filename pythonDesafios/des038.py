#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#* - O primeiro valor é maior  ou...
#* - O segundo valor é maior  ou...
#* - Não existe valor maior. os dois são iguais

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input('Digite o segundo valor: '))
if v1 > v2:
    print('O PRIMEIRO valor, ({}), é o maior'.format(v1))
elif v1 < v2:
    print('O SEGUNDO valor, ({}), é o maior'.format(v2))
else:
    print('Os dois valores são iguais.')

# * Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
