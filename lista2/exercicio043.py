# Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:  infantil A = 5 - 7 anos; infantil B = 8-10 anos; juvenil A = 11-13 anos; juvenil B = 14-17 anos; adulto = maiores de 18 anos.

idade = int(input('Idade: '))

if idade >= 18:
    print('Categoria Adulto')
elif idade >= 14:
    print('Categoria Juvenil B')
elif idade >= 11:
    print('Categoria Juvenil A')
elif idade >= 8:
    print('Categoria Infantil B')
else:
    print('Categoria Infantil A')