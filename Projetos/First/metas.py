meta = 10000
lista = [["joao", 15700], ["joana", 8000], ["marcela", 12500], ["joaquim", 12500], ["mano", 10000], ["jacson", 20000]]
for item in lista:
    if item[1] >= meta:
        print("O {} bateu a meta vendendo {}".format(item[0],item[1]))