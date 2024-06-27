def colchetesint(a):
    i=0
    n=""
    while i<(len(a)):
        if i==0:
            n = n + str(a[i])
        else:
            n=n+", "+str(a[i])
        i+=1
    return n
n=input().split()
lista=[]
i=0
menor= None
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
print(colchetesint(lista))
