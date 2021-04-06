# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    
#* Até 9 anos: MIRIM
#* Até 14 anos: INFANTIL
#* Até 19 anos: JÚNIOR
#* Até 20 anos: SÊNIOR
#* Acima: MASTER

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
from datetime import datetime

nasc = int(input('Digite o ano de nascimento: '))
hoje = datetime.now().year
idade = hoje - nasc
print('-=-'*15)
if idade <= 9:
    print('A idade é de \033[36m{} anos\033[m. A categoria é \033[36mMIRIM\033[m.'.format(idade))
elif idade > 9 and idade <= 14:
    print('A idade é de \033[34m{} anos\033[m. A categoria é \033[34mINFANTIL\033[m.'.format(idade))
elif idade > 14 and idade <= 19:
    print('A idade é de \033[32m{} anos\033[m. A categoria é \033[32mJÚNIOR\033[m.'.format(idade))
elif idade > 19 and idade <= 20:
    print('A idade é de \033[37m{} anos\033[m. A categoria é \033[37mSÊNIOR\033[m.'.format(idade))
else:
    print('A idade é \033[35macima de 20 anos\033[m. A categoria é \033[35mMASTER\033[m.')
    

#* Funcionou!    
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#