# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é: 
# par ou ímpar; 
# positivo ou negativo; 
# inteiro ou decimal. 

def main():
    nums = [] # Lista para armazenar os 2 números

    for i in range(2):
        num = float(input(f"Número {i+1}: "))
        nums.append(num)
    
    respostas = ['subtração', 'soma', 'divisão', 'multiplicação']
    while True:
        operacao = input('Qual Operação você deseja realizar? ').lower()
        if operacao in respostas:
            break
        print('Operação inválida! Tente novamente.')
    
    
    resultado = calcula(nums,operacao)
    print(f"Operação escolhida {operacao} e o resultado é {resultado:.1f}")
    
    # Se o número for inteiro entra aqui
    if decimal_ou_inteiro(resultado):
        print(f"{resultado:.1f} é inteiro e {impar_ou_par(resultado)}")
    else: # Se o número for decimal entra aqui
        print(f"{resultado:.1f} é decimal")
    
    if resultado>0:
        print(f"{resultado:.1f} é positivo!")
    elif resultado==0:
        print(f"{resultado:.1f} é neutro!")
    else: 
        print(f"{resultado:.1f} é negativo!")


def calcula(nums, operacao):
    match operacao:
        case 'soma':
            return sum(nums)
        case 'subtração':
            return nums[0]-nums[1]
        case 'divisão':
            return nums[0]/nums[1]
        case 'multiplicação':
            return nums[0]*nums[1]

def impar_ou_par(valor):
    if valor%2==0:
        return "par!"
    else:
        return "ímpar!"
    
def decimal_ou_inteiro(valor):
    if valor%1==0: # Para saber se é inteiro basta dividir por 1, se tiver resto é
        return True
    else: # Se não tiver resto, o número é decimal
        return False


main()

