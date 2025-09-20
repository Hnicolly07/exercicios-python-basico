# Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. 
# Escreva ao ﬁnal a matriz obtida

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        if i == j: # Diagonal principal
            num = 1
        else:
            num = 0
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print(linha)