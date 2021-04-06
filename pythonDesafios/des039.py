#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#* - Se ela ainda vai se alistar ao serviço militar,
#* - Se é hora de se alistar
#* - Se já passou o tempo de alistamento
# O programa também deverá mostrar o tempo que faltou ou o que passou do prazo.

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
from datetime import datetime

nasc = int(input('Digite o ano de nascimento: '))
print(''' Sexo:
      \033[32m----------------------
      [ m ] para masculino
      [ f ] para feminin
      ----------------------\033[m''')
sexo = str(input('Digite a opção: '))
# if sexo != 'm' and sexo != 'f':
    #print('Opção Inválida. Digite m ou f')  #! INCOMPLETO
hoje = datetime.now().year
idade = hoje - nasc
alista = nasc + 18
print('-x-'*20)
if sexo == 'f':
    print('\033[1;7;45m Mulheres estão dispensadas do Serviço Militar Obrigatório. \033[m')
elif idade < 17:
    dif = 18 - idade
    print('Você tem apenas \033[33m{} anos\033[m e deverá se alistar no Serviço Militar em \033[33m{} ano(s)\033[m.'.format(idade, dif))
    print('Seu alistamento será em \033[36m{}\033[m.'.format(alista))
    print('-=-'*25)
elif idade >= 17 and idade <=18:
    print('\033[mVocê tem \033[33m{} anos\033[me está na fase de alistamento militar. \033[32mAliste-se agora.\033[m'.format(idade))
    print('-=-'*25)
elif idade > 18:
    dif = idade - 18     
    print('Você já tem \033[33m{} anos\033[m e deveria ter se alistado há \033[33m{} ano(s)\033[m.'.format(idade, dif))
    print('Seu alistamento foi em \033[36m{}\033[m.'.format(alista))
    print('-=-'*25)
    

#* Funcionou!
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
