#Peça ao usuário para inserir um número e exiba a tabuada desse número de 1 a 10. Dica: Use um loop for em um
# range e a operação de multiplicação

num = int(input('Escreva um número: '))

print("a tabuada de {} é a seguinte: ".format(num))
for tabuada in range(1,11):
    resultado = num * tabuada
    print("{} x {:2} = {}".format(num, tabuada, resultado))
