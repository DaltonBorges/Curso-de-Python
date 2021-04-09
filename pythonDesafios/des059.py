# Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''
# Seu programa deverá realizar a operação solicitada em cada caso.

#-------------------------------------------------------
from time import sleep
option = 0
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
while option != 5:
    print('''Opções:
        ------------------------
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Encerrar o programa.
        ------------------------''')
    option = int(input('Digite a opção desejada: '))
    if option == 1:
        soma = v1 + v2
        print(('{} + {} = {}.'.format(v1, v2, soma)))
    elif option == 2:
        mult = v1 * v2
        print(' {} x {} = {}.'.format(v1, v2, mult))
    elif option == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
            print('O maior valor entre {} e {} é o {}.'.format(v1, v2, maior))
    elif option == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Digite o primeiro valor: '))
        v2 = int(input('Digite o segundo valor: '))  
    elif option == 5:
        print('Finalizando...')
        sleep(1)            
    else:
        print('Opção inválida. Tente novamente.')
    print('-'*40)
print('Fim do programa.')

        
        
    

    
