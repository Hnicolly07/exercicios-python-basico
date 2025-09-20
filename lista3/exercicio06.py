# Faça um programa para calcular um valor A elevado a um expoente B.
# Os valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de repetição.

a = int(input('Digite o número A: '))
b = int(input('Digite o número B: '))
resultado = a

for _ in range(b-1):
    resultado *= a

print(f"O resultado é {resultado}")
