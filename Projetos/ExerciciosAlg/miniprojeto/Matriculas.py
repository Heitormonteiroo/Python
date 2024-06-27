#caso tirar um aluno tirar ele de todas as diciplinas
def colchetesint(a):
    i=0
    n=""
    while i<(len(a)):
        if i==0:
            n = n + str(a[i])
        else:
            n=n+str(a[i])
        i+=1
    return n
def escrever(nome,cpf):
    fp=open("Alunos.csv","a")
    fp.write("Nome: "+ str(nome) + " CPF: "+ str(cpf)+ "\n")
    fp.close()
def verificar(cpf):
    fp=open("Alunos.csv","r")
    linhas=fp.readlines()
    i=0
    condicao=False
    while len(linhas)>i:
        linha=linhas[i].split()
        if linha[3]==cpf:
            condicao=True
        i+=1
    fp.close()
    return condicao
def achar(cpf):
    fp = open("Alunos.csv", "r")
    linhas = fp.readlines()
    i = 0
    condicao = True
    alunoobtido=[]
    indice=None
    while len(linhas) > i:
        linha = linhas[i].split()
        if linha[3] == cpf:
            alunoobtido=linha
            indice=i
        i += 1
    fp.close()
    return alunoobtido, indice
def lista():
    fp=open("Alunos.csv","r")
    linhas=fp.readlines()
    fp.close()
    return linhas
def editar(indice,novo,oque):
    fp=open("Alunos.csv","r")
    linhas = fp.readlines()
    linha=linhas[indice].split()
    linha[oque]=novo
    i=0
    n = ""
    while i < (len(linha)):
        if i == len(linha):
            n = n + str(linha[i])
        else:
            n = n + str(linha[i]+" ")
        i += 1
    linhas[indice]=n+"\n"
    fp.close()
    fp = open("Alunos.csv","w")
    fp.writelines(linhas)
    fp.close()
def remover(cpf,novo):
    fp=open("Alunos.csv","r")
finalizar=True
while finalizar:

    print("----------------------------------------------------")
    print("Digite:")
    print("1-Gerenciamento ou cadastro de usuarios")
    print("2-Gerenciamento e cadastro diciplinas")
    print("3-Matricular aluno em uma diciplina")
    print("4-Cancelar a matricula de um aluno")
    print("5-Relatorio matriculas por diciplina")
    print("6-Sair")
    print("----------------------------------------------------")
    
    op1=int(input())

    if op1==1:
        continuar=True
        while continuar:
            print("-------------------------------------")
            print("Voce deseja: ")
            print("1-Cadastrar um novo usuario")
            print("2-Editar um usuario")
            print("3-Remover um usuario")
            print("4-Listar os alunos")
            print("5-Voltar")
            print("-------------------------------------")
            op2=int(input())
            if op2==1:
                #Usar strip para deixar o cpf certo
                certo1=True
                
                while certo1:
                    nome=input("Digite o nome: ")
                    cpf=input("Digite o CPF: ")
                    if len(cpf)==11:
                        if verificar(cpf):
                            print("Esse numero de cpf ja esta cadastrado")
                        else:
                            escrever(nome,cpf)
                            certo=False
                    else:
                        print("Digite o cpf corretamente")
                    print("Digite 1 para digitar novamente ou qualquer tecla para voltar")
                    certo1op=input()
                    if certo1op!="1":
                        certo1=False
            if op2==2:
                certo1=True
                while certo1:
                    print("--------------------------------------------------------------------------")
                    print("Digite o CPF ou digite 1 para abrir a lista de aluno ou 2 para voltar")
                    print("--------------------------------------------------------------------------")
                    n=input()
                    if n=="1":
                        listainicial=lista()
                        listafinal=colchetesint(listainicial)
                        print(listafinal)
                    elif n=="2":
                        certo1=False
                    elif len(n)==11 and verificar(n):
                        aluno,indice=achar(n)
                        aluno=colchetesint(aluno)
                        certo2=True
                        print(aluno)
                        while certo2:
                            print("-------------------------------------")
                            print("O que voce deseja fazer com este aluno")
                            print("1=Mudar o nome")
                            print("2=Mudar o CPF")
                            print("3=Voltar")
                            print("-------------------------------------")
                            n=input()
                            if n=="1":
                                print("Digite o novo nome:")
                                novo=input()
                                oque=1
                                editar(indice, novo, oque)
                                print("Nome trocado com sucesso")
                            if n=="2":
                                print("Digite o novo CPF:")
                                novo=input()
                                oque=3
                                if len(novo) ==11 and verificar(novo)==False:
                                    editar(indice,novo,oque)
                                    print("CPF trocado com sucesso")
                                else:
                                    print("Esse CPF ja pertence a outro aluno")
                            if n=="3":
                                certo2=False
                    else:
                        print("CPF invalido")
            if op2==3:
                certo1 = True
                while certo1:
                    print("--------------------------------------------------------------------------")
                    print("Digite o CPF ou digite 1 para abrir a lista de aluno ou 2 para voltar")
                    print("--------------------------------------------------------------------------")
                    n = input()
                    if n == "1":
                        listainicial = lista()
                        listafinal = colchetesint(listainicial)
                        print(listafinal)
                    elif n == "2":
                        certo1 = False
                    elif len(n) == 11 and verificar(n):
                        aluno,indice=achar(n)
                        print(aluno)
                        print("Voce tem certeza que deseja remover esse aluno?(sim/nao)")
                        confirmacao=input()
                        if confirmacao == "sim"or confirmacao == "Sim":

            if op2==4:
                listainicial = lista()
                listafinal = colchetesint(listainicial)
                print(listafinal)
            if op2==5:
                continuar=False
    if op1==6:
        finalizar=False
        print("Programa encerrado,Até Logo")