import sys

email =input('''Digite seu email
''')
nome = input('''Digite sue nome
''')

arroba = email.find("@")
lista = email[arroba:]


if nome !='' and email !='':
   if email.find('@') and lista.find("."):
    print("Cadastro concluido")
   else:
    print("Email invalido")
else:
    print("Prencha todos os dados corretamente")

