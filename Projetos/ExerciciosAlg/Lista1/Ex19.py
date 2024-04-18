import math

tamanho = int(input("Digite o tamanho da area a ser pintada: "))
litros = tamanho/3
latas80 = round((litros/18)+0.5)
latas36 = round((litros/3.6)+0.5)
litrosmodulo = litros%18
latas36b =litrosmodulo/3.6
latas80b = round((litros/18)-0.5)
print("Vai precisar de "+str(latas80)+" lata(s) vai dar  R$"+str(latas80*80))
print("Vai precisar de "+str(latas36)+" lata(s) vai dar R$"+str(latas36*25))
print("Vai precisar de "+str(latas80b)+" latas de 18 litros e "+str(round(latas36b+0.5))+" latas de 3,6 litros e o valor final vai ser de R$" + str(latas80b*80+(round(latas36b+0.5)*25)))


latas8 = math.ceil(litros/18)
print(latas8)