# import math
from math import sqrt, floor, ceil      #? selecionando itens da biblioteca

num = int(input('Digite um número: '))

#* Com a biblioteca inteira:
# raiz = math.sqrt(num) #? Chamando a biblioteca
# print('A raiz de {} é igual a {}'.format(num, raiz))
# print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# print('A raiz de {} é igual a {} (arredondada pra cima)'.format(num, math.ceil(raiz))) #? Chamando a biblioteca
# print('A raiz de {} é igual a {} (arredondada para baixo)'.format(num, math.floor(raiz))) #? Chamando a biblioteca

#* Com itens selecionados da biblioteca:
raiz = sqrt(num) #? Não precisa chamar a biblioteca
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {} (arredondada pra cima)'.format(num, ceil(raiz))) #? Não precisa chamar a biblioteca
print('A raiz de {} é igual a {} (arredondada para baixo)'.format(num, floor(raiz))) #? Não precisa chamar a biblioteca

