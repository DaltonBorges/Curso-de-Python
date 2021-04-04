# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Nome completo:\n')).strip()
print('O nome contém a palavra "Silva"?: {}'.format('silva' in nome.lower()))