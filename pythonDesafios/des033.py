# Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

# ? Resolução:

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input("Digite mais um número: "))
# testando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# testando o maior
maior = a  # * pode ser feito com qualquer variável
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))
