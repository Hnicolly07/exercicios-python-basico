# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: para homens: (72.7*h) – 58 e para mulheres: (62.1*h) - 44.7 (h = altura)  obs: altura em metros

def main():
    altura = float(input('Digite sua altura (em metros): '))
    while True:
        sexo = input('Qual o seu sexo (F/M)? ').lower()
        if sexo == 'f' or sexo == 'm':
            break
        print('Apenas F/f ou M/m. Digite novamente!')
    print(f"Seu peso ideal é {calcula_peso(altura,sexo):.2f}Kg")


def calcula_peso(altura,sexo):
    if sexo == 'f':
        return (62.1*altura)-44.7
    else:
        return (72.7*altura)-58


main()
