# Condições Python

nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Dalton':
    print('Bonito nome!')
else:  #* indenteção NECESSÁRIA
    print("Que nome estranho!")
print('Bom dia, {}!'.format(nome))
