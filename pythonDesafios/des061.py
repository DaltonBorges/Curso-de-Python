# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão, usando a estrutura de repetição "while".

#--------------------------------------------------

print('·'*20)
print('Dez termos de P.A.')
print('·'*20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
while contador <= 10:
    print('{}'.format(termo), end='')
    print(' -> ' if contador < 10 else ' · ', end='')
    termo += razão
    contador += 1
print('FIM.')