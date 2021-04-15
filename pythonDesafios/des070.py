# Crie um programa que leia o nome e o preço de vários produtos. O prpgrama deverá perguntar se o usuário vai continuar. No final, mostre:
#* A) Qual é o total gasto na compra.
#* B) Quantos produtos custam mais de R$ 1000.
#* C) Qual é o nome do produto mais menor.
#----------------------------------------------------

total = plus = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    while True:
        try:
            preço = float(input('Preço: R$ '))
            break
        except ValueError:
            print("Digite um valor numérico para p preço")
    cont += 1
    total += preço
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    if preço > 1000:
        plus += 1
    while resp not in 'SN':
        resp = str(input('Cadastrar mais produtos: {S/N} ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total da compra: \033[33mR$ {total:.2f}\033[m.')
print(f'Total de \033[36m{plus}\033[m produtos acima de R$ 1000,00')
print(f'O produto mais menor foi \033[32m{barato}\033[m, custando \033[33mR$ {menor}\033[m')


