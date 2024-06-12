#Um jogador interessado em cassinos deseja fazer um levantamento estatístico
#simples sobre uma roleta. Para isso, ele fez n lançamentos nesta roleta. Sabendo
#que uma roleta contém 37 números (de 0 a 36), calcular a frequência de cada
#número desta roleta nos n lançamentos realizados.
def colchetesint(a):
    i=0
    n=""
    while i<(len(a)):
        if i==0:
            n = n + str(a[i])
        else:
            n=n+","+str(a[i])
        i+=1
    return n
n=int(input())
lista=[]
i=0
while i<37:
    lista.append(0)
    i+=1
i=0
while i<n:
    result=int(input())
    lista[result]=lista[result]+1
    i+=1
print(colchetesint(lista))
