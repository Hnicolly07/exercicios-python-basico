# A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações

valor_compra = float(input("Valor compra: "))
print(f"5 prestações de R${valor_compra/5:.2f}")