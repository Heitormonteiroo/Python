def colchetesint(a):
    i=0
    n=""
    while i<(len(a)):
        if i==0:
            n = n + str(a[i])
        else:
            n=n+","+str(a[i])
        i+=1
    return n
