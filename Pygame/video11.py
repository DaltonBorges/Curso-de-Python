class Cachorros:
    def __init__(self, nome, cor_de_pelo, idade, tamanho):
        self.nome = nome
        self.cor_de_pelo = cor_de_pelo
        self.idade = idade
        self.tamanho = tamanho

    def latir(self):
        print('Au au')
    def correr(self):
        print(f'{self.nome} correndo...')


cachorro_1 = Cachorros('Toby', 'Marrom', 5, 'Grande')

#print(cachorro_1.nome)
#print(cachorro_1.idade)
cachorro_1.idade = 8
cachorro_1.latir()
cachorro_1.correr()

cachorro_2 = Cachorros('Max', 'Preta', 3, 'Pequeno')
print(cachorro_2.tamanho)