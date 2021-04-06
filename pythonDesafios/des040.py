# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#* Média abaixo de 5.0 : REPROVADO
#* Média entre 5.0 e 6.9 : RECUPERAÇÃO
#* Média 7.0 ou superior : APROVADO

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

n1 = float(input("Primeira nota: "))
n2 = float(input('Segunda Nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Sua média foi {}. Aluno \033[31mREPROVADO.\033[m'.format(m))
    print('Estude mais no próximo ano!')
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {}. Aluno em \033[33mRECUPERAÇÃO.\033[m'.format(m))
    print('Ainda há tempo de se esforçar! Concentre-se!')
elif m > 7.0:
    print('Sua média foi {}. Aluno \033[32mAPROVADO!\033[m'.format(m))
    print('Parabéns! Continue assim!')
print("BONS ESTUDOS!")


#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
