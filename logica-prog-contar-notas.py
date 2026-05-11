valor = int(input('Digite o valor em R$: '))

while True:
  if valor >= 100:
    cont100 = valor // 100
    valor -= cont100 * 100
    print(f'Serão necessárias {cont100} de R$ 100,00')
    if not valor:
      break

  elif valor >= 50:
    cont50 = valor // 50
    valor -= cont50 * 50
    print(f'Serão necessárias {cont50} de R$ 50,00')
    if not valor:
      break

  elif valor >= 20:
    cont20 = valor // 20
    valor -= cont20 * 20
    print(f'Serão necessárias {cont20} de R$ 20,00')
    if not valor:
      break

  elif valor >= 10:
    cont10 = valor // 10
    valor -= cont10 * 10
    print(f'Serão necessárias {cont10} de R$ 10,00')
    if not valor:
      break

  elif valor >= 5:
    cont5 = valor // 5
    valor -= cont5 * 5
    print(f'Serão necessárias {cont5} de R$ 5,00')
    if not valor:
      break

  if valor:
    cont1 = valor
    print(f'Serão necessárias {cont1} de R$ 1,00')
  break
