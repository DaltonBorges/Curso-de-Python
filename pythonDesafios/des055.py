# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#¨ Resolução: 

for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))
    if pess == 1:   # Verifica aepnas o primeiro peso
        maior = peso
        menor = peso        
    else:           # Verifica os outros pesos
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} Kg.'.format(maior))
print('O menor peso lido foi de {} Kg.'.format(menor))
