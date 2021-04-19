'''
num = (2, 5, 9, 1) 
num[2] = 3          #! ERRO, pois TUPLA é imutável
print(num)
'''

'''
num = [ 2, 5, 9, 1]
num[2] = 3          #* funciona com a LISTA
num.append(7)
# num.sort()
num.sort(reverse=True)
num.insert(2, 0)
#num.pop()
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não há número 4 na lista.')
print(num)
print(f'Essa lista tem {len(num)} elementos')
'''

'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
# for v in valores:
for c, v in enumerate(valores):
    print(f'Na posição {c}, temos {v}.')
print('Fim da lista')
'''


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
# for v in valores:
for c, v in enumerate(valores):
    print(f'Na posição {c}, temos {v}.')
print('Fim da lista')
'''

a = [2, 3, 4, 7]
# b = a           #? Cria uma ligação com a lista
b = a[:]        #? Cria uma cópia da lista
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''