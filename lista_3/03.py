#Crie uma string com espaços extras e remova-os. Exemplo: texto = " Espaços extras "

texto_com_espaço = " jaburu jaburanga jabucreia "
texto_sem_espaço = texto_com_espaço.strip()

print(texto_sem_espaço)

'''
O strip() remove, por padrão, todos os espaços em branco do início e do fim da string.
Se quiser remover outros caracteres, precisa especificá-los dentro dos parênteses como um argumento.

    exemplo:
    texto = "***Olá, mundo!***"
    texto_limpo = texto.strip("*")
    print(texto_limpo)  # Saída: "Olá, mundo!"

'''