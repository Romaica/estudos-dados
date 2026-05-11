# Questão 2
print('----------Seja bem vindo a Pizzaria da Romaica Bitencourt----------')
print('-----------------------------Cardápio------------------------------')
print('-------------------------------------------------------------------')
print('-----|  Tamanho  |  Pizza Salgada (PS)  |  Pizza Doce (PD)  |------')
print('-----|     P     |       R$ 30,00       |     R$ 34,00      |------')
print('-----|     M     |       R$ 45,00       |     R$ 48,00      |------')
print('-----|     G     |       R$ 60,00       |     R$ 66,00      |------')
print('-------------------------------------------------------------------')

# Declarar variaveis
total_pedido = 0

while True:

    preco = 0
    #Cliente informa o tipo de pizza que quer comprar
    tipo_pizza = input('Informe o tipo de pizza desejada, sendo PS (Pizza Salgada) ou PD (Pizza Doce): ')

    #Valida se informou os tipos aceitos
    while tipo_pizza != 'PS' and tipo_pizza != 'PD':
      print('Sabor de pizza inválido. \n')
      tipo_pizza = input('Informe o tipo de pizza desejada, sendo PS (Pizza Salgada) ou PD (Pizza Doce): ')

#-----------------------------Pizza Salgada-----------------------------#
    #Se o cliente informa o tipo de pizza PS entra aqui
    if tipo_pizza == 'PS':

    #Definição do tamanho da pizza para podermos atribuir o valor dela corretamente
      tamanho = input('Informe o tamanho desejado, para a sua pizza salgada, sendo P, M ou G: ')

      #Valida se o tamanho está dentro do que o exercício pede
      while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. \n')
        tamanho = input('Informe o tamanho desejado, para a sua pizza salgada, sendo P, M ou G: ')

      #Se ionforma um tamanho válido, entra aqui
      if tamanho == 'P':
        preco += 30
        print(f'Você escolheu uma pizza salgada de tamanho pequeno e o preço é R${preco} \n')

      elif tamanho == 'M':
        preco += 45
        print(f'Você escolheu uma pizza salgada de tamanho médio e o preço é R${preco} \n')

      elif tamanho == 'G':
        preco += 60
        print(f'Você escolheu uma pizza salgada de tamanho grande e o preço é R${preco} \n')

      total_pedido += preco

#-----------------------------Pizza Doce-----------------------------#

    #Se o cliente informa o tipo de pizza PD entra aqui
    elif tipo_pizza == 'PD':

    #Definição do tamanho da pizza para podermos atribuir o valor dela corretamente
      tamanho = input('Informe o tamanho desejado, para a sua pizza doce, sendo P, M ou G: ')

      #Valida se o tamanho está dentro do que o exercício pede
      while tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. \n')
        tamanho = input('Informe o tamanho desejado, para a sua pizza salgada, sendo P, M ou G: ')

      #Se ionforma um tamanho válido, entra aqui
      if tamanho == 'P':
        preco += 34
        print(f'Você escolheu uma pizza doce de tamanho pequeno e o preço é R${preco} \n')

      elif tamanho == 'M':
        preco += 48
        print(f'Você escolheu uma pizza doce de tamanho médio e o preço é R${preco} \n')

      elif tamanho == 'G':
        preco += 66
        print(f'Você escolheu uma pizza doce de tamanho grande e o preço é R${preco} \n')

      total_pedido += preco

    #Pede se o cliente quer pedir mais alguma coisa
    pedir_mais = input('Deseja pedir mais alguma coisa? Informe S ou N: ')

    #Se o cliente quer pedir mais alguma coisa entra aqui e repete o processo
    if pedir_mais == 'S':
      continue

    #Se o cliente não quer pedir mais alguma coisa entra aqui
    elif pedir_mais == 'N':
       break

print(f'O valor total a ser pago é R$ {total_pedido}')
