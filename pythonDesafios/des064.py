# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condiução de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

#---------------------------------------------------

num = cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('Foram digitados {} números e a soma entre eles foi de {}.'.format(cont, soma))
