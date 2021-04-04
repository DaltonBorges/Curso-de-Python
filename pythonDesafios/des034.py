# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#* Para salários superiores a R$ 1.250.00, calcule um aumento de 10%.
#* Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Salário atual: R$ "))
if sal <= 1250.00:
    print('O valor do aumento é de R$ {:.2f}.'.format(sal + (15 / 100 * sal)))
else:
    print('O valor do aumento é de R$ {:.2f}.'.format(sal + (10 / 100 * sal)))

#* Funcionou!