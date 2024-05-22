n = int(input())
contadorguardadoc=0
contadorguardadot=0
contadorcasa = 0
contadortrabalho = 0
while n>0:
    ida,volta=input().split(" ")
    if ida =="chuva":
        if contadorcasa == 0:
            contadorguardadoc=contadorguardadoc+1
            contadortrabalho=contadortrabalho+1
        if contadorcasa>0:
            contadorcasa=contadorcasa-1
            contadortrabalho=contadortrabalho+1
    if volta =="chuva":
        if contadortrabalho == 0:
            contadorguardadot=contadorguardadot+1
            contadorcasa=contadorcasa+1
        if contadortrabalho>0:
            contadortrabalho=contadortrabalho-1
            contadorcasa=contadorcasa+1
    n=n-1
print(contadorguardadoc,contadorguardadot)
