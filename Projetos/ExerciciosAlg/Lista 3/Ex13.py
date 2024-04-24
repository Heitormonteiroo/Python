i=int(input())
aux=0
verificar="Sim"
while i>0:
    n=int(input())
    if (verificar=="Sim"):
        if n>aux:
            aux=n
            verificar="Sim"
        else:
            verificar="Nao"
    i=i-1
print(verificar)