frase=input()
tamanho= len(frase)
tamanho=tamanho-1
i=0
condicao="É palindromo"
fraseaocontrario=""
while i<=tamanho:
    fraseaocontrario=fraseaocontrario+frase[tamanho]
    tamanho=tamanho-1
if frase==fraseaocontrario:
    print(condicao)
else:
    print("Nao é um palindromo")