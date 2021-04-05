
# Estrtutura condicional aninhada:
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

nome = str(input('Qual é o seu nome? '))
if nome == 'Dalton':
    print('Que nome bonito!')
elif nome == 'José':
    print("Que nome comum!")
elif nome in 'Ana Clara Maria Isabela':
    print('É um nome feminino bem comum.')
elif nome in 'Juvenal Gumercindo Onofre':
    print('Que nome tosco!')
else:
    print('E isso é nome?')
print('Tenha um bom dia, {}!'.format(nome))