E, V = input().split(' ')
tempo_viagem = int(E) / int(V)
horas_viagem = int(tempo_viagem)
minutos_viagem = (tempo_viagem - horas_viagem) * 60
partida_horas = 19
partida_minutos = 0
nova_hora = partida_horas + horas_viagem
nova_minuto = partida_minutos + int(minutos_viagem)
if nova_minuto >= 60:
    nova_hora += nova_minuto // 60
    nova_minuto = nova_minuto % 60
if nova_hora >= 24:
    nova_hora = nova_hora % 24
resultado = f"{nova_hora:02}:{nova_minuto:02}"
print(resultado)