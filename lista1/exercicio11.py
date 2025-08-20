# Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m

valor = float(input("Valor Depositado: "))
rendimento = valor*(0.7/100)
print(f"Rendimento após 1 mês: {rendimento:.2f}")
print(f"Valor Total: R${valor+rendimento}")