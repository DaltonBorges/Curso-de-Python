# Crie um programa que leia o nome completo de uma pessoa e mostre:
#? O nome com todas as letras maiúsculas
#? O nome com todas as letras minúsculas
#? Quantas letras ao todo, sem considerar espaços
#? Quantas letras tem o primeiro nome

nome = str(input('Escreva seu nome completo:\n')).strip()
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}: '.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#* Outra maneira de fazer a última:
separa = nome.split()
print('Seu primeiro nome, {}, tem {} letras.'.format(separa[0], len(separa[0])))