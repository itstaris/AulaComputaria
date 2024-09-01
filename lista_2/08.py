#Use um loop for e range para somar todos os números ímpares de 1 a 300 e exiba a soma

num_impar = range(1, 300, 2)
soma = sum(num_impar)

print("A soma de todos os números ímpares entre 1 e 300 é {}".format(soma))