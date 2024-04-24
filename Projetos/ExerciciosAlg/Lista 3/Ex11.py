i=1
maiorv=0
maiord=0
while i<8:
    valor=int(input())
    if valor>maiorv:
        maiorv=valor
        maiord=i
    i=i+1
print("O dia com mais foi "+str(maiord)+" e o valor foi "+str(maiorv))
