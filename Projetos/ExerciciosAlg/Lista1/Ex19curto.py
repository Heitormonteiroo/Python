tamanho = int(input("Digite o tamanho da area a ser pintada: "))
litros = tamanho/3
print("Vai precisar de "+str(round((litros/18)+0.5))+" lata(s) vai dar  R$"+str(round((litros/18)+0.5)*80))
print("Vai precisar de "+str(round((litros/3.6)+0.5))+" lata(s) vai dar R$"+str(round((litros/3.6)+0.5)*25))
print("Vai precisar de "+str(round((litros/18)-0.5))+" latas de 18 litros e "+str(round((litros%18/3.6)+0.5))+" latas de 3,6 litros e o valor final vai ser de R$" + str(round((litros/18)-0.5)*80)+str(round(((litros%18)/3.6)+0.5)*25))
