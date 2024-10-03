#Faça um programa que peça o nome, idade e altura de uma pessoa e imprima os valores formatados,
#  com uma mensagem personalizada, usando uma f-string. Utilize placeholders para as variáveis na mensagem.

nome = input('Qual é seu nome? ')
idade = input('E a sua idade? ')
altura = input('Tá.. por último, qual a sua altura? ')

print(f"Prazer, {nome}! Então você tem {altura} de altura e {idade} anos em. Tá na flor da idade!")