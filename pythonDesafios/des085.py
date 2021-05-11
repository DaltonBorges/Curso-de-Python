# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e os valores ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#-------------------------------------------------

lista = [[],[]]
n = 0
for c in range (1,8):
    n = (int(input(f'Cadastrar o {c}º número:')))
    if n % 2 ==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os números cadastrados foram: {lista}')
print(f'Os números pares foram: {sorted(lista[0])}')
print(f'Os números ímapres foram: {sorted(lista[1])}')


#todo Resolvido na saída, mas o enunciado pedia uma lista única.
#-------------------------------------------------
