# Faça um programa que lê as duas notas parciais de um aluno obtidas por um aluno
# numa disciplina ao lomgo de um semestre e calcule sua média.
# A atribuição de conceitos obedece a tabela abaixo:
# Entre 9.0 e 10.0   A
# Entre 7.5 e 9.0    B
# Entre 6.0 e 7.5    C
# Entre 4.0 e 6.0    D
# Entre 4.0 e 0      E

notas = []

for i in range(2):
    while True:
        nota = float(input(f"Nota {i+1}: "))
        if nota<=10 and nota>=0:
            break
        print('Apenas notas entre 0 e 10.0. Digite Novamente!')
    notas.append(nota)

media = sum(notas)/2

if media>9:
    conceito = 'A'
    reprovado_aprovado = True
elif media>7.5:
    conceito = 'B'
    reprovado_aprovado = True
elif media>6:
    conceito = 'C'
    reprovado_aprovado = True
elif media>4:
    conceito = 'D'
    reprovado_aprovado = False
else:
    conceito = 'E'
    reprovado_aprovado = False

print()
print('-----------------------------')
for i in range(2):
    print(f"{f'NOTA {i+1}:':<22}{notas[i]:.2f}")
print(f"{'MÉDIA:':<22}{media:.2f}")
print(f"{'CONCEITO:':<22}{conceito}")
if reprovado_aprovado:
    print(f"{'STATUS:':<20}APROVADO")
else:
    print(f"{'STATUS:':<22}REPROVADO")