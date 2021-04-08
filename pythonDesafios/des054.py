# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores (considere a maioridade com 21 anos).

from datetime import date
maior = 0
menor = 0
atual = date.today().year
for pess in range(1, 8):
    nasc = int(input("Data de nascimento da {}ª pessoa: ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é \033[32mMAIOR\033[m de idade.')
        maior += 1
    else:
        print('Essa pessoa é \033[33mMENOR\033[m de idade.')
        menor +=1
print('Total de pessoas maiores de idade: {}'.format(maior))
print('Total de pessoas menores de idade: {}'.format(menor))
