#Crie um programa que gere e exiba os primeiros 10 números da sequência de Fibonacci. Dica: use uma estrutura
#de loop para gerar a sequência

a = 0
b = 1
d = 0

while d<10:
   c = a + b
   print(c)
   a = b
   b = c
   d+=1