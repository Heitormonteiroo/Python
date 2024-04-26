i=1
contador=0
vi=0
vg=0
empate=0
while i!=2:
    (goli,golg)=input().split(" ")
    contador=contador+1
    if int(goli)>int(golg):
        vi=vi+1
    elif int(goli)<int(golg):
        vg=vg+1
    else:
        empate=1+empate
    print("Novo grenal (1-sim 2-nao)")
    i=int(input())
if vi>vg:
    ganhador="Inter venceu mais"
elif vi<vg:
    ganhador="Gremio venceu mais"
else:
    ganhador='Nao houve vencedor'
print("{} grenais".format(contador))
print("Inter:{}".format(vi))
print("Gremio:{}".format(vg))
print("Empates:{}".format(empate))
print(ganhador)