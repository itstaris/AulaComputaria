# Dado a variável meuTexto = “Esta lista contém muitos nomes”, utilize uma f-strig com if e
# else para dizer se a variável meuTexto contém a string “muitos”

meuTexto = "Esta lista contém muitos nomes"

if "muitos" in meuTexto:
    print(f"De fato. {meuTexto}.")
else:
    print("Ah, nem são tantos nomes assim na lista.")    


#Thiago disse que da pra fazer em uma linha só também, TENTAR DEPOIS

'''
meuTexto = "Esta lista contém muitos nomes"
print(f"De fato. {meuTexto}" if "muitos" in meuTexto else "Ah, nem são tantos nomes assim na lista.")
if "muitos" in meuTexto:
    print(f"De fato. {meuTexto}.")
'''