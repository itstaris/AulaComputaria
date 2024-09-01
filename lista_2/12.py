#Melhore o exercício 4 com o módulo Time e a função sleep() 

import time

tempo = 101

while tempo>0:
    tempo-=1
    print(tempo)
    time.sleep(1)

print("fim")