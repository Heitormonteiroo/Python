tipo = input("Qual a categoria?")
nome = input("Qual o nome do produto?")
qnt = int(input("Qual a quantidade em estoque?"))
if tipo and nome and qnt:
    if tipo == "bebida":
        if qnt <60:
            print("Quantidade de {} baixa,Estoque: {}".format(nome,qnt))
    elif tipo == "limpeza":
        if qnt <35:
            print("Quantidade de {} baixa,Estoque: {}".format(nome, qnt))
    elif tipo == "comida":
        if qnt <25:
            print("Quantidade de {} baixa,Estoque: {}".format(nome, qnt))
    else:
        print("Digite a categoria corretamente")
else:
    print("Digite todos os valores")