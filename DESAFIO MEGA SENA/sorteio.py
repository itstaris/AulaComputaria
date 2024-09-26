import random
import csv

lista = []
contador = 0

while contador < 6:
    num = random.randint(1,61)
    if num not in lista:
        lista.append(num)
        contador+=1
    else:
        pass

print(lista)

with open('C:\Users\202310164\Desktop\python\tarefas\DESAFIO MEGA SENA.csv', 'r') as csvfile:
    leitor_csv = csv.reader(csvfile)
    for linha in leitor_csv:
        if all(lista in linha for lista in leitor)