while True:
    try:
        n,d=input().split(" ")
        i=0
        diacerto=""
        jafoi=False
        while i<int(d):
            lista=input().split(" ")
            condicao=True
            i2=1
            while i2 <= int(n):
                if int(lista[i2])==0:
                    condicao=False
                i2+=1       
            if condicao==True and jafoi==False:
                diacerto=lista[0]
                jafoi=True
            i2=0
            i+=1
        if diacerto=="":
            print("Pizza antes de FdI")
        else:
            print(diacerto)
    except EOFError:
        break