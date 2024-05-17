def comprimento(a):
    numeros=""
    while a!=1:
        if (a%2==0):
            a=a/2
            numeros=numeros+str(int(a))+" "
        else:
            a=a*3+1
            numeros=numeros+str(int(a))+" "
    numeros=numeros
    return numeros
kvezes=int(input())
while kvezes>0:
    k=int(input())
    numeros=comprimento(k)
    print(numeros)
    kvezes=kvezes-1
