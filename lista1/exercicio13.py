# Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

custo = float(input("Custo: "))
acrescimo = float(input("Acréscimo: "))
print(f"Valor de venda: R${custo+(custo*(acrescimo/100)):.2f}")