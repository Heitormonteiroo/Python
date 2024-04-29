n=int(input())
condicao=("Nao existem numeros iguais consectutivos")
while n>=1:
    ultimo_numero=int(n)%10
    print(ultimo_numero)
    n=int(n)/10
    if ultimo_numero==(int(n)%10):
        condicao=("Existem numeros iguais consectutivos")
print(condicao)