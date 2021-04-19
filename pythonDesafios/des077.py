# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#* Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.
#------------------------------------------------

palavras = ('Biscoito', 'Pizza', 'Carro', 'Forno', 'Coelho', 'Turma', 'Multa', 'Tropa', 'Rosa', 'Máscara', 'Fácil', 'Glúten')
for p in palavras:
    print(f'\nNa palavra {p} as vogais são: ', end = ' ')
    for letra in p:
        if letra.lower() in 'aáeéiíoóuú':
            print(letra, end =' ')
            

#? Resolvido em aula.
#------------------------------------------------