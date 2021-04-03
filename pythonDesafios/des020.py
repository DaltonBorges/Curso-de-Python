from random import shuffle

c1 = input("Primeiro nome: ")
c2 = input("Segundo nome: ")
c3 = input("Terceiro nome: ")
c4 = input("Quarto nome: ")
lista = [c1,c2, c3, c4]
shuffle(lista)

print("A ordem de apresentação será:\n{}".format(lista))
