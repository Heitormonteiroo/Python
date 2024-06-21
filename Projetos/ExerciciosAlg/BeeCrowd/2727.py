while True:
    try:
        lista=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        n=int(input())
        i=0
        resposta=[]
        while i<n:
            caso=input().split()
            total=0
            if caso[0]==".":
                valor=1
            elif caso[0]=="..":
                valor=2
            elif caso[0]=="...":
                valor=3
            total=valor+((len(caso)-1)*3)
            resposta.append(lista[total-1])
            i+=1
        i=0
        while i<len(resposta):
            print(resposta[i])
            i+=1
    except EOFError:
        break    
