# CRie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

#---------------------------------------------------
cont = soma = 0
while True:
    num = int(input('Digite o número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Total de {cont} números digitados e a soma entre eles é: {soma}.')


#* Funcionou!
#¨ Conferido.
#---------------------------------------------------