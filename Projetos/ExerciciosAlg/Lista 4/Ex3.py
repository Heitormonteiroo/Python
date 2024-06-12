gabarito=input().split(' ')
n=int(input())
i=0
i2=0
boletim=[]
while i<n:
    gabaritoalunos=input().split(' ')
    contador=0
    while i2<6:
        if gabarito[i2]==gabaritoalunos[i2]:
            contador=contador+1
        i2=i2+1
    boletim.append(str(contador))
    i=i+1
    i2=0
i=0
while i<n:
    print(boletim[i])
    i=i+1