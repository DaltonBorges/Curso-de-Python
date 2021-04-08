# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DA CONVERSÃO.
#* - 1 para Binário
#* - 2 para octal
#* - 3 para hexadeecimal
#* - 3 para hexadeecimal

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para a conversão:
---------------------------------
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL
---------------------------------''')
base = int(input('Digite a opção: '))
if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num,oct(num)[2:]))
elif base == 3:
    print('{} convertido em HEXADECIMAL é igual a {}.'.format(num,hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
