#Faça um programa que peça um valor de temperatura em Celsius e mostre o valor convertido
# para Fahrenheit. (cálculo para Fahrenheit: F = 9*C/5+32)

celcius = float(input('Digite um número: '))
fafa = 9 * celcius /5 + 32

print("{}°C equivale a {}°F.".format(celcius, fafa))