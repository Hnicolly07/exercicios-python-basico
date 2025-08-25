# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido"

turno = input('Em que turno você estuda? (M- Matutino/V-Vespertino/N-Noturno) ').lower()

respostas = ['m', 'n', 'v']

if turno in respostas:
    if turno == 'm':
        print('Bom Dia!')
    elif turno == 'v':
        print('Boa Tarde!')
    else:
        print('Boa Noite!')
else:
    print('Valor Inválido!')