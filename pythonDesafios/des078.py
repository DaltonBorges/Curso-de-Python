# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#* No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
#----------------------------------------------

números = []
for num in range(0, 5):
    números.append(int(input('Digite um número: ')))
print(f'O valor máximo digitado foi {max(números)}')
print(f'O valor múnimo digitado foi: {min(números)}.')


#* Funcionou!
#----------------------------------------------
    
    
