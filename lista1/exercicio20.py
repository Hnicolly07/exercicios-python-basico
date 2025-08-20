# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = int(input('Valor A: '))
b = int(input('Valor B: '))

a, b = b, a # troca de valores

print()
print('------------------')
print('  NOVOS VALORES   ')
print('------------------')
print(f"VALOR A: {a}")
print(f"VALOR B: {b}")
