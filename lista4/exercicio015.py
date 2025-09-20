# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete
# feita a uma grande quantidade de organizações:
# 'Qual o melhor Sistema Operacional para uso em servidores?'
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e
# informe ao final o resultado da mesma. O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
# valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma
# das opções devem ser armazenados numa lista. Após os dados terem sido
# completamente informados, o programa deverá calcular o percentual de cada um dos
# concorrentes e informar o vencedor da enquete.

sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

votos = [0] * 7
total = 0

print('Qual o melhor Sistema Operacional para uso em servidores?')

for i in range(len(sistemas)):
    print(f'{i+1}- {sistemas[i]}')
print('0- Encerrar a entrada de dados')
print()


while True:
    resposta = int(input('Sua resposta: '))
    
    if 0 <= resposta <= 6:
        if resposta == 0:
            break
    
        votos[resposta] += 1
        total += 1
    else:
        print('Opção inválida. Digite um número de 0 a 6.')
        
print()
print('--- Resultado da Enquete ---')
print(f"{'Sistema Operacional':<20}{'Votos':>10}{'%':>10}")
print('-' * 42)

for i in range(len(sistemas)):
    nome_os = sistemas[i]
    voto_os = votos[i+1]
    
    if total > 0:
        percentual = (voto_os / total) * 100
        print(f"{nome_os:<20}{voto_os:>10}{percentual:>10.2f}%")
    else:
        print(f"{nome_os:<20}{voto_os:>10}{0.00:>10.2f}%")

print('-' * 42)
print(f"{'Total de votos:':<20}{total:>10}")
print()

if total > 0:
    votos_reais = votos[1:]

    vencedor_votos = max(votos_reais)

    vencedor_index = votos_reais.index(vencedor_votos) + 1
    
    print(f'O vencedor da enquete é o {sistemas[vencedor_index-1]} com {vencedor_votos} votos.')
else:
    print('Nenhum voto foi registrado.')