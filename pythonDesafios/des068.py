# Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

#----------------------------------------------------

from random import randint

cont = 0
while True:
    comp = randint(0, 99)
    palpite = str(input('PAR ou ÍMPAR [P/I]? ')).strip().upper()
    while palpite not in 'PI':
        print('Opção inválida. Digite P ou I.')
        palpite = str(input('PAR ou ÍMPAR [P/I]? ')).strip().upper()
    while True: 
        try:    # Resolvido com Stack Overflow (não foi mostrado em aula)
            num = int(input('Escolha um número: '))
            break
        except ValueError:
            print("Não é um número!")
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

#? Resolução (não valida o número):
'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÌMPAR? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}.', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente!')
    '''