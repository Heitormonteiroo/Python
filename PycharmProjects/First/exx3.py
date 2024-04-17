meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_1sem.extend(vendas_2sem)
melhor = max(vendas_1sem)
indicemaior = vendas_1sem.index(melhor)
pior = min(vendas_1sem)
indicemenor = vendas_1sem.index(pior)
vendastotal = sum(vendas_1sem)
print("O melhor mes foi {} com {} vendas e o pior mes foi {} com {} vendas".format(meses[indicemaior], melhor,
                                                                                   meses[indicemenor], pior))
print('O total de vendas foi {}'.format(vendastotal))
vendas_1sem.remove(melhor)
melhor2 = max(vendas_1sem)
vendas_1sem.remove(melhor2)
melhor3 = max(vendas_1sem)
top3 = [melhor, melhor2, melhor3]
print(top3)
