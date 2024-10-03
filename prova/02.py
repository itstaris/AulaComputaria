#Solicite 4 notas de um aluno para o usuário digitar. Tire a média e mostre se ele foi
# aprovado ou não (média 7).


print("Oiê, farei sua média de notas.")
n1 = float(input('Quanto tirou na primeira prova? ')) #valor da primeira nota
n2 = float(input('E na segunda prova? ')) #valor da segunda nota
n3 = float(input('Na terceira? ')) #valor da terceira nota
n4 = float(input('Ok, por último fale a quarta nota: ')) #valor da quarta nota

notas = [n1, n2, n3, n4]

média = sum(notas) / len(notas) #soma do valor das notas dividido pela quantidade de notas

if média < 7: #caso a média seja a baixo de 7
    print(f"Puts.. você ficou com {média} de média, BOMBOU! Estude mais!!!!")
else: #caso a média seja a cima 7
    print(f"Olha! sua média é {média}. Passou!!!!!!!! Boas férias :)")