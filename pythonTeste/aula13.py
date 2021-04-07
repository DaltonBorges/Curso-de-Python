#* Contador de 0 a 6 (sempre ignora o último - imprime de 10 a 5):

# for c in range(0, 6):
#     print('Oi!')
# print('FIM!')

#------------------------------------

#* Contador invertido, de 6 a 0 (sempre ignora o último imprime de 6 a 1)

# for c in range(6, 0, - 1):  #? -1 = quanto será tirado a cada laçada
#     print(c)
# print('FIM!')

#------------------------------------

#* Contador sequencial, de 0 a 6, contando de 2 em 2:

# for c in range(0, 7, 2):
#     print(c)
# print('FIM')

#------------------------------------

# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)

#------------------------------------

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# for c in range(i, f+1, p):
#     print(c)
# print('FIM')

#------------------------------------

# for c in range(0, 3):
#     n = int(input('Digite um valor: '))
# print('FIM.')

#------------------------------------

s = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os valores foi {}.'.format(s))