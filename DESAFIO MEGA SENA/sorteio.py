import random

lista = []
contador = 0

while contador < 6:
    num = random.randint(1,61)
    lista.append(num)
    if num not in lista:
        contador+=1
        pass
print(lista)