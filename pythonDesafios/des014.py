print('Conversão de graus Celcius para Fahrenheit')
print("="*20)
#* fim do cabeçalho

tc = float(input('Informe a temperatura em °C: '))
# tf = ((9*tc) / 5) + 32
tf = 9 * tc / 5 + 32     #* Neste caso, não porecisa dos parênteses, pois segue a precedência
print('A temperatura de {:.1f} C corresponde a {:.1f} F.'.format(tc, tf))