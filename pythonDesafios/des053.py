'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços (digitando sem acentuação).
* Exemplo:
 APOS A SOPA
 A SACADA DA CASA
 A TORRE DA DERROTA
 O LOBO AMA O BOLO
 ANOTARAM A DATA DA MARATONA
'''

#---------- Modo explícito: ----------
'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, '<=>', inverso)
if inverso == junto:
    print('{} é um palíndromo.'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))

'''
#---------- Modo simplificado: ----------

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, '<=>', inverso)
if inverso == junto:
    print('{} é um palíndromo.'.format(frase))
else:
    print('{} não é um palíndromo.'.format(frase))