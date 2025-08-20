# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Tamanho do arquivo em MB: '))
velocidade = float(input('Velocidade de link de Internet em MBps: '))
print(f"Tempo aproximado: {(arquivo/velocidade)/60:.2f} minutos")