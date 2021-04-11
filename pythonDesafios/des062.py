# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
# ! A matemática já começou a foder...

# ----------------------------------------
print('·' * 20)
print('Dez termos de P.A.')
print('·' * 20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo), end='')
        print(' -> ' if contador < 10 else ' · ')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('PA finalizada com {} termos mostrados'.format(total))
print('Encerrando...')
