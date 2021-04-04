# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

#* Exemplo
#? Ana Maria de Souza
#? Primeira = Ana
#? Última = Souza

nc = str(input('Nome completo: ')).strip()
nome = nc.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[len(nome)-1]))