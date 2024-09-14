#Conte o número de vezes que a letra r aparece na frase: “O rato roeu a roupa do rei de Roma”. Conte
#diretamente em um f-string 

frase = "O rato roeu a roupa do rei de Roma"
frasezinha = frase.lower()          #isso aqui é pra ele conseguir contar independente se estiver em caixa alta ou não
letra = 'r'
contagem = frasezinha.count(letra)

print(f"Na frase '{frase}', a letra R aparece {contagem} vezes!")