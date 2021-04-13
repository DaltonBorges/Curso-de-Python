# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#----------------------------------------------------

from random import randint

cont = 0
while True:
    comp = randint(0, 999)
    palpite = str(input('PAR ou ÍMPAR [P/I]? ')).strip().upper()
    num = int(input('Escolha um número: '))
    res = (num + comp) % 2
    print(f'Eu escolhi {comp} e você escolheu {num}.')
    if res == 0 and palpite in 'Pp':
        cont += 1
        print(f'{num + comp} é PAR! Você ganhou!')
    elif res != 0 and palpite in 'Ii':
        cont += 1
        print(f'{num + comp} é ÍMPAR! Ganhou!')
    elif res == 0 and palpite in 'Ii':
        print(f'{num + comp} é PAR! Você perdeu!')
        print(f'Você ganhou {cont} vezes.')
        break
    elif res != 0 and palpite in 'Pp':
        print(f'{num + comp} ÍMPAR! Você perdeu!')
        print(f'Você ganhou {cont} vezes.')
        break
print('>>>>> GAME OVER <<<<<')


#* Funcionou!
#----------------------------------------------------