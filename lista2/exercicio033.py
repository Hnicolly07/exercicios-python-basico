# Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo
# Indique, caso os lados formem um triângulo, se o mesmo é: equilatero, isósceles ou escaleno
# OBS: Triângulo é formado quando a soma de 2 lados é maior que o terceiro
# Equilátero: 3 lados iguais
# Isósceles: 2 lados iguais
# Escaleno: 3 lados diferentes

def main():
    lados = []

    for i in range(3):
        lado = int(input(f"Lado {i+1}: "))
        lados.append(lado)

    if checa_triangulo(lados):
        conjunto_lados = set(lados) # Set junta valores iguais
        qtd_valores = len(conjunto_lados)
        if qtd_valores == 1: # se houver apenas 1 valor é porque todos os lados são iguais
            print('Triângulo Equilátero')
        elif qtd_valores == 2: # 2 lados são iguais
            print('Triângulo Isósceles')
        else: # se houverem 3 valores é porque todos os lados são diferentes
            print('Triângulo Escaleno')
    else:
        print("Os valores informados não formam um triângulo!")

# Função para checar se forma ou não um triângulo
def checa_triangulo(valores):
    if valores[0] + valores[1] > valores[2] and valores[1]+valores[2]>valores[0] and valores[2]+valores[0]>valores[1]:  
        return True
    else:
        return False

main()