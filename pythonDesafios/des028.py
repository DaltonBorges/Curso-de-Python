# Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuários tentar descobrir qual foi o número escolhido pelo computador.
# * O programa deverá escrever na tela se o usuário venceu ou perdeu.

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# import random
# num = [0, 1, 2, 3, 4, 5]
# ns = random.choice(num)
# print('Número sorteado: {}'.format(ns))
# usern = int(input('Adivinhe o número de 0 a 5: '))
# if usern == ns:
#     print('Parabéns! Você acertou e venceu!')
# else:
#     print('Infelizmente, você errou e perdeu. Tente novamente.')
# print("O número sorteado foi: {}".format(ns))

# * Funcionou!
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# ? Resolução:

from random import randint
comp = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5...')
print('Ok! Já pensei')
print('-=-' * 20)
# print('Número sorteado: {}'.format(comp))
player = int(input('Tente adivinhar o número: '))
if player == comp:
    print('Parabéns! Você acertou e venceu!')
else:
    print('Infelizmente, você errou e perdeu. Tente novamente.')
    print("Eu pensei no número {} e não no {}.".format(comp, player))
