# Escreva um programa que calcule a média de 30 alunos
# exiba  a mensagem (aprovado, reprovado ou recuperação)

for i in range(30):
    soma = 0
    for j in range(3): # média de 3 notas
        while True:
            nota = float(input(f"Nota {j+1}: "))
            soma += nota
            if nota >= 0 and nota <= 10:
                break
            
    media = soma/3
    print(f"Média: {media:.2f}")
    if media >= 7:
        print(f"Aluno {i+1} APROVADO!")
    elif media >= 5:
        print(f"Aluno {i+1} em RECUPERAÇÃO!")
    else:
        print(f"Aluno {i+1} REPROVADO!")
    print('--------------------')
    print()
