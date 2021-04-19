# Crie uma tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#* A) Apenas os 5 primeiros colocados.
#* B) Os últimos 4 colocados da tabela.
#* C) Uma lista com os times em ordem alfabética.
#* D) Em que posição na tabela está o time da Chapecoense.
#----------------------------------------------------

tabela = ('São Paulo', 'América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino','Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'Sport')

print('-'*40)
print('Os 5 primeiros colocados são:')
print(tabela[0:5])
print('-'*40)
print('Os 4 últimos colocados são:')
print(tabela[-4:])
print('-'*40)
print('Times em ordem alfabética:')
print(sorted(tabela))
print('-'*40)
'''
for p, c in enumerate(tabela):
    if c == 'Chapecoense':
        print(f'Chapecoense está na {p+1}ª posição  da tabela')
'''
#? Correção:
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')

       
#* Acho que fiz uma gambiarra, mas funcionou!
#----------------------------------------------------
