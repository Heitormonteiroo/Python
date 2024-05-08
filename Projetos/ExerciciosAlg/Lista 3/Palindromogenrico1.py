frase=input()
tamanho= len(frase)
tamanho=tamanho-1
i=0
condicao="É palindromo"
while i<tamanho:
    letra1=frase[i]
    letra2=frase[tamanho]
    if letra1==letra2:
        i=i+1
        tamanho=tamanho-1
    else:
        condicao="Não é um palindromo"
        i=tamanho
print(condicao)

