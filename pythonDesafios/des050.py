# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.


#-----------------------------------------------
s = 0
for num in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
print('·'*40)
print('A soma  de todos valores \033[4mpares\033[m é \033[1;32m{}\033[m.'.format(s))
print('·'*40)


#* Funcionou!!
#-----------------------------------------------