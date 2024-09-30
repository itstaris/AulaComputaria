with open('C:\Users\202310164\Desktop\python\tarefas\DESAFIO MEGA SENA.csv', 'r') as csvfile:
    leitor_csv = csv.reader(csvfile)
    for linha in leitor_csv:
        if all(lista in linha for lista in leitor)