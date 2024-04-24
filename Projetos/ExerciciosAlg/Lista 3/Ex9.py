i=int(input())
soma=0
soma2=0
while i>0:
    n=int(input())
    if n>0:
        soma=soma+1
    else:
        soma2=soma2+1
    i=i-1
print(str(soma)+" e "+str(soma2))