# método normal:
#--------------------
# co = float(input("Comprimento do cateto oposto: "))
# ca = float(input("comprimento do cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)

# print("A hipotenusa do triângulo é {:.2f}".format(hi))

# Método por módulo
#---------------------
from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hi = hypot(co, ca)

print("A hipotenusa do triângulo é {:.2f}".format(hi))
