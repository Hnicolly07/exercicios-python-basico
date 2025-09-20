# Escreva um programa que calcula o fatorial de um dado número N.

def main():
    num = int(input('Digite o número do qual você deseja calcular o fatorial: '))
    print(f"{num}! é igual a {fatorial(num)}")

def fatorial(num):
    if num < 0:
        return 'Não existe fatorial de número negativo'
    if num == 0 or num == 1:
        return 1
    return num * fatorial(num-1)

main()