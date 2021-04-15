while True:
  try:
    num = int(input('Escolha um número: '))
    break
  except ValueError:
    print("Não é um número!")

print(f'{num} é um número inteiro.')