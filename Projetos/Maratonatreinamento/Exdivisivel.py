indice=int(input())
for i in range(indice):
    (a,b)=input().split(" ")
    if (int(a)%int(b)!=0):
        n1=(int(a)%int(b))
        contador=int(b)-n1
        print(contador)
    else:
        print("0")
