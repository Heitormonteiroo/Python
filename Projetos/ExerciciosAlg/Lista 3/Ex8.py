n=int(7)
contador=0
while n>0:
    temp=int(input())
    if temp<0:
        contador=contador+1
    n=n-1
print(str(contador))
