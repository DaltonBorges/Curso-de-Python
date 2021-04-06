# Crie um programa que faça o computador jogar JOKENPÕ com você

<<<<<<< Updated upstream
=======
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
from random import choice
from time import sleep

lista = (0, 2, 5)
comp = choice(lista)
player = int(input('''Escolha uma opção: 
                 --------------
                 [ 0 ] PEDRA
                 [ 2 ] TESOURA
                 [ 5 ] PAPEL
                 ---------------''', end=''))
if player != 0 or player != 2 or player != 5:
    print('Opção inválida. Reinicie o jogo.')
else:
    print('=' * 20)
    print('Jo KEN...')
    sleep(2)
    print('PÕ!')
    print('=' * 20)
    print (' Eu escolhi {} e você escolheu {}.'.format(comp, player))
    if comp == player:
        print('EMPATAMOS! Vamos mais uma!')
    elif comp == 0 and player ==2:
        print('Pedra quebra a tesoura. EU VENCI!')
    elif comp == 0 and player == 5:
        print ('Papel embrulha a pedra. VOCÊ VENCEU!')
    elif comp == 2 and player == 0:
        print('Pedra quebra tesoura. VOCÊ VENCEU!')
    elif comp == 2 and player == 5:
        print('Tesoura corta papel. EU VENCI!')
    elif comp == 5 and player == 0:
        print('Papel embrulha pedra. EU VENCI!')
    elif comp == 5 and player == 2:
        print('Tesoura corta papel. VOCÊ VENCEU!')
>>>>>>> Stashed changes
