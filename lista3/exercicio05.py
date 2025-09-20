# Faça um programa para calcular a área de N quadriláteros. Fórmula: Área = Lado * Lado.

n = int(input('Quantidade de quadriláteros: '))

for i in range(n):
    while True:
        resposta = input('É um quadrado?').lower()

        if resposta in ['sim', 's', 'não', 'n']:
            if resposta == 'sim' or resposta == 's':
                lado = float(input('Digite o valor do lado: '))
                area = lado**2
            else:
                lado1 = float(input('Lado 1: '))
                lado2 = float(input('Lado 2: '))
                area = lado1*lado2
            print(f"Área {i+1}: {area:.2f}")
            break
        print('Resposta Inválida. Tente Novamente!')

