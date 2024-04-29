import random
placar1=0
placar2=0
contador=3
meuponto=0
pontoadversario=0
listaa=[]
rodadas=int(input("Digite qunatos pontos para terminar a partida: "))
verificador1,verificador2,verificador3=0,0,0
lista = [1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 3.4, 4.1, 4.2, 4.3, 4.4, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, 8.4, 9.1, 9.2, 9.3, 9.4, 10.1, 10.2, 10.3, 10.4]
lista2 = ["4 de ouros", '4 de espadas',"4 de copas","4 de paus","5 de ouros", "5 de espadas","5 de copas","5 de paus","6 de ouros", "6 de espadas","6 de copas","6 de paus","7 de ouros", "7 de espadas","7 de copas","7 de paus","Dama de ouro","Dama de espadas","Dama de copas","Dama de paus","Valete de ouro","Valete de espadas","Valete de copas","Valete de Paus","Rei de ouro","Rei de espadas","Rei de copas","Rei de paus","A de ouro","A de espadas","A de copas","A de paus" ]
while placar1<rodadas and placar2<rodadas:
    carta1 = random.choice(lista)
    lista.remove(carta1)
    carta2 = random.choice(lista)
    lista.remove(carta2)
    carta3 = random.choice(lista)
    lista.remove(carta3)
    carta1a = random.choice(lista)
    lista.remove(carta1a)
    carta2a = random.choice(lista)
    lista.remove(carta2a)
    carta3a = random.choice(lista)
    lista.remove(carta3a)
    listaa.append(carta1a)
    listaa.append(carta2a)
    listaa.append(carta3a)
    print("Cartas: {},{},{}".format(carta1, carta2, carta3))
    while contador>0:
        escolha = input("Escolha a sua carta: ")
        cartaadv=random.choice(listaa)
        if escolha =='1' and verificador1!=1:
            if carta1>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(carta1))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador1=1
            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(carta1))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador1=1
            listaa.remove(cartaadv)
            contador = contador - 1
        elif escolha =='2' and verificador2!=1:
            if carta2>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(carta2))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador2 = 1
            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(carta1))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador2 = 1
            listaa.remove(cartaadv)
            contador = contador - 1
        elif escolha =='3' and verificador3!=1:
            if carta3>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(carta3,))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador3 = 1

            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(carta1))
                print("A do seu adversario foi {}".format(cartaadv))
                verificador3 = 1
            listaa.remove(cartaadv)
            contador = contador - 1
        else:
            print("Escolha corretamente")
    if meuponto>pontoadversario:
        placar1=placar1+1
        meuponto=0
        pontoadversario=0
        print("Voce ganhou a rodada!!")
    else:
        placar2=placar2+1
        meuponto = 0
        pontoadversario = 0
        print("Voce perdeu a rodada:(")
    print("Placar:{} a {}!".format(placar1,placar2))
    lista.append(carta1)
    lista.append(carta2)
    lista.append(carta3)
    lista.append(carta1a)
    lista.append(carta2a)
    lista.append(carta3a)
    verificador3,verificador2,verificador1,contador=0,0,0,3
if placar1>placar2:
    print("Voce ganhou o jogo, o placar foi de {} a {}".format(placar1,placar2))
else:
    print("Voce perdeu o jogo, o placar foi de {} a {}".format(placar2,placar1))