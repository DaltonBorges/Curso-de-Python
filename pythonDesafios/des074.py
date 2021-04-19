# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#* Depois disso, mostre a listagem de números gerados e, também, indique o menor e o maior valor que estão na tupla.
#----------------------------------------------------

from random import randint

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
print(f'Números sorteados: {sorteio}')
print(f'O maior número foi {max(sorteio)}.')
print(f'O menor valor foi {min(sorteio)}')


#* Funcionou!
#----------------------------------------------------