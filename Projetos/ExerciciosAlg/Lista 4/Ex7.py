def colchetesint(a):
    i=0
    n=""
    while i<(len(a)):
        if i==0:
            n = n + str(a[i])
        else:
            n=n+","+str(a[i])
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
    if i == 0:
        menor=lista[0]
    if menor>lista[i]:
        menor=lista[i]
    i+=1
print(menor)