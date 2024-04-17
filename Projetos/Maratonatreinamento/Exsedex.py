N= int(input())
lista= input()
lista =(lista.split(" "))
if int(lista[0])>=N and int(lista[1])>=N and int(lista[2])>=N:
    print("S")
else:
    print("N")