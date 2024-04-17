n1 = int(input('Digite 1 numero'))
n2 = int(input('Digite 1 numero'))
n3 = int(input('Digite 1 numero'))

if (n1 > n2 and n1 > n3):
   maiorn = n1
   print(maiorn)
elif n2 > n1 and n2 > n3:
   maiorn = n2
   print(maiorn)
else:
    maiorn = n3
    print(maiorn)
if n1 < n2 and n1 < n3:
    menorn = n1
    print(menorn)
elif n2 < n1 and n2 < n3:
    menorn = n2
    print(menorn)
else:
    menorn = n3
print(menorn)
