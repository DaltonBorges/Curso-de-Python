'''
teste = list()
teste.append('Dalton')
teste.append(49)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 35
galera.append(teste[:])
print(galera)
'''
'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# print(galera[0][0])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
    
'''

galera = []
dado = []
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f' {p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')