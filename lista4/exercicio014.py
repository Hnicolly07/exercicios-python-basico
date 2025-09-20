# Faça um programa que leia um número indeterminado de valores, correspondentes a notas
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados
# c. Exiba todos os valores na ordem inversa à que foram informados
# d. Calcule e mostre a soma dos valores;
# e. Calcule e mostre a média dos valores;
# f. Calcule e mostre a quantidade de valores acima da média calculada;
# g. Calcule e mostre a quantidade de valores abaixo de sete;
# h. Encerre o programa com uma mensagem.

notas = []
i = 0

while True:
    nota = float(input(f'Digite a nota {i+1}: '))
    if nota == -1:
        break
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        i += 1
    else:
        print('NOta Inválida. Apenas valores entre 0 e 10')
    

if len(notas) == 0:
    print('Nenhum valor foi lido. Programa encerrado!')
else:    
    soma = sum(notas)
    media = soma/i

    print()
    print('-'*40)
    print(f"{'QUANTIDADE DE VALORES LIDOS:':<25}{i}")
    print(f"{'VALORES LIDOS':<20}{notas}")
    print(f"{'VALORES ORDEM INVERSA:':<20}{list(reversed(notas))}")
    print(f"{'SOMA:':<20}{soma:.2f}")
    print(f"{'MÉDIA CALCULADA:':<20}{media:.2f}")

    qtd_acima = qtd_abaixo = 0

    for i in range(len(notas)):
        if notas[i] >= media:
            qtd_acima += 1
        if notas[i] < 7:
            qtd_abaixo += 1

    print(f"{'ACIMA DA MÉDIA':<20}{qtd_acima}")
    print(f"{'ABAIXO DE 7':<20}{qtd_abaixo}")

    print('Encerrando programa!')