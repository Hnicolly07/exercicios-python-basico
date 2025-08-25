# Faça um programa que pergunte o preço de três produtos e informe qual produto você
# deve comprar, sabendo que a decisão é sempre pelo mais barato.

precos = {}

for i in range(3):
    precos[f"Produto {i+1}"] = float(input(f"Produto {i+1}: R$"))

menor_valor = precos["Produto 1"]
produto_mais_barato = 'Produto 1'

for produto, valor in precos.items():
    if valor < menor_valor:
        menor_valor = valor
        produto_mais_barato = produto

print(f"Compre o {produto_mais_barato} que custa R${menor_valor:.2f}")