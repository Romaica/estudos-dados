# Questão 3
print('Bem vindo a Madeireira da Lenhadora Romaica Bitencourt')
print('PIN - Tora de Pinho')
print('PER - Tora de Peroba')
print('MOG - Tora de Mogno')
print('IPE - Tora de Ipê')
print('IMB - Tora de Imbuia \n')

# Função que valida o tipo de madeira e apresenta o valor por m³
def escolha_tipo ():

  while True:
    madeira = input('Por favor, informe o tipo de madeira desejado: ')

    if madeira == 'PIN':
      valor = 150.49
      return valor

    elif madeira == 'PER':
      valor = 170.20
      return valor

    elif madeira == 'MOG':
      valor = 190.90
      return valor

    elif madeira == 'IPE':
      valor = 210.10
      return valor

    elif madeira == 'IMB':
      valor = 220.70
      return valor

    #entra aqui se informar um tipo válido
    else:
      print('Tipo de madeira inválido, por favor, digite novamente.\n')

# Função que define o tamanho da madeira e valida
def qtd_toras ():

  while True:
    # valida se a quantidade pode ser encomendada (inferior a 2.000)
    try:
      tamanho = int(input('Por favor, informe a quantidade de toras desejadas em m³: \n'))

      if tamanho >= 2000:
        print ('Quantidade de toras superior ao limite máximo permitido, verifique a quantidade informada. \n')
        continue

      if tamanho < 100:
        desconto = 0
      elif tamanho >= 100 and tamanho <500:
        desconto = 4/100
      elif tamanho >= 500 and tamanho <1000:
        desconto = 9/100
      elif tamanho >= 1000 and tamanho <2000:
        desconto = 16/100

      return tamanho, desconto

    # Se não informar um número entra aqui
    except ValueError:
      print('Por favor, informe um número.')

# Função que o tipo de transporte e valida
def transporte ():

  while True:
    try:
      tipo_transporte = int(input('Por favor, informe o tipo de transporte: \n'))
      print('1 - Transporte Rodoviário  - R$ 1.000,00')
      print('2 - Transporte Ferroviário - R$ 2.000,00')
      print('3 - Transporte Hidroviário - R$ 2.500,00')

      if tipo_transporte == 1:
        return 1000

      elif tipo_transporte == 2:
        return 2000

      elif tipo_transporte ==3 :
        return 2500

      else:
        print('Tipo de transporte inválido.\n')

    except ValueError:
      print('Informe um 1, 2 ou 3.\n')

    return tipo_transporte

#Programa Principal
valor_madeira = escolha_tipo()
quantidade, desconto = qtd_toras()
tipo_transporte = transporte()

total = ((valor_madeira * quantidade)*(1-desconto)) + tipo_transporte

print(f'O total do seu pedido é: R${total}')
