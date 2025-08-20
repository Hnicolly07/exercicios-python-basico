# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9) 

temp_fahrenheit = float(input('Temperatura em Farenheit: '))

print(f"Temperatura em Celsius: {(5 * (temp_fahrenheit-32))/9:.2f}°C")