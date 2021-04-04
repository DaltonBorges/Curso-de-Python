# Deselvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por km, para viagens de até 200Km e R$ 0,45 para viagens mais longas.

dist = float(input("Qual é a distância da viagem? Km: "))
if dist <= 200:
    print('O valor da passagem é de R$ {:.2f}.'.format(dist * 0.50))
else:
    print("O valor da passagem é de R$ {:.2f}.".format(dist * 0.45))


#* Funcionou!