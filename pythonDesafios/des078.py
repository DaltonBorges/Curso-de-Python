# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#* No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas cições na lista.
#----------------------------------------------
'''
números = []
for num in range(0, 5):
    números.append(int(input(f'Digite um número para a cição {num}: ')))
print(f'Os números digitados foram {números}.')
print(f'O vmaior valor digitado foi {max(números)}')
print(f'O menor digitado foi: {min(números)}.')

'''
#* Funcionou!
#todo Esqueci das cições!
#----------------------------------------------
    
#? Resolução:
'''
números = []
mai = 0
men = 0
for c in range(0, 5):
    números.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        mai = men = números[c]
    else:
        if números[c] > mai:
            mai = números[c]
        if números[c] < men:
            men = números[c]
print('-='*30)
print(f'Você digitou os valores {números}.')
print(f'O maior valor digitado foi o {mai} nas posições', end = ' ')
for i, v in enumerate(números):
    if v == mai:
        print(f'{i}...', end = ' ')
print(f'O menor valor digitado foi o {men} nas posições', end = ' ')
for i, v in enumerate(números):
    if v == men:
        print(f'{i}...', end = ' ')
print()
'''

#? Opção simplificada:

lista = []
posicao_maior = []
posicao_menor = []
for p in range(0, 5):
    val = int(input(f'Digite um valor na posição {p}: '))
    lista.append(val)
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)
    if valores == min(lista):
        posicao_menor.append(posicao)
print(f'Você digitou os valores {lista}')
print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')
