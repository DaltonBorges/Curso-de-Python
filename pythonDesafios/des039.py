#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#* - Se ela ainda vai se alistar ao serviço militar,
#* - Se é hora de se alistar
#* - Se já passou o tempo de alistamento
# O programa também deverá mostrar o tempo que faltou ou o que passou do prazo.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
from datetime import datetime

nasc = int(input('Digite o ano de nascimento: '))
hoje = datetime.now().year
idade = hoje - nasc
print('-=-'*25)
if idade < 17:
    print('Você tem apenas \033[33m{} anos\033[m e vai poder se alistar no Serviço Militar ao completar 17 anos.'.format(idade))
    print('-=-'*25)
elif idade >= 17 and idade <=18:
    print('\033[mVocê tem \033[33m{} anos\033[me está na fase de alistamento militar. \033[32mAliste-se agora.\033[m'.format(idade))
    print('-=-'*25)
elif idade > 18:    
    print('\033[mVocê já tem \033[33m{} anos\033[m e \033[31mpassou do tempo\033[m de alistamento.'.format(idade))
    print('-=-'*25)
    

#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
