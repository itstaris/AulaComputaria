#Solicite um número ao usuário, de 1 a 6. Depois, faça um D6 (dado de 6 lados) e diga se
# ele acertou ou não o número. Caso acerte, dê os parabéns, dizendo o número de tentativas
# que foram gastas. Caso erre, diga que errou e volte a tentar até que o usuário acerte o
# número e dê a mensagem de acerto, com a quantidade de tentativas usadas para acertar

import random

d6 = range(1,7)
num_sorteado = random.choice(d6) #sorteamento de um número aleatório do d6
chutes = 0 #número de tentativas de chutes 

print("Joguei um dado de 6 lados.")
resposta = int(input('Tente chutar que número caiu! ')) #palpite de qual foi o número foi sorteado

while resposta != num_sorteado: #loop que repete enquanto o palpite não corresponder ao número sorteado
    chutes+=1 #soma no número de tentativas de chutes
    resposta = int(input('Hmmm, resposta errada! Dê outro palpite: ')) #novo palpite

if chutes == 1:
    print(f"{num_sorteado}! Isso mesmo, parabéns!!! Você tentou {chutes} vez.")
else:
        print(f"{num_sorteado}! Isso mesmo, parabéns!!! Você tentou {chutes} vezes.")