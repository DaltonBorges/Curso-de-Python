# Crie um programa que leia um número inteiro e mostre na tela se é PAR ou ÍMPAR.

num = int(input("Digite um número: "))
if num % 2 == 0:
    print('O número {}{}{} é \033[36mPAR\033[m!'.format('\033[33m',num,'\033[m'))
else:
    print('O número {}{}{} é \033[32mÍMPAR\033[m'.format('\033[33m', num ,'\033[m'))


#* Funcionou!