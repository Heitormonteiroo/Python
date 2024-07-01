#caso tirar um aluno tirar ele de todas as diciplinas
#Remover disciplinas ta errado testar tudo de nov
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
def remover(indice):
    linhas2 = []
    fp=open("Alunos.csv","r")
    linhas=fp.readlines()
    i=0
    while len(linhas)>i:
        if i!=indice:
            linhas2.append(linhas[i])
            i+=1
        else:
            i+=1
    fp.close()
    fp=open("Alunos.csv","w")
    fp.writelines(linhas2)
    fp.close()
def escreverm(materia):
    fp = open("Materias.csv", "a")
    fp.write("Nome: " + str(materia) + "\n")
    fp.close()
def verificarm(disciplina):
    fp = open("Materias.csv", "r")
    linhas = fp.readlines()
    i = 0
    condicao = False
    while len(linhas) > i:
        linha ="Nome: "+ str(linhas[i].split())
        if linha == disciplina:
            condicao = True
        i += 1
    fp.close()
    return condicao
def editarm(indice,novo):
    fp = open("Materias.csv", "r")
    linhas = fp.readlines()
    linha = linhas[indice].split()
    linha[1] = novo
    i = 0
    n = ""
    while i < (len(linha)):
        if i == len(linha):
            n = n + str(linha[i])
        else:
            n = n + str(linha[i] + " ")
        i += 1
    linhas[indice] = n + "\n"
    fp.close()
    fp = open("Materias.csv", "w")
    fp.writelines(linhas)
    fp.close()
def listam():
    fp = open("Materias.csv", "r")
    linhas = fp.readlines()
    fp.close()
    return linhas
def acharm(disciplina):

    fp = open("Materias.csv", "r")
    linhas = fp.readlines()
    i = 0
    condicao = True
    disciplinaobtida =""
    indice = None
    while len(linhas) > i:
        linha ="Nome: "+ str(linhas[i].split())
        if linha == disciplina:
            disciplinaobtida = linha
            indice = i
        i += 1
    fp.close()
    return disciplinaobtida, indice
def removerm(indice):
    linhas2 = []
    fp = open("Materias.csv", "r")
    linhas = fp.readlines()
    i = 0
    while len(linhas) > i:
        if i != indice:
            linhas2.append(linhas[i])
            i += 1
        else:
            i += 1
    fp.close()
    fp = open("Materias.csv", "w")
    fp.writelines(linhas2)
    fp.close()
print("Seja bem-vindo(a)")
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
                    else:
                        print("Digite o cpf corretamente")
                    print("Digite 1 para cadastrar outro aluno ou qualquer tecla para voltar")
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
                    print("Digite o CPF do aluno que deseja remover  "
                          "Ou digite 1 para abrir a lista de aluno ou 2 para voltar")
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
                        print(colchetesint(aluno))
                        certo2=True
                        while certo2:
                            print("Voce tem certeza que deseja remover esse aluno?(sim/nao)")
                            confirmacao=input()
                            if confirmacao == "sim"or confirmacao == "Sim":
                                remover(indice)
                                print("Aluno removido com sucesso")
                                certo1=False
                                certo2=False
                            if confirmacao == "nao" or confirmacao == "Nao" or confirmacao == "Não" or confirmacao == "não":
                                certo2=False
            if op2==4:
                listainicial = lista()
                listafinal = colchetesint(listainicial)
                print(listafinal)
                input("Pressione ENTER para continuar")
            if op2==5:
                continuar=False
    if op1==2:
        continuar = True
        while continuar:
            print("-------------------------------------")
            print("Voce deseja: ")
            print("1-Cadastrar uma nova disciplina")
            print("2-Editar uma disciplina")
            print("3-Remover uma disciplina")
            print("4-Listar as diciplinas")
            print("5-Voltar")
            print("-------------------------------------")
            op2 = int(input())
            if op2==1:
                certo1 = True

                while certo1:
                    disciplina = input("Digite o nome da disciplina que deseja cadastrar ou digite 2 para voltar: ")
                    if disciplina=="2":
                        certo1=False
                    elif verificarm(disciplina):
                        print("Essa disciplina ja existe")
                    else:
                        print("Voce deseja cadastras--"+str(disciplina)+"(sim/nao)")
                        simounao=input()
                        if simounao=="sim" or simounao=="Sim":
                            escreverm(disciplina)
                            print("Disciplina cadastrada com sucesso")
                        print("Digite 1 para cadastrar outra materia ou aperte qualquer tecla para voltar")
                        voltar=input()
                        if voltar!="1":
                            certo1=False
            if op2 == 2:
                certo1=True
                while certo1:
                    print("--------------------------------------------------------------------------------------")
                    print("Digite a Disciplina ou digite 1 para abrir a lista de disciplinas ou 2 para voltar")
                    print("--------------------------------------------------------------------------------------")
                    n = input()
                    if n == "1":
                        listainicial = listam()
                        listafinal = colchetesint(listainicial)
                        print(listafinal)
                    elif n == "2":
                        certo1 = False
                    elif verificarm(n):
                        disciplina,indice = acharm(n)
                        disciplina = colchetesint(disciplina)
                        certo2 = True
                        print(disciplina)
                        print("Digite o novo nome da materia ou digite 1 para voltar")
                        disciplinanova=input()
                        if disciplinanova==1:
                            certo1==False
                        elif verificarm(disciplinanova):
                            print("Essa disciplina ja existe")
                        else:
                            acharm(disciplinanova)
                            editarm(indice,disciplina)
                            print("Nome trocado com sucesso")
            if op2 == 3:
                certo1 = True
                while certo1:
                    print("--------------------------------------------------------------------------")
                    print("Digite o nome da disciplina que deseja remover  "
                          "Ou digite 1 para abrir a lista de disciplinas ou 2 para voltar")
                    print("--------------------------------------------------------------------------")
                    n = input()
                    if n == "1":
                        listainicial = listam()
                        listafinal = colchetesint(listainicial)
                        print(listafinal)
                    elif n == "2":
                        certo1 = False
                    if verificarm(n):
                        disciplina, indice = acharm(n)
                        print(colchetesint(disciplina))
                        certo2 = True
                        while certo2:
                            print("Voce tem certeza que deseja remover essa disciplina?(sim/nao)")
                            confirmacao = input()
                            if confirmacao == "sim" or confirmacao == "Sim":
                                removerm(indice)
                                print("Disciplina removida com sucesso")
                                certo1 = False
                                certo2 = False
                            if confirmacao == "nao" or confirmacao == "Nao" or confirmacao == "Não" or confirmacao == "não":
                                certo2 = False
            if op2 == 4:
                print(colchetesint(listam()))
                input("Pressione ENTER para continuar")
            if op2 == 5:
                continuar = False
    if op1==3:
        print("Programa")
    if op1==4:
        print("Programa")
    if op1==5:
        print("Programa")
    if op1==6:
        finalizar=False
        print("Programa encerrado,Até Logo")