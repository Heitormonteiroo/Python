n=int(input())
ultimodigito=n%10
condicao="O primeiro e o ultimo digito nao sao iguais"
while n>1:
    n=int(n/10)
    if (n/10<1):
        resto=n%10
        if resto==ultimodigito:
            condicao="O primeiro e o ultimo digito sao iguais"
print(condicao)
