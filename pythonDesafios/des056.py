# Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final do programa mostre:
#* A média de idade do grupo.
#* Qual é o nome do homem mais velho.
#* Quantas mulheres têm menos de 20 anos.

#¨ Resolução: (esse foi foda)

somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0
for pess in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: M / F')).strip()#.upper()
    somaidade += idade
    if pess == 1 and sexo in 'Mm':  # 'in' Pode ser substituído por .upper() no input da string.
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média entre as idades é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadeh, nomevelho))
print('O total de mulheres com menos de 20 anos é de {}.'.format(totmulher20))

