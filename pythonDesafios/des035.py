# Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

print('\033[0;36m-=-\033[m'*20)
print('\033[32m     A N A L I S A D O R    D E    T R I Â N G U L O S\033[m')
print('\033[0;36m-=-\033[m'*20)

r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[0;32mPODEM FORMAR\033[m um triângulo.')
else:        
    print('Os segmentos acima \033[0;31mNÃO PODEM FORMAR\033[m um triângulo.')

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#