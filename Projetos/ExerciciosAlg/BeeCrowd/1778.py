t=float(input())
lista=[]
i=0
while i<100:
    if i ==0:
        lista.append(t)
        i+=1
        t=t/2
    lista.append(t)
    t=t/2
    i+=1
i=0
while i<len(lista):
    print(f"N[{i}] = {lista[i]:.4f}")
    i+=1