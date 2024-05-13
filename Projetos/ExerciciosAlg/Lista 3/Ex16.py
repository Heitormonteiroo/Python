i=int(input())
n1=int(input())
n2=int(input())
aux=0
i2=0
contador=0
if n2<n1:
    aux=n1
    n1=n2
    n2=aux
while i>i2:
    result=int(n1*contador)
    result2=int(n2*contador)
    resultant=int(n1*(contador-1))
    resultant2=int()
    print(result,result2,resultant,contador)
    if result==result2:
        print(result)
        contador=contador+1
        i2=i2+1
    else:
        if result%n2==0:
            print(result2)
            i2=i2+1
            contador=contador+1
        elif result2>resultant and resultant!=0 and resultant%n1!=0:
            print(resultant)
            i2=i2+1
            contador=contador+1
        else:
            print(result)
            print(result2)
            i2=i2+2
            contador=contador+1

