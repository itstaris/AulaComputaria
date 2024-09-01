#Melhore o exercício 1 solicitando um número ao usuário. Adicione uma checagem de erro caso ele não digite um número

import random

try:
    dado = input('Digite um número: ')
    num_aleatorio = random.randint(1, int(dado))
    print("Aqui um número aleatório entre 1 e {}: {}".format(dado, num_aleatorio))
except ValueError:
    print("ERRO! {} não é um número...".format(dado))