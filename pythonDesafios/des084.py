# faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#* A) Quantas pessoas foram cadastradas.
#* B) Uma listagem com as pessoas mais pesadas.
#* C) Uma listagem com as pessoas mais leves.

#--------------------------------------------

temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    while segue not in 'SN':
        print('Opção inválida.')
        segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    if segue == 'N':
        break
print('-'*40)
print(f'Dados cadastrados nesta sessão: {princ}.')
print(f'Total de cadastros: {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg.')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi de {menor}Kg.')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')
print()

#! Resolução não funcionou como deveria.