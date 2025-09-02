# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?";
# "Esteve no local do crime?";
# "Mora perto da vítima?";
# "Devia para a vítima?";
# "Já trabalhou com a vítima?"; 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# SIM em 2 questões - "Suspeita"
# entre 3 e 4 - "Cúmplice" 
# 5 - "Assassina". Caso contrário, ele será classificado como "Inocente".

possiveis_respostas = ['sim', 'não', 's', 'n', 'nao']

perguntas = ['Esteve no local do crime?', 'Telefonou para a vítima?', 'Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']

qtd_sim = 0

for pergunta in perguntas:
    while True:
        resposta = input(f"{pergunta} ").lower()
        if resposta in possiveis_respostas:
            if resposta == 'sim' or resposta == 's':
                qtd_sim +=1            
            break
        print('Resposta Inválida!')

if qtd_sim == 5:
    print('Assassino!')
elif qtd_sim >= 3:
    print('Cúmplice!')
elif qtd_sim == 2:
    print('Pessoa suspeita!')
else:
    print('Inocente!')
