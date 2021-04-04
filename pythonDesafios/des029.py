# Escreva um programa que leia a velocidade de um carro.
#* Se ele ultrapassar 80km/h, mostra uma mensagem dizendo que ele foi multado.
#* A multa vai custar R$ 7,00 por cada Km acima do limite.

vel = float(input("Velocidade registrada no radar: "))
mul = (vel - 80.0) * 7.0
if vel > 80.0:
    print('Você voi multado em R$ {:.2f}!'.format(mul))

#* Funcionou!