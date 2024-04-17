peso=int(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
imc=peso/(altura**2)
print('Seu imc é {:.2f}'.format(imc))
if imc<=20:
    print('Abaixo do peso')
elif imc<=25:
    print("Peso normal")
elif imc<=30:
    print("Sobrepeso")
elif imc<=40:
    print("Obeso")
elif imc>40:
    print("Obesidade morbida")