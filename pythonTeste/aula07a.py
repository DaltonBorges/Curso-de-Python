# nome = input('Qual é o seu nome? ')
# print('Olá, {:.^20}. É um prazer conhecer você!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
m = n1*n2
d = n1/n2
i = n1//n2
e = n1**n2

print('A soma é {}, a multiplicação é {}, \n a divisão é {:.3f} \n'.format(s,m,d,i,e, ),end='=>>>')
print('A divisão inteira é {}, exponencial é {}'.format(i, e))
