n=int(input())
certo=input()
a=0
b=0
c=0
i=0

if certo =="A":
    a=1
elif certo=="B":
    b=1
else:
    c=1
while i<n:
    movimento=int(input())
    aux=0
    if movimento==1:
        aux=a
        a=b
        b=aux
        
    elif movimento==2:
        aux=b
        b=c
        c=aux
        
    elif movimento==3:
        aux=c
        c=a
        a=aux
        
    i+=1
if a==1:
    print("A")
elif b==1:
    print("B")
elif c==1:
    print("C")
