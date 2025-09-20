# Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

qtd_acima_de_10 = 0
for i in range(4):
    for j in range(4):
        elemento = int(input(f'Elemento [{i+1}][{j+1}]: '))
        if elemento > 10:
            qtd_acima_de_10 += 1

print(f"A matriz possui {qtd_acima_de_10} elementos maiores que 10")