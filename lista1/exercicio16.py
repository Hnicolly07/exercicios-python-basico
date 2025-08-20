# Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês

nome = input("Nome: ")
salario = float(input("Salário: "))
vendas = float(input("Total de Vendas: "))
print()
print('----------------------------')
print(f"NOME: {nome}")
print(f"SALÁRIO FIXO: R${salario}")
print(f"SALÁRIO COM COMISSÃO: R${salario+(vendas*(15/100)):.2f}")