# Faça um Programa que leia três números e mostre o maior deles.

nums = []

for _ in range(3):
    num = int(input('Digite um número: '))
    nums.append(num)

nums.sort()
print(f"Maior Número: {nums[0]}")