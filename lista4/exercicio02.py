# Faça um Programa que leia 10 números reais e mostre-os na ordem inversa.

nums = []
for i in range(10):
    num = float(input(f"Número {i+1}: "))
    nums.append(num)

print(nums)

print(list(reversed(nums)))