# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o númeo solicitado for negativo.

#---------------------------------------------------
'''
while True:
    num = int(input('dígite um número para ver sua taubada: '))
    if num < 0:
        break
    print(f'\n Tabuada do {num}:')
    print(':'*15)
    print(f'{num} x {0:2} = {num * 0}')
    print(f'{num} x {1:2} = {num * 1}')
    print(f'{num} x {2:2} = {num * 2}')
    print(f'{num} x {3:2} = {num * 3}')
    print(f'{num} x {4:2} = {num * 4}')
    print(f'{num} x {5:2} = {num * 5}')
    print(f'{num} x {6:2} = {num * 6}')
    print(f'{num} x {7:2} = {num * 7}')
    print(f'{num} x {8:2} = {num * 8}')
    print(f'{num} x {9:2} = {num * 9}')
    print(f'{num} x {10:2} = {num * 10}')
    print(':'*15)
print('Programa encerrado.')

'''
#* Funcionou!
#---------------------------------------------------

#? Resolução:

while True:
    num = int(input('dígite um número para ver sua taubada: '))
    if num < 0:
        break
    print(f'\n Tabuada do {num}:')
    print(':'*15)
    for c in range(0, 11):
        print(f'{num} x {c:2} = {num * c}')
    print(':'*15)
print('Programa encerrado.')