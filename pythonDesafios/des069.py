# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#* A) Quantas pessoas têm mais de 18 anos.
#* B) Quantos homens foram cadastrados.
#* C) Quantas mulheres têm menos de 20 anos.

#----------------------------------------------------

cont = 0
fem = 0
masc = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    cont += 1
    if sexo == 'F':
        fem += 1
    if sexo == 'M':
        masc += 1
    segue = str(input('Deseja inserir mais cadastros? [S/N]')).strip().upper()[0]
    if segue == 'S':
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
        cont += 1

print('Fim')
