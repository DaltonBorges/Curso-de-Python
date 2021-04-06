# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#* À vista: dinheiro / cheque: 10% de desconto
#* À vista no cartão: 5% de desconto
#* em até 2x no cartão: preço normal
#* 3x ou mais no cartão: 20% de juros

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

valor = float(input('Valor do produto: '))
print('\033[33m='*40)
print('\033[33mÀ vista - dinheiro ou cheque: digite \033[36m1\033[m')
print('\033[33mÀ vista - no cartão: digite \033[36m2\033[m')
print('\033[33mEm até 2x no cartão: digite \033[36m3\033[m')
print('\033[33mEm 3x ou mais no cartão: digite \033[36m4\033[m')
print('\033[33m='*40)
forma = int(input('\033[mQual a forma de pagamento? '))
vistad = valor - (valor * 10 / 100)
vistac = valor - (valor * 5 / 100)
div3c = valor + (valor * 20 /100)
if forma == 1:
    print('Para pagamento à vista, em dinheiro ou em cheque, o valor fica em \033[32mR$ {:.2f}\033[m.'.format(vistad))
    print('='*70)
elif forma == 2:
    print('Para pagamento à vista, no cartão, o valor fica em \033[32mR$ {:.2f}\033[m.'.format(vistac))
    print('='*70)
elif forma == 3:
    print('Para pagamento em até 2x no cartão, o valor continua \033[32mR$ {:.2f}\033[m.'.format(valor))
    print('='*70)
elif forma == 4:
    print('Para pagamento em 3x ou mais no cartão, o valor total é de \033[32mR$ {:.2f}\033[m.'.format(div3c))
    print('='*70)


#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#