# Faça um Programa que peça as 4 notas bimestrais e mostre a média

soma = 0
for i in range (1,5):
    nota = float(input(f"nota {i}: "))
    soma += nota

media = soma/4

print(f"Sua média bimestral é {media:.1f}")
