import math

tamanho = int(input('Digite o tamanho do arquivo: '))
velocidade = int(input('Digite a velocidade da internet em MBs: '))
tempo = tamanho/velocidade
tempom = tempo/60

print(round(tempom))