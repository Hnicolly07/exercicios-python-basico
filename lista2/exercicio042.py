# Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
# Até 5 Kg           Acima de 5 Kg 
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtd_morango = float(input('Deseja quantos Kgs de morango? '))
qtd_maca = float(input('Deseja quantos Kgs de maçã? '))

valor_pago = 0

if qtd_maca > 5:
    valor_pago += (qtd_maca*1.5) 
else:
    valor_pago += (qtd_maca*1.8)

if qtd_morango > 5:
    valor_pago += (qtd_morango*2.2)
else:
    valor_pago += (qtd_morango*2.5)

if qtd_morango+qtd_maca > 8 or valor_pago > 25:
    valor_pago -= (valor_pago*0.1)

print(f"Você comprou {qtd_maca+qtd_morango:.1f}Kgs de fruta, totalizando R${valor_pago:.2f}")