# Crie um programa onde o usuário possa digitar cinco valores e cadastre-os numa lista, já na posição de inserção (sem usar o sort).
#* No final, mostre a lista ordenada na tela.

#---------------------------------------
lista = []
for c in range(0,5):
    num = int(input('digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
          if num <= lista[pos]:
              lista.insert(pos, num)
              print(f'Adicionado a posição {pos}.')
              break
          pos += 1
print('-='*30)
print(f'Lista ordenada: {lista}')

        
#? Resolvido em aula
#---------------------------------------