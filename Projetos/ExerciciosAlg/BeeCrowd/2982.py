n=int(input())
i=0
gasto=0
verba=0
while i<n:
    caso=input().split()
    if caso[0]=="G":
        gasto=gasto+int(caso[1])
    else: 
        verba=verba+int(caso[1])
    i+=1
if verba>=gasto:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")