# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
#* Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
#----------------------------------------------------

numext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze','Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente (apenas números entre 0 e 20).')
    print(f'Por extenso, o número digitado é: \033[33m{numext[num]}\033[m')
    print('·'*40)
    segue = str(input('Deseja continuiar? [S/N] '))
    


#* Funcionou!
#¨ Revisado
#----------------------------------------------------