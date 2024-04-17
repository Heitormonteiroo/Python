tipo = input('Digite o tipo de animal: ')
tipo2 = input('Digite uma caracteristica desse animal: ')
tipo3 = input('Digite outra caracteristica desse animal: ')
if tipo == "vertebrado":
    if tipo2 == "ave":
        if tipo3 == "carnivoro":
            print("Aguia")
        elif tipo3 == "onivoro":
            print("Pomba")
        else:
            print("Digite corretamente")
    elif tipo2 == "mamifero":
        if tipo3 == "onivoro":
            print("Humano")
        elif tipo3 == "herbivoro":
            print("Vaca")
        else:
            print("Digite corretamente")
    else:
        print("Digite corretamente")
elif tipo == "invertebrado":
    if tipo2 == "inseto":
        if tipo3 == "herbivoro":
            print("Largarta")
        elif tipo3 == "hematofago":
            print("Pulga")
        else:
            print("Digite corretamente")
    elif tipo2 == "anelideo":
        if tipo3 == "hematofago":
            print("Sanguessuga")
        elif tipo3 == "onivoro":
            print("minhoca")
        else:
            print("Digite corretamente")
    else:
        print("Digite corretamente")
else:
    print("Digite corretamente")
