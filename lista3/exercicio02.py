# Escreva um programa que leia 10 números e informe o maior e o menor

num = float(input('Número 1: '))

maior_num = menor_num = num

for i in range(9):
    num = float(input(f"Número {i+2}: "))

    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num

print(f"Maior número: {maior_num}; Menor número: {menor_num}")