cpf = input('''Digite seu CPF
''')
cpf1 = cpf.lstrip()
cpf2 = cpf1.replace("." , "")
cpf3 = cpf2.replace("-" , "")
if len(cpf3) ==11 and cpf3.isnumeric():
    print(cpf3)
else :
    print("Digite o cpf corretamento")