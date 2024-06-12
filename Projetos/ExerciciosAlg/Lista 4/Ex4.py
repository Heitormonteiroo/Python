#Tentando descobrir se um dado era viciado, um dono de cassino o lançou n vezes.
#Dados os n resultados dos lançamentos (um por linha), determinar o número de
#ocorrências de cada face

n=int(input())
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
contador6=0
i=0
results=[]
while i<n:
    dado=int(input())
    results.append(dado)
    i+=1
i=0
while i<n:
    if results[i]==1:
        contador1+=1
    elif results[i]==2:
        contador2+=1
    elif results[i]==3:
        contador3=contador3+1
    elif results[i]==4:
        contador4+=1
    elif results[i]==5:
        contador5+=1
    elif results[i]==6:
        contador6+=1
    i+=1
print(str(contador1)+' '+str(contador2)+' '+str(contador3)+' '+str(contador4)+' '+str(contador5)+" "+str(contador6))