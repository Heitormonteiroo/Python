taxa = float(input('Digite a taxa: '))
aplicacao = float(input('Digite a aplicaçao mensal: '))
nmeses = int(input('Digite a quantidade de meses: '))
valor = (aplicacao*((1+taxa)**nmeses)-1)/taxa
print('O valor acumulado é: R$'+ str(valor))