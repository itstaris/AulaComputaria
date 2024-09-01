#Crie uma lista com 3 nomes, peça um nome para o usuário e diga se este nome está contido ou não na lista

print("Olá, aqui é o Red Carpet Facamp 2024! O evento mundialmente (des)conhecido mais badalado de todos!!!!! \n Aqui é um evento VIP, só entra se tiver o nome na lista.")
nome = input('Por favor, qual é o seu nome? ')

lista = ["Thiago", "Kadow", "Damiani"]

if nome in lista:
    print("Olha só, {} está na lista! Pode entrar, seja bem-vindo.".format(nome))
else:
    print("Hmmm, {} não está na lista... RALA DAQUI!!!!!!!!!!!!!!!!!".format(nome))