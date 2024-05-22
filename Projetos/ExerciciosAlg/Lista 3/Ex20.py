def mdc (a,b):
    resto=-1
    while resto !=0:
        resto=a%b
        a=b
        b=resto
    return a
i=int(input())
n=0
n1=0
aux=0
result=0
while i>n:
    if n==0:
        n1=int(input())

    else:
        n2=int(input())
        result=mdc(n1,n2)
        n1=result
    n=n+1
print(result)