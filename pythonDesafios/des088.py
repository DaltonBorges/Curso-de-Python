# Faça um programa que ajude um jogador de MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
#---------------------------------
from random import randint
from time import sleep

print('-' * 30)
print('   PALPITES MEGA SENA   ')
print('-' * 30)
jogos =[]
palpites =[]
tot = 1
qtd =int(input('Quantos palpites você quer? '))
while tot <= qtd:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    palpites.append(jogos[:])
    jogos.clear()
    tot += 1
print()
print('-.' * 3, f'Sorteando {qtd} jogos', '.-' * 3)
print()
for i, l in enumerate(palpites):
    sleep(.7)
    print(f'Palpite {i+1}: {l}')
print()
print('*'*10, 'Boa Sorte!', '*'*10)
    
#? Resolvido em aula
#---------------------------------