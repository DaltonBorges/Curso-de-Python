'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')


#* Tuplas são IMUTÁVEIS
# lanche[1] = 'pastel'  #! ERRO! Python não permite
# print(lanche[1:])
# print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer {comida}.')

print('='*40)

for cont in range(0, len(lanche)): #? O mesmo resultado
    print(f'Eu vou comer {lanche[cont]}')
    
print('='*40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}' )
    
print('='*40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}' )
    
print('='*40)

print(sorted(lanche)) # Põe a tupla em ordem alfabética

print('Comi pra caramba!')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(a)
print(b)
print(c)

'''

pessoa = ('Dalton', 49, 'M', 89.90)
print(pessoa)