# Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# D = (R+S)/2
# R = (A+B)**2 e S = (B+C)**2

a = int(input("Número A: "))
b = int(input("Número B: "))
c = int(input("Número C: "))

r = (a+b)**2
s = (b+c)**2

print(f"A expressão vale: {(r+s)/2}")