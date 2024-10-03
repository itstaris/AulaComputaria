#Crie um programa que exiba uma contagem regressiva de 10 para 0, em tempo real de segundos.

import time

cronometro = 10 #definição do número do cronometro 

while cronometro > -1: #looping para printar a contagem regressiva até chegar em 0
    print(cronometro) 
    cronometro-=1 #diminuição do número do cronometro
    time.sleep(1) #definição da velocidade do cronometro


print("EXPLOSÃO TCHAKABUM!!!") #fim da contagem regressiva / do looping