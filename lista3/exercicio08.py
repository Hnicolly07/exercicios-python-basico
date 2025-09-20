# Faça um programa para:
# a) Ler um valor x qualquer
# b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100).

x = float(input('Digite o valor de x: '))
y=0
for i in range(100):
    y += (x+(i+1))

print(f"Y = {y:.2f}")
