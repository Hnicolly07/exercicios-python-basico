# Faça um Programa que verifique se uma letra digitada é "F" ou M. 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

genero = input('Qual o seu sexo (F/M): ').lower()

respostas = ['f', 'm']

if genero in respostas:
    if genero == 'f':
        print('F - Feminino')
    else:
        print('M - Masculino')
else:
    print('Sexo Inválido!')

