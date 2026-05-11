# Questão 1:
print('Seja bem vinda ao Sistema de Romaica Bitencourt')

valorBase =  float(input('Por favor, informe o valor base do plano de saúde: '))
idade = float(input('Por favor, informe a idade do cliente: '))

#Identificar o percentual será aplicado sobre o valor da mensalidade, partindo da idade informada
if idade > 0 and idade < 19:
  porcentagem = 100/100
elif idade >=19 and idade < 29:
  porcentagem = 150/100
elif idade >=29 and idade < 39:
  porcentagem = 225/100
elif idade >=39 and idade < 49:
  porcentagem = 240/100
elif idade >=49 and idade < 59:
  porcentagem = 350/100
else:
  porcentagem = 600/100
valorMensal = valorBase * porcentagem

print(f'O valor da mensalidade do plano de saúde é R${valorMensal}')
