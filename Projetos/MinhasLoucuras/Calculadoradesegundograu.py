import math

a = float(input('Qual o valor de a: '))
b = float(input('Qual o valor de b: '))
c = float(input('Qual o valor de c: '))

if a != 0:
    delta= (b**2)-(4*a*c)
    if delta <0:
        print('Nao possui raizes raizes reais')
    elif delta ==0:
        raiz1 =  -b/2*a
        print('Possui apenas uma raiz real, {}'.format(raiz1))
    else:
        raizdelta = math.sqrt(delta)
        r1 = round((-b + raizdelta)/2 * a)
        r2 = round((-b - raizdelta) / 2 * a)
        print('A raiz 1 é {} e a raiz 2 é {}'.format(r1,r2))
else :
    print('Não é uma equaçao de segundo grau')