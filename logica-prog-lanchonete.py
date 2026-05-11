print('Lanchonete')
print('1 - Coxinha R$ 5,00')
print('2 - Pastel R$ 7,00')
print('3 - Café R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - Sair')

total = 0
while True:
  opcao = int(input('Por favor, informe qual item deseja comprar: '))

  if (opcao == 1):
    qtd = int(input('Por favor, informe a quantidade que deseja comprar: '))
    total += qtd * 5
  elif (opcao == 2):
    qtd = int(input('Por favor, informe a quantidade que deseja comprar: '))
    total += qtd * 7
  elif (opcao == 3):
    qtd = int(input('Por favor, informe a quantidade que deseja comprar: '))
    total += qtd * 4
  elif (opcao == 4):
    qtd = int(input('Por favor, informe a quantidade que deseja comprar: '))
    total += qtd * 6
  elif (opcao == 5):
    break
  else:
    print('Opção inválida')

print(f'O total a ser pago nesse pedido é R$ {total}')
