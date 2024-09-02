#Peça 4 notas de um aluno. Tire a média e mostre se ele foi aprovado ou não (média 7)

n1 = float(input('Insira a nota da sua 1ª prova: '))
n2 = float(input('Insira a nota da sua 2ª prova: '))
n3 = float(input('Insira a nota da sua 3ª prova: '))
n4 = float(input('Insira a nota da sua 4ª prova: '))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print("Sua média é {}! Parabéns, você passou!!!!".format(media))
else:
    print("Puts... sua média é {}. Você não passou!".format(media))