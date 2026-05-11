lado1 = float(input('Por favor, informe o lado 1: '))
lado2 = float(input('Por favor, informe o lado 2: '))
lado3 = float(input('Por favor, informe o lado 3: '))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
  if lado1 == lado2 and lado2 == lado3:
    print('Triângulo equilátero')
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo isósceles')
  else:
    print('Triângulo escaleno')
else:
  print('Não é um triângulo')
