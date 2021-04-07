# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um LAÇO FOR.

#----------------------------------------------------------

num = int(input('dígite um número para ver sua taubada: '))
print('\n Tabuada do {}:'.format(num))
print('·'*15)
for tab in range(0, 11):
    print('{} x {:2} = {}'.format(num, tab , num * tab))
print('·'*15)    

#* Funcionou!
#-----------------------------------------------------------


