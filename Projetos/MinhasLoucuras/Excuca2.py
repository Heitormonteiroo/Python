n = int(input())
nomes = input().split()
idades = input().split()
dicionario_idades = {}
idade_atual = idades[0]
i=1
i2=0
resposta=""
for nome, idade in zip(nomes, idades):
    dicionario_idades[nome] = idade_atual
    if nome == idade_atual:
        idade_atual = idades[i]
        i=i+1
    resposta = resposta + dicionario_idades[nomes[i2]] + " "
    i2 = i2 + 1
resposta=resposta.strip()
print(resposta)