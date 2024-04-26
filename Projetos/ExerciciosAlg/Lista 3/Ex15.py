i=int(input())
aux=i
condicao="Nao, o primeiro e ultimo digito nao sao iguais"
while i>0:
    n1=int(input())
    if i==aux:
        aux1=n1
    if i==1:
        aux2=n1
        if  aux1==aux2:
            condicao=("Sim, o primeiro e ultimo digito são iguais")

    i=i-1
print(condicao)
