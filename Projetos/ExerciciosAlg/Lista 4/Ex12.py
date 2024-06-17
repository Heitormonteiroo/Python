n=input().split()
lista=[]
listajafoi=[]
contadores=[]
i=0
while i<len(n):
    lista.append(int(n[i]))
    i+=1
i=0
while i<len(lista):
    i2=i+1
    if lista[i] not in listajafoi:
        contador=1
        while i2<len(lista):
            if lista[i]==lista[i2]:
                contador=contador+1
            i2+=1
        contadores.append(contador)
        listajafoi.append(lista[i])
    i+=1
i=0
while i<len(listajafoi):
    print(str(listajafoi[i])+" apareceu "+str(contadores[i])+" vezes")
    i+=1