n = int(input())
i = 2
n1 = 0
n2 = 1
if n == 1:
    print(0)
elif n == 0:
    ()
else:
    tudo = (str(n1) + ‘, ‘ + str(n2))

    while i < n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        tudo = tudo + ‘, ‘ + str(n3)
        i = i + 1
    if n > 2:
             print(tudo)