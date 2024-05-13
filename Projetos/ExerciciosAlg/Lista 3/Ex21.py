def conta_digitos(c, d):
    contagem=len(d)
    n=0
    contador=0
    while contagem>n:
        if c == d[n]:
            contador=contador+1
        n=n+1
    return contador
a=input()
b=input()
n2=0
permutacao="É permutaçao"
while n2<len(a):
    a1=a[n2]
    b1=b.index(a1)
    contadora=conta_digitos(a[n2],a)
    contadorb=conta_digitos(b[b1],b)
    if contadora==contadorb:
        n2=n2+1
    else:
        permutacao="Nao é permutaçao"
        n2=n2+1
print(permutacao)