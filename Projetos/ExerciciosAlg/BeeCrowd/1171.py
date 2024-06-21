lista=[]
i=0
while i<100:
    n=float(input())
    lista.append(n)
    i+=1
i=0
while i<len(lista):
    if lista[i]<=10:
        print("A["+str(i)+"] = "+ str(lista[i]))
    i+=1