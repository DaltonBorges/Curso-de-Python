# Escreva um programa que leia a velocidade de um carro.
#* Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado.
#* A multa vai custar R$ 7,00 por cada Km acima do limite.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# vel = float(input("Velocidade registrada no radar: Km/h"))
# mul = (vel - 80.0) * 7.0
# if vel > 80.0:
#     print('Você voi multado em R$ {:.2f}!'.format(mul))
# else:
#     print("Boa viagem! Dirija com segurança!")

#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#? Resoluçao (condição simples, sem o "else"):

velocidade = float(input("Qual é a velocidade atual do carro? "))
if velocidade > 80.0:
    print('Você excedeu o limite de permitido, que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você voi multado em R$ {:.2f}!'.format(multa))
print("Boa viagem! Dirija com segurança!") #* Apresenta a mensagem mesmo com a multa.