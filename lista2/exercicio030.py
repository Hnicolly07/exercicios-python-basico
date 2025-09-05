# Faça um programa para o cálculo de uma folha de pagamento
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês
# FGTS corresponde a 11%, mas não é descontado
# Sindicato corresponde a 3%
# Salário liquido = salário bruto - descontos
# Desconto Imposto de Renda:
# Até 900 - isento; Até 1500 - 5%; Até 2500 - 10%; Acima de 2500 - 20%
# Imprima na tela as informações

valor_hora = float(input('Quanto vale sua hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))

salario_bruto = valor_hora*horas_trabalhadas
if salario_bruto <= 900:
    imposto_de_renda = 0
elif salario_bruto <= 1500:
    imposto_de_renda = 0.05
elif salario_bruto <= 2500:
    imposto_de_renda = 0.1
else:
    imposto_de_renda = 0.2

inss = salario_bruto*0.1

descontos = inss + (salario_bruto*imposto_de_renda) + (salario_bruto*0.03)

salario_liquido = salario_bruto - descontos

print()
print('---------------------------------------')
print(f"{'SALÁRIO BRUTO:':<30}R${salario_bruto:.2f}")
print(f"{'IR:':<30}R${imposto_de_renda*salario_bruto:.2f}")
print(f"{'INSS (10%):':<30}R${inss:.2f}")
print(f"{'SINDICATO':<30}R${salario_bruto*0.03}")
print(f"{'FGTS (11%):':<30}{salario_bruto*0.11:.2f}")
print(f"{'TOTAL DE DESCONTOS:':<30}R${descontos:.2f}")
print(f"{'SALÁRIO LÍQUIDO:':<30}R${salario_liquido:.2f}")