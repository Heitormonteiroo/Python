i=int(input())
n=0
n2=0
n1=0
while i>n:
    print(str(n1+n2))
    aux=n1
    n1=n2
    n2=n2+aux
    if n==0:
        n1=1
    n=n+1