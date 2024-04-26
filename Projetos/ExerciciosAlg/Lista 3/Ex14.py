i=int(input())
aux=()
condicao=("Não")
while i>0:
    n1=int(input())
    if n1==aux:
        condicao=("Sim")
    else:
        aux=n1
    i=i-1
print(condicao)