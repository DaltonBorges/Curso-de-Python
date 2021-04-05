# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Oprograma vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# * Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou, então, o empréstimo será negado.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

print('\033[0;36m-=-\033[m'*20)
print('\033[32m     A N A L I S A D O R    D E    E M P R É S T I M O S\033[m')
print('\033[0;36m-=-\033[m'*20)
vcasa = float(input('Qual o valor do imóvel?: R$ \033[32m'))
vsal = float(input('\033[mQual é o salário mensal?: R$ \033[32m'))
nprest = int(input('\033[mEm quantos meses?: \033[33m'))
vprest = vcasa / nprest
vmin = 30 / 100 * vsal
print('\033[mO valor da prestação em \033[33m{}\033[m vezes é de \033[36mR$ {:.2f}\033[m'.format(
    nprest, vprest))
print('O valor mínimo para o pagamento em \033[33m{}\033[m vezes é de \033[36mR$ {:.2f}\033[m mensais'.format(
    nprest, vmin))
if vmin < vprest:
    print('O empréstimp foi \033[31mNEGADO\033[m.')
    print('\033[35mTente com mais prestações.\033[m')
else:
    print('O empréstimo foi \033[32mAPROVADO!\033[m')
    

# * Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
