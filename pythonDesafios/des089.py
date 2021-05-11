# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
#------------------------------------

ficha =[]
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media ])
    segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    while segue not in 'SN':
        print('Opção inválida.')
        segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    if segue == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar as notas de qual aluno? (999 para interromper): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< FINALIZADO >>>')