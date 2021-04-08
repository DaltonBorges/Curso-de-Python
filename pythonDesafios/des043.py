# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre o seu status, de acordo com a tabela abaixo:

#* Abaixo de 18.5: Abaixo do peso
#* Entre 18.5 e 25: Peso ideal
#* 25 até 30: Sobrepeso
#* 30 até 40: Obesidade
#* Acima de 40: Obesidade mórbida

#! Como calcular IMC ?
#¨ imc = peso / (altura ** 2)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#


peso =float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura ** 2)
print ('O IMC é de \033[33m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print ('Você está \033[4;36mabaixo do peso\033[m ideal')
elif imc >= 18.5 and imc <= 25:
    print('Você está com o \033[4;32mpeso ideal\033[m.')
elif imc > 25 and imc <=30:
    print('Você está \033[4;33macima do peso\033[m.')
elif imc > 30 and imc <= 40:
    print('Você está \033[4;31mobeso(a)\033[m.')
elif imc > 40:
    print('Você está com \033[4;35mobesidade mórbida\033[m.')
  

#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
