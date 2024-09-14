# Crie uma variável com 10 dígitos de π (Pi) e formate os apenas os 2 primeiros dígitos, com vírgula,
# utilizando um f-string

pizão = 3.141592653
pizinho = round(pizão, 2)

print(f"{pizinho}".replace('.', ','))

'''
tentei usar print(pizinho.replace('.', ',')) , MAS NÃO FUNCIONA
por 'pizinho' ser um float, o replace não funciona (método string). daria certo só se declarasse com antecedência que é do tipo string
    assim:
        pizão = 3.141592653
        pizinho = round(pizão, 2)
        string_pizinho = str(pizinho)
        print(string_pizinho.replace('.', ','))

    com format também funciona:
        pizão = 3.141592653
        pizinho = round(pizão, 2)
        print("{:,}".format(pizinho))

    outro jeito usando f-string (O ':,' indica que queremos usar vírgula como separador decimal):
        pizão = 3.141592653
        pizinho = round(pizão, 2)
        print(f"{pizinho:,}")
'''