# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
# Salário bruto
# Quanto pagou ao INSS
# Quanto pagou ao sindicato
# O salário líquido

valor_por_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou esse mês? '))

salario_bruto = valor_por_hora*horas_trabalhadas
inss = salario_bruto*(8/100)
sindicato = salario_bruto*(5/100)
imposto_de_renda = salario_bruto*(11/100)
salario_liquido = salario_bruto - inss - sindicato - imposto_de_renda 
print()
print('---------------------------')
print('          VALORES          ')
print('---------------------------')
print(f"Salário Bruto: {salario_bruto:.2f}")
print(f"INSS: {inss:.2f}")
print(f"Sindicato: {sindicato:.2f}")
print(f"Salário Líquido: {salario_liquido}")