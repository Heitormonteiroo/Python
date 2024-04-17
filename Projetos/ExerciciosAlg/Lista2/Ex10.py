sal=float(input("Digite seu salario: "))
if sal<=500:
    sal=sal+(sal*0.30)
    print("Seu salario com aumento é de R${:.2f}".format(sal))
else:
    print("Nao houve aumento no seu salario")