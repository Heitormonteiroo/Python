i=int(input())
n1=int(input())
n2=int(input())
i2=0
while i>i2:
    if (n1*i2)<(n2*i2):
        print(n1*i2)
        i2=i2+1
    if (n1*i2)>(n2*i2):
        print(n2*i2)
        i2=i2+1
    if (n1*i2)==(n2*i2):
        print(n1*i2)
        i2 = i2 + 1
    if (n1*i2)>(n2*(i2-1)) and (n2*(i2-1))>0:
        print(n2*(i2-1))
        i=i-1
#Usar um contador pra cada um