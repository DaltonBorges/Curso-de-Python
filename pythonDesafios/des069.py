# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#* A) Quantas pessoas têm mais de 18 anos.
#* B) Quantos homens foram cadastrados.
#* C) Quantas mulheres têm menos de 20 anos.

#----------------------------------------------------

cont = 0
fem = 0
masc = 0
maiores = 0
mulher_menor = 0
print('='*20)
print('> C A D A S T R O <')
print('='*20)
while True:
    # Leitura de dados:
    while True: 
        try:
            idade = int(input('Digite a idade: '))
            break
        except ValueError:
            print("Digite um número inteiro para a idade")
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    while sexo not in 'M/F':
        print ('Opção inválida. Digite M ou F para continuar.')
        sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    # Análise de dados solicitada:
    if idade >= 18:
        maiores += 1
    cont += 1
    if sexo == 'F':
        fem += 1
        if idade < 20:
            mulher_menor += 1
    elif sexo == 'M':
        masc += 1
    segue = str(input('Continuar cadastrando?? [S/N]')).strip().upper()[0]
    # Opção de seguir:
    while segue not in 'SN':
        print ('Opção inválida. Digite S ou N para continuar.')
        segue = str(input('Continuar cadastrando? [S/N]')).strip().upper()[0]
    if segue =='N':
        break
print('='*20)
print('R E L A T Ó R I O :')
print('='*20)
print(f'Total de pessoas cadastradas: \033[33m{cont}\033[m')
print(f'Total de \033[33m{maiores}\033[m pessoas com mais de 18 anos.')
print(f'Total de \033[33m{masc}\033[m homens cadastrados')
print(f'Total de \033[33m{mulher_menor}\033[m mulheres com menos de 20 anos.')


#* Funcionou!
#----------------------------------------------------