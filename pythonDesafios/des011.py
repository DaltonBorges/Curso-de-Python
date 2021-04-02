w = float(input('Largura da superfície: '))
h = float(input('Altura da superfície: '))
a = w * h
t = a / 2
print('Total da área: {} m².'.format(a))
print('Para uma parede de {} x {} metros, serão necessários {} litros de tinta.'.format(w,h,t))
