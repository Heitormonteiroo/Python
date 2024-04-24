i=int(input())
somap=0
somai=0
while i>0:
    n=int(input())
    if (n%2==0):
        somap=somap+n
    else:
        somai= somai+n
    i=i-1
print("A soma dos pares é "+str(somap)+" e a soma dos impares é "+str(somai))