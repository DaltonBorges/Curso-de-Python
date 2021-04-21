# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, mostrará:
#* A) Quantos números foram digitados.
#* B) A lista deve ter valores ordenados de forma decrescente.
#* C) Se o valor 5 foi digitado e está ou não na lista.
#------------------------------------------------------

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    while segue not in 'SN':
        print('Opção inválida.')
        segue = str(input('Deseja continuar? [S/N]')).strip().upper()
    if segue == 'N':
        break
print(f'A lista decrescente de dígitos é: {sorted(lista, reverse=True)}.')
print(f'O total de números digitados foi {len(lista)}.')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não inserido na lista.')


#* Funcionou!
#------------------------------------------------------