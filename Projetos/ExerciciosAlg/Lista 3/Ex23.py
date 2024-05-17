def quebra(a):
    a2=str(a)
    n=1
    miolo=""
    contagem=len(a2)-1
    primeirodigito=a2[0]
    ultimodigito=a2[len(a2)-1]
    while n<contagem:
        miolo=miolo+a2[n]
        n=n+1
    return primeirodigito,miolo,ultimodigito
numero=int(input())
contador=len(str(numero))-1
while contador>0:
    primeirodigito,miolo,ultimodigito=quebra(numero)
    condicao="Palindromo"
    if primeirodigito==ultimodigito:
        numero=miolo
    else:
        condicao="nao é palindromo"
    contador=contador-2
print(condicao)
