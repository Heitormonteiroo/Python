print('Digite o numero de alunos')
i=int(input())
maiornota=0
menornota=100
while i>0:
    nota=int(input())
    if nota<=100 and nota>=0:
        if nota>maiornota:
            maiornota=nota
        if nota<menornota:
            menornota=nota
        i=i-1
    else:
        print("Digite corretamente")
print("A maior nota é "+str(maiornota)+" e a menor nota "+(str(menornota)))