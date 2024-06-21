lista=[]
i=0
while i<20:
    n=int(input())
    lista.append(n)
    i+=1

j=19
i=0
while i<j:
    aux1=lista[i]
    aux2=lista[j]
    lista[i]=aux2
    lista[j]=aux1
    i+=1
    j-=1
i=0
while i<len(lista):
    print("N["+str(i)+"] = "+ str(lista[i]))
    i+=1