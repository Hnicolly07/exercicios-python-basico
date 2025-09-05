# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Até 20 litros:
# Álcool: 3% por litro  Gasolina: 4% por litro
# Acima de 20 litros:
# Álcool: 5% por litro  Gasolina: 6% por litro
# Escreva um programa que leia o número de litros vendidos, o tipo de combustível,
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço da gasolina é R$2,50/L e o álcool é R$1,90/L

def main():
    litros = int(input('Litros: '))
    while True:
        combustivel = input('Combústível (A-Álcool ou G-Gasolina): ').lower()
        if combustivel in ['a', 'g']:
            break
        print("Apenas 'A' ou 'G'. Digite novamente!")
    
    desconto = calcula_desconto(litros,combustivel)

    if combustivel == 'g':
        valor_pago = (2.5*litros)-desconto
    else:
        valor_pago = (1.9*litros)-desconto

    print()
    print(f"VALOR PAGO: {valor_pago:.2f}") 
    


def calcula_desconto(litros,combustivel):
    if litros <= 20:
        if combustivel == 'g':
            return (2.5*litros)*0.04
        else:
            return (1.9*litros)*0.03
    else:
        if combustivel == 'g':
            return (2.5*litros)*0.06
        else:
            return (1.9*litros)*0.05
        


main()