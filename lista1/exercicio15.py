# Escreva um programa que leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:
# D = (R+S)/2
# R = (A+B)**2 e S = (B+C)**2

def main():
    a = ler_numero('Número A (inteiro e positivo): ')
    b = ler_numero('Número B (inteiro e positivo): ')
    c = ler_numero('Número C (inteiro e positivo) ')

    r = (a+b)**2
    s = (b+c)**2

    print(f"A expressão vale: {(r+s)/2:.2f}")
    
#função para ler a entrada e garantir que o número é positivo
def ler_numero(msg):
    while True:
        try:
            num = int(input(msg))
            if num > 0:
                return num
            else:
                print('O número deve ser positivo. Tente Novamente!')
        except ValueError:
            print(f'Digite apenas números')

main()