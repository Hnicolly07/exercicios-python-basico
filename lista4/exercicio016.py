# Escreva um programa em Python para encontrar o segundo maior elemento de uma lista com 20 números inteiros.
# OBS: todos os valores informados serão de valores diferentes e a solução não
# deve fazer este tratamento das entradas. Além disso, a solução não deve
# modificar a lista original com a ordem fornecida dos números.

nums = []
for i in range(20):
    num = int(input(f"Número {i+1}: "))
    nums.append(num)
# cria cópia da lista com fatiamento
copia_nums = nums.copy()
copia_nums = sorted(copia_nums)
segundo_maior = copia_nums[-2]

print(f"Segundo maior elemento: {segundo_maior}")
