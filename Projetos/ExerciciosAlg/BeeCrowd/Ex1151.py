i=int(input())
n=0
n2=0
n1=0
tudo=""
while i>n:
    soma=n1+n2
    aux=n1
    n1=n2
    n2=n2+aux
    if n==0:
        n1=1
        tudo=str(soma)
    else:
        tudo=tudo+" "+str(soma)
    n=n+1
print(tudo)

