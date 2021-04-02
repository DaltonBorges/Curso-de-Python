print("AUGUEL DE CARROS")
print("="*20)
#* fim do cabeçalho

dias = int(input("Quantos dias alugado?: "))
km = float(input("Quantos Km rodados?: "))
tot = (60.0 * dias) + (0.15 * km)
print("O valor total a pagar é de R$ {:.2f}".format(tot))