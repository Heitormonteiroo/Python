n = int(input())
lista_nome = input().split(" ")
lista_nomecrescente = input().split(" ")
i=0
resposta=""
while n>i:
    resposta = resposta + lista_nomecrescente[0] + " "
    lista_nomecrescente.remove(lista_nome[i])
    i=i+1
resposta = resposta.strip()
print(resposta)