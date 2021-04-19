# Crie um programa que tenha uma tupla única, com nome de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
#----------------------------------------------------

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
produtos = ('Lápis', 1.75, 'Caneta', 4.99, 'Caderno', 18.90, 'Borracha', 2.00, 'Régua', 3.45, 'Estojo', 10.80)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f' R$ {produtos[pos]:>6.2f}')
print('='*40)


#? Resolvido
#----------------------------------------------------
        