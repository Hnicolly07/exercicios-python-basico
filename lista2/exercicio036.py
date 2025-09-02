# Faça um programa para a leitura de três notas parciais de um aluno 
# O programa deve calcular a média alcançada pelo aluno e apresentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10. 

notas = []

for i in range(3):
    while True:
        nota = float(input(f"Nota {i+1}: "))
        if nota<=10 and nota>=0:
            break
        print('Apenas notas entre 0 e 10. Digite Novamente!')
    notas.append(nota)

media = sum(notas)/3

if media == 10:
    print('APROVADO COM DISTINÇÃO')    
elif media>=7:
    print('APROVADO')
else:
    print('REPROVADO')

print(f"MÉDIA: {media:.2f}")