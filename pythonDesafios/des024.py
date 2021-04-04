# Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra "Santo".

cidade = str(input('Digite o nome da sua cidade:\n')).strip()
print(cidade[:5].upper() == 'SANTO ')