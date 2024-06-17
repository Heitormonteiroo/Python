n=input().split()
lista=[]
i=0
condicao= "É balanceada"
somaant=None
while i<len(n):
    lista.append(int(n[i]))
    i+=1
i=0
while i<len(lista):
    i2=i
    while i2<len(lista):
        if lista[i]>lista[i2]:
            aux=lista[i]
            lista[i]=lista[i2]
            lista[i2]=aux
        i2+=1
    i+=1
i2=len(lista)-1
i=0
while i<i2:
    soma=lista[i]+lista[i2]
    if i!=0:
        if soma!=somaant:
            condicao="Não é balanceada"
    i+=1
    i2=i2-1
    somaant=soma
print(condicao)