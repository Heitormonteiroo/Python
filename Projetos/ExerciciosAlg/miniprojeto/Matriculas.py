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
    condicao=True
    while len(linhas)>i:
        linha=linhas[i].split()
        print(linha)
        if linha[3]==cpf:
            condicao=False
        i+=1
    fp.close()
    return condicao
def achar(cpf):
    fp=open("Alunos.csv","r")
    linhas=fp.readlines()

def lista():
    fp=open("Alunos.csv","r")
    linhas=fp.readlines()
    fp.close()
    return linhas


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
                        if verificar(cpf)==False:
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
                    print("Digite 1 para abrir a lista de alunos ou digite o cpf")
                    n=input()
                    if n=="1":
                        listainicial=lista()
                        listafinal=colchetesint(listainicial)
                        print(listafinal)
                    else:
                        
            if op2==5:
                continuar=False
