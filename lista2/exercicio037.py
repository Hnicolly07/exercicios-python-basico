# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina

while True:
  saque = int(input('Valor de saque: '))
  if saque >= 10 and saque<=600:
    break
  print('O valor mínimo de saque é R$10,00 e o máximo é de R$600,00')

notas_100 = notas_50 = notas_10 = notas_5 = notas_1 = 0

while saque>0:
  if saque>=100:
    saque-=100
    notas_100+=1
  elif saque>=50:
    saque-=50
    notas_50+=1
  elif saque>=10:
    saque-=10
    notas_10+=1
  elif saque>=5:
    saque-=5
    notas_5+=1
  else:
    saque-=1
    notas_1+=1
print(f"Serão necessárias {notas_100} notas de 100, {notas_50} de 50, {notas_10} de 10, {notas_5} de 5 e {notas_1} de 1")