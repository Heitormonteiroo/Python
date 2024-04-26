i=int(input())
while i>0:
    n1=int(input())
    if (n1%2)==0:
        if n1>0:
            print('EVEN POSITIVE')
        elif n1<0:
            print('EVEN NEGATIVE')
        else:
            print('NULL')
    else:
        if n1>0:
            print('ODD POSITIVE')
        elif n1<0:
            print('ODD NEGATIVE')
    i=i-1