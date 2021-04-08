# Crie um programa que faça o computador jogar JOKENPÕ com você

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
from random import randint
from time import sleep

<<<<<<< Updated upstream
lista = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Escolha uma opção: 
    --------------
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ---------------''')
player = int(input("Digite a sua opção: "))
print('=' * 40)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÕ!!')
print('=' * 40)
print('Eu escolhi {} e você escolheu {}.'.format(lista[comp], lista[player]))
print('=' * 40)
if comp == player:
    print('EMPATAMOS! Vamos mais uma!')
elif comp == 0 and player == 1:
    print('PAPEL ebrulha a PEDRA. VOCÊ VENCEU!')
elif comp == 0 and player == 2:
    print ('PEDRA quebra a TESOURA. EU VENCI!')
elif comp == 1 and player == 0:
    print('PAPEL embrilha a PEDRA. EU VENCI!')
elif comp == 1 and player == 2:
    print('TESOURA corta PAPEL. VOCÊ VENCEU!')
elif comp == 2 and player == 0:
    print('PEDRA quebra TESOURA. VOCÊ VENCEU!')
elif comp == 2 and player == 1:
    print('Tesoura corta papel. EU VENCI!')
print('='*40)
=======
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
