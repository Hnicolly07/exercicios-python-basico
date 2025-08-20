# Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

cotacao = float(input('Qual a cotação do dólar? '))
dolares = float(input('Quantos dólares você tem? '))

print(f"Você tem o equivalente a R${cotacao*dolares:.2f}")