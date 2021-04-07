# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.

#--------------------------------------------------

print('·'*20)
print('Dez termos de P.A.')
print('·'*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
qtd = t + (10 - 1) * r
for pa in range(t, qtd + r, r):
    print(pa, end=' -> ')
print('FIM.')


#* Funcionou!
#---------------------------------------------------