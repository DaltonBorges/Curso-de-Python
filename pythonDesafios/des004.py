algo = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(algo))
print("É um número inteiro? {}".format(algo.isnumeric()))
print("É alfabético? {}".format(algo.isalpha()))
print("É alfanumérico? {}".format(algo.isalnum()))
print("É caixa alta? {}".format(algo.isupper()))
print("É capitalizada? {}".format(algo.istitle()))
print("É caixa baixa? {}".format(algo.isalpha()))
print("É um espaço? {}".format(algo.isspace()))



