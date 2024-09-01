# Crie uma lista com os números de 1 a 100. A seguir, escolha um número desta lista e imprima-o. Utilize a função
# choice() do módulo random

import random

lista = range(1, 101, 1)
escolha = random.choice(lista)

print(escolha)