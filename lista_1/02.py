#Faça um programa que tenha as variáveis de dia, mês e ano e imprima, formatando a data com o
#nome da cidade e “/” entre as variáveis.

dia = input('Digite um dia: ')
mes = input('Digite o número de um mês: ')
ano = input('Digite um ano: ')
cidade = input('Digite o nome de uma cidade: ')

print("{}/{}/{}, {}".format(dia, mes, ano, cidade))