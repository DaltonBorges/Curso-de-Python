# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente, até ter um valor correto.


sexo = str(input('''Informe o sexo
---------------
[ M ] Masculino
[ F } Feminino
---------------\n''')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite novamente')).strip().upper()[0]
print('Seso {} registrado com sucesso'.format(sexo))
    