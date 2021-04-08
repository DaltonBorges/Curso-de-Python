# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#* À vista: dinheiro / cheque: 10% de desconto
#* À vista no cartão: 5% de desconto
#* em até 2x no cartão: preço normal
#* 3x ou mais no cartão: 20% de juros
#* 3x ou mais no cartão: 20% de juros

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

print('{:=^40}'.format('| LOJAS BORGES |'))
valor = float(input('Valor da compra: '))
print('\033[33m='*35)
print('[ \033[36m1\033[m \033[33m] À vista / dinheiro ou cheque')
print('[ \033[36m2\033[m \033[33m] À vista - no cartão')
print('[ \033[36m3\033[m \033[33m] 2x no cartão')
print('[ \033[36m4\033[m \033[33m] 3x ou mais no cartão')
print('\033[33m='*35)
forma = int(input('\033[mQual a forma de pagamento? '))
if forma == 1:
    total = valor - (10 / 100 * valor)
elif forma == 2:
    total = valor - (5 / 100 * valor)
elif forma == 3:
    total = valor
    parc = total / 2
    print('Sua compra será parcelada em 2x de R$ { sem juros'.format(parc))
elif forma == 4:
    total = valor + (20 / 100 * valor)
    totparc = int(input('Quantas parcelas?: '))
    parc = total / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(totparc, parc))
else:
    total = valor
    print('\033[31mForma de pagamento inválida. Tente novamente, digitando a opção correta.\033[m')
        
print('Sua compra de R$ {} vai custar R$ {} no final.'.format(valor, total))


#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
