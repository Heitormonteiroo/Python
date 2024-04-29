import random
placar1=0
placar2=0
contador=3
meuponto=0
pontoadversario=0
rodadas=int(input("Digite quantos pontos para terminar a partida: "))
verificador1,verificador2,verificador3=0,0,0

lista = [1.1, 1.2, 1.3, 1.4,
         2.1, 2.2, 2.3, 2.4,
         3.1, 3.2, 3.3, 3.4,
         4.1, 4.2, 4.3, 4.4,
         5.1, 5.2, 5.3, 5.4,
         6.1, 6.2, 6.3, 6.4,
         7.1, 7.2, 7.3, 7.4,
         8.1, 8.2, 8.3, 8.4,
         9.1, 9.2, 9.3, 9.4,
         10.1, 10.2, 10.3, 10.4]

baralho= [
    "4 de ouros", '4 de espadas', "4 de copas", "4 de paus",
    "5 de ouros", "5 de espadas", "5 de copas", "5 de paus",
    "6 de ouros", "6 de espadas", "6 de copas", "6 de paus",
    "7 de ouros", "7 de espadas", "7 de copas", "7 de paus",
    "Dama de ouro", "Dama de espadas", "Dama de copas", "Dama de paus",
    "Valete de ouro", "Valete de espadas", "Valete de copas", "Valete de Paus",
    "Rei de ouro", "Rei de espadas", "Rei de copas", "Rei de paus",
    "A de ouro", "A de espadas", "A de copas", "A de paus",
    "2 de ouros", '2 de espadas', "2 de copas", "2 de paus",
    "3 de ouros", '3 de espadas', "3 de copas", "3 de paus"]

while placar1<rodadas and placar2<rodadas:
    cartas = random.sample(lista, 6)
    carta1, carta2, carta3, cartaadv1, cartaadv2, cartaadv3 = cartas
    indice1 = lista.index(carta1)
    indice2 = lista.index(carta2)
    indice3 = lista.index(carta3)
    cartasadv = [cartaadv1, cartaadv2, cartaadv3]
    print("Cartas: {}=1,{}=2,{}=3".format(baralho[indice1], baralho[indice2], baralho[indice3]))
    while contador>0:
        escolha = input("Escolha a sua carta 1, 2 ou 3: ")
        cartaadv=random.choice(cartasadv)
        i = lista.index(cartaadv)
        if escolha =='1' and verificador1!=1 :
            if carta1>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(baralho[indice1]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador1=1
            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(baralho[indice1]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador1=1
            cartasadv.remove(cartaadv)
            if meuponto==2 or pontoadversario==2:
                contador = 0
            else:
                contador = contador - 1
        elif escolha =='2' and verificador2!=1:
            if carta2>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(baralho[indice2]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador2 = 1

            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(baralho[indice2]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador2 = 1
            cartasadv.remove(cartaadv)
            if meuponto==2 or pontoadversario ==2:
                contador = 0
            else:
                contador = contador - 1
        elif escolha =='3' and verificador3!=1:
            if carta3>cartaadv:
                meuponto = meuponto+1
                print("Voce ganhou!!")
                print("Sua carta foi {}".format(baralho[indice3]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador3 = 1

            else:
                pontoadversario=pontoadversario+1
                print("Voce perdeu :(")
                print("Sua carta foi {}".format(baralho[indice3]))
                print("A do seu adversario foi {}".format(baralho[i]))
                verificador3 = 1
            cartasadv.remove(cartaadv)
            if meuponto==2 or pontoadversario==2:
                contador=0
            else:
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
    print("---------------")
    print("PLACAR:{} a {}!".format(placar1, placar2))
    print("PROXIMA RODADA")
    print("---------------")
    verificador3,verificador2,verificador1,contador=0,0,0,3
if placar1>placar2:
    print("Voce ganhou o jogo, o placar foi de {} a {}".format(placar1,placar2))
else:
    print("Voce perdeu o jogo, o placar foi de {} a {}".format(placar2,placar1))
#Resolver o negocio do jogo acabar errado colocar pra trucar