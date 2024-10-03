#Faça um input com a mensagem "Digite seu nome". Não saia do looping até que seja digitado
# literalmente "seu nome". Use a sintaxe de erro de exceção para o looping e condições de
# ou caso o usuário digite seu nome em letras maiúsculas ou minúsculas.

nome = []
nome_lower = []

while nome_lower != "seu nome": #loop enquanto a resposta não for "seu nome"
    nome = input('Digite seu nome ')
    nome_lower = nome.lower().strip()

print("Obrigada :)") #quebra do loop