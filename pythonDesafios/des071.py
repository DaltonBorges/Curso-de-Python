# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuários qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#* OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
#----------------------------------------------------

print('='*40)
print('>>>  C A I X A  E L E T R Ô N I C O  <<<')
print('='*40)

saque = int(input('Valor do saque: R$ '))
valor = saque
cédula = 50
qtd_céd = 0
while True:
    if valor >= cédula:
        valor -= cédula
        qtd_céd += 1
    else:
        print(f'Total de {qtd_céd} de R$ {cédula}.')
        if cédula == 50:
            cédula = 20
        elif cédula ==20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        qtd_céd = 0
        if valor == 0:
            break
            