# 8 Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#* Ao final, mostre o conteúdo das três listas geradas.
#------------------------------------------------------

lista = []
listap = []
listai = []
while True:
    num = lista.append(int(input('Adicione o número: ')))
    segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    while segue not in 'SN':
        print('Opção inválida.')
        segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    if segue == 'N':
        break    
for i, v in enumerate(lista):
    if v % 2 == 0:
        listap.append(v)
    elif v % 2 == 1:
        listai.append(v)
print(f'Lista completa: {lista}.')
print(f'Lista de números pares: {listap}.')
print(f'Lista de números ímpares: {listai}.')


#? Resolvido em aula
#------------------------------------------------------