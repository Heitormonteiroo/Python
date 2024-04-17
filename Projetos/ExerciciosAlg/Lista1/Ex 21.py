km = float(input("Digite a distancia que vc vai percorrer: "))
kmh = float(input("Digite a velocidade que voce esta viajando:  "))
tempo = round(((km*1000)/(kmh/3.6)/60))
if tempo>60:
    min = round(tempo % 60)
    tempo= round((tempo/60)-0.5)
    print('A viagem vai levar {} horas e {} minutos'.format(tempo,min))
else:
    print('A viagem vai levar {} minutos'.format(tempo))