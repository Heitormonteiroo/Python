i=int(input())
while(i>0):
    (a,b)=input().split(" ")
    a=int(a)
    b=int(b)
    t=0
    if(a%b!=0):
        resto=a%b
        t=b-resto
        print(t)
    else:
        print(t)
    i=i-1

