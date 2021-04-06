# Refaça o DESAFIO 035, dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#* Equilátero: todos os lados iguais
#* Isósceles: dois lados iguais
#* Escaleno: Todos os lados diferentes

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

print('\033[0;36m-=-\033[m'*20)
print('\033[32m   A N A L I S A D O R    D E    T R I Â N G U L O S   II\033[m')
print('\033[0;36m-=-\033[m'*20)

r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[0;32mPODEM FORMAR\033[m um triângulo.')
if r1 == r2 and r1 == r3:
    print('O triângolo formado entre as retas medindo {}, {} e {} é EQUILÁTERO.'.format(r1, r2, r3))
elif r1 != r2 and r1 == r3 or r1 == r2 and r1 != r3: #! NÃO RESOLVIDO
    print('O triângulo formado entre as retas medindo {}, {} e {} é ISÓSCELES.'.format(r1, r2, r3))
elif r1 != r2 and r1 != r3 and r2 != r3:
    print('O triângulo formado entre as retas medindo {}, {} e {} é ESCALENO'.format(r1, r2, r3))
else:        
    print('Os segmentos acima \033[0;31mNÃO PODEM FORMAR\033[m um triângulo.')
    
    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#