
#* importando o módulo:
#---------------------------------
# import math
# angulo = float(input("Qual é o ângulo?: "))
# seno = math.sin(math.radians(angulo))
# print("O ângulo de {} tem o seno de {:.2f}.".format(angulo,seno))
# cosseno = math.cos(math.radians(angulo))
# print("O ângulo de {} tem o cosseno de {:.2f}.".format(angulo,cosseno))
# tangente = math.tan(math.radians(angulo))
# print("O ângulo de {} tem a tangente de {:.2f}.".format(angulo,tangente))


#* importando itens da biblioteca:
#---------------------------------
from math import sin, cos, tan, radians
angulo = float(input("Qual é o ângulo?: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o seno de {:.2f}.".format(angulo,seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o cosseno de {:.2f}.".format(angulo,cosseno))
tangente = tan(radians(angulo))
print("O ângulo de {} tem a tangente de {:.2f}.".format(angulo,tangente))
