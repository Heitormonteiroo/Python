n=int(input())
lista=input().split()
i=0
listainteiros=[]
menor=0
posicao=0
while i<len(lista):
    listainteiros.append(int(lista[i]))
    if i==0:
        menor=listainteiros[i]
    if menor>listainteiros[i]:
        menor=listainteiros[i]
        posicao=i
    i+=1
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")