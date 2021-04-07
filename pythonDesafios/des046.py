# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#---------------------------------------------------------

from time import sleep
for c in range(10, -1, -1): # o enunciado pede "indo de 10 até o 0" - Python ignora o último.
    print(c)
    sleep(1)
print('\033[33mFIM\033[m')

#* Funcionou!
#---------------------------------------------------------
