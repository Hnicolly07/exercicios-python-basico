# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# •	o produto do dobro do primeiro com metade do segundo 
# •	a soma do triplo do primeiro com o terceiro
# •	o terceiro elevado ao cubo

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = float(input('Número 3: '))

print()
print('----------------------------------')
print(f"Resposta 1: {(2*num1)*(num2/2):.2f}")
print(f"Resposta 2: {(3*num1)+num3:.2f}")
print(f"Resposta 3: {num3**3:.2f}")