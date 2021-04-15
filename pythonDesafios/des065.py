# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

#----------------------------------------------

resp = 'S'
cont = soma = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    cont += 1
    soma += num
    maior = num
    menor = num
    if cont == 1 :
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if resp not in "Ss" or resp not in "Nn":
        print('Valor inválido. Tente novamente.')
        num = int(input('Digite um número: '))
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]    
med = soma / cont
print('Quantidade de números digitados: {}.'.format(cont))
print('A média entre todos os valores é de {:.2f}.'.format(med))
print('O maior valor digitado foi: {}.'.format(maior))
print('O menor valor digitado foi: {}.'.format(menor))
    

