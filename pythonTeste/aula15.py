'''
cont = 1
while cont <= 10:
    print(cont,'->', end='')
    cont += 1
print('Acabou.')
'''

'''
n = s =0
while n != 999:
    n= int(input('Digite um número: '))
    s += n
    # ENQUANTO não for digitado 999, o programa continua em looping
print('A soma vale {}.'.format(s))
'''

'''
n = s =0
while True:
    n= int(input('Digite um número: '))
    # ENQUANTO não for digitado 999, o programa continua em looping
    if n == 999:
        break   # para antes da soma
    s += n
# print('A soma vale {}.'.format(s))
#-------------------------------------
#* Nova forma de formatar (f string) - Python 3.6 
print(f'A soma vale {s}.')
#-------------------------------------
'''

nome = 'Dalton'
idade = 49
print(f'O {nome} tem {idade} anos.')

