t=int(input())
for i in range(t):
    lista = input().split(" ")
    minutos = int(lista[0])*60+int(lista[1])
    minutosf= 1440-minutos
    print(minutosf)