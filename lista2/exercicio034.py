# Faça um programa que calcule as raízes de uma equação do segundo grau
# Fórmula geral: (a*(x**2)) + (b*x ) + c
# O programa deverá pedir os valores de a, b e c e fazer as consistências
# informando ao usuário as seguintes situações:
# A = 0 - Informar que equação não é do segundo grau e encerrar o programa
# Delta negativo - Informar que a equação não possui raízes e encerrar o programa
# Delta positivo - Informar as 2 raízes ao usuário
import sys
from math import sqrt

def main():
    a = int(input('Digite o valor de a: '))
    if a==0:
        print('A equação não é do segundo grau!')
        sys.exit(1) # encerrar o programa e retornar código 1 
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))

    nums = [a,b,c]

    delta = calcula_delta(nums)
    if delta>=0:
        print(f"As raízes da equação são: {calcula_raizes(nums,delta)}")
    else:
        print('Equação não possui raízes!')

def calcula_delta(valores):
              # b                 a          c
    return (valores[1]**2)-(4*valores[0]*valores[2])
    

def calcula_raizes(valores,delta):
    raiz1 = (-valores[1]+sqrt(delta))/(2*valores[0])
    raiz2 = (-valores[1]-sqrt(delta))/(2*valores[0])
    return raiz1,raiz2

main()