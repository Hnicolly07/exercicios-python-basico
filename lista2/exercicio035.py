# Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

ano = int(input('Ano: '))
# anos bissextos são divisiveis por 400 ou por 4, mas não por 100

if ano%400==0:
    print(f"{ano} é bissexto")
elif ano%100==0:
    print(f"{ano} não é bissexto")
elif ano%4==0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")