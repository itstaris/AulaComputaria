#Crie um programa que solicite um número ao usuário e informe se o número é par ou ímpar. Dica: Use o operador
# % para verificar a divisão inteira

num_escolhido = int(input('Escreva um número: '))

#se a sobra do número escolhido dividido por 2 for 0, o número escolhido é par
if num_escolhido % 2 == 0:
    print("{} é par!".format(num_escolhido))
else: print("{} é ímpar!".format(num_escolhido))