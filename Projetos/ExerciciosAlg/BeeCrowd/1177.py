t=int(input())
lista=[]
i=0
contador=0
while i<1000:
    lista.append(contador)
    contador+=1
    if contador==t:
        contador=0
    i+=1
i=0
while i<len(lista):
    print("N["+str(i)+"] = "+ str(lista[i]))
    i+=1