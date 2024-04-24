i=int(input())
somap=0
somai=0
while i>0:
    n=int(input())
    if (n%2==0):
        somap=somap+1
    else:
        somai= somai+1
    i=i-1
print(str(somap)+" numeros pares e "+str(somai)+" numeros impares")