# Crie um programa onde o usuário posa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidas todos os valores únicos digitados, em ordem crescente.
#----------------------------------------------

lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('Número adicionado com sucesso.')
    else:
        print('O número já s encontra na lista. Não será adicionado.')        
    segue = str(input('Deseja continuar? [S/N]')).strip().upper()                
    while segue not in 'SN':
        print('Opção inválida.')
        segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    if segue == 'N':
        break
print('-'*40)
print(f'Lista completa em ordem crescente:\n{sorted(lista)}.')


#* Funcionou!
#----------------------------------------------
