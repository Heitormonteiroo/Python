valor= float(input("Digite o valor do produto: "))
if valor <= 50:
    valor = valor * 1.05
elif valor <= 100:
    valor = valor * 1.10
else:
    valor = valor * 1.15
if valor<80:
    print("Barato")
elif valor<=120:
    print("Normal")
elif valor<=200:
    print("Caro")
else:
    print("Muito caro")