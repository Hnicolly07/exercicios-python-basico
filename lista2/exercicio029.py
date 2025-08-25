# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% 
# Após o aumento ser realizado, informe na tela: o salário antes do reajuste e o percentual de aumento aplicado, o valor do aumento e o novo salário, após o aumento

salario = float(input('Salário: R$ '))
reajuste = 0

if salario <= 280:
    reajuste = 0.2
elif salario > 280 and salario <= 700:
    reajuste = 0.15
elif salario > 700 and salario <= 1500:
    reajuste = 0.1
else:
    reajuste = 0.05

aumento = salario*reajuste
salario_com_reajuste = salario + aumento

print()
print('-----------------------------------')
# alinha o texto na esquerda e completa com espaços pra formatação
print(f"{'SALÁRIO:':<25}R${salario:.2f}") 
print(f"{'REAJUSTE:':<32}{int(reajuste*100)}%")
print(f"{'AUMENTO:':<27}R${aumento:.2f}")
print(f"{'SALÁRIO COM REAJUSTE:':<25}R${salario_com_reajuste:.2f}")