# Melhore o jogo do desafio 028, onde o computador vai "pensar" em um número entre 0 a 10. Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#---------------------------------------

from random import randint
from time import sleep
comp = randint(0, 10)
qtd = 0
print('=' * 40)
print('Estou pensando em um número entre 0 e 10...')
sleep(1)
print('Ok! Já pensei! Você consegue adininhar?')
print('=' * 40)
acertou = False
while not acertou:
    player = int(input('Qual é o seu palpite? \033[32m'))
    qtd += 1
    if player == comp:
        acertou = True
    else:
        if player < comp:
            print('\033[36mMais!\033[m')
        elif player > comp:
            print('\033[36mMenos!\033[m')
print('\033[mVocê acertou com \033[33m{}\033[m palpites.'.format(qtd))