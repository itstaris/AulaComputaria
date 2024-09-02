#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem de aumento. Mostre o valor do aumento, do salário atual e quanto a mais este
#aumento vai resultar em 1 ano

salário = input('hmmmm que carteira gorda em meu amigo, qual que é seu salário? ')
aumentoporc = input('mas você vai receber um aumento, né? qual a porcentagem de aumento? ')

salário2 = float(salário) * (float(aumentoporc)/100 + 1)
aumento = float(salário2) - float(salário)

s1ano = float(salário) * 12
s2ano = float(salário2) * 12
diferença_ano = float(s2ano) - float(s1ano)
print("então você vai ganhar ", aumento, "reais a mais e em um ano ganhará", diferença_ano, "reais de diferença")