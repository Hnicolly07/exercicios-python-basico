# Faça um Programa que leia 5 números inteiros, armazene-os em uma lista.

nums = []
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    nums.append(num)

print(nums)