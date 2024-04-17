ivezes=int(input())
n = input()
n = n.split(" ")
for i in range(ivezes):
    resto=int(n[i])%14
    if resto <=6 and int(n[i])>14 and resto >0:
        print("Sim")
    else:
        print("Não")