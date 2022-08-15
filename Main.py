from random import randint
leitores = []
livros = []
emprestados = []


def main():
    print('O que você deseja?\n[ 1 ]Cadastrar leitores\n[ 2 ]Cadastrar itens\n[ 3 ]Buscar item\n[ 4 ]Realizar empréstimo de item\n[ 5 ]Devolver item\n[ 6 ]Listar itens disponíveis\n[ 7 ]Sair da biblioteca')
    escolha = int(input('\nQual a sua opção: '))
    if escolha == 1:
        cadastrarLeitor()
    elif escolha == 2:
        cadastrarLivro()
    elif escolha == 3:
        buscarItem()
    elif escolha == 4:
        emprestarItem()
    elif escolha == 5:
        devolverItem()
    elif escolha == 6:
        listarItensDisponiveis()
    elif escolha == 7:
        return print('------------\nVolte sempre\n------------')
    else:
        print("\nDigite uma opção válida!")
        main()

def cadastrarLeitor():
 
    matricula = int(input('Digite sua matrícula:'))
    nome = str(input('Digite seu nome:'))
    cargo = int(input('Você é:\n1 - Aluno\n2 - Professor\n3 - Funcinário\n'))

    if cargo == 1:
        cargo = "aluno"
    elif cargo == 2:
        cargo = "professor"
    elif cargo == 3:
        cargo = "funcionário"
    else:
        print("Cargo inválido, preencha novamente os dados:")
        return cadastrarLeitor()


    leitor = {
        "matricula": matricula,
        "nome": nome,
        "cargo": cargo,
        "status": "ativo"
    }
    
    leitores.append(leitor)
    sair()

def cadastrarLivro():

    titulo = str(input("Digite o titúlo do livro:"))
    quant = int(input("Digite a quantidade de volumes que deseja cadastrar:"))
    id = randint(0, 99999)

    livro = {
        "titulo": titulo,
        "quantidade": quant,
        "status": "disponivel",
        "id": id
    }

    livros.append(livro)
    print("Seu livro foi cadastrado!")
    print(livro)
    sair()

def buscarItem():
    item = input("Digite o titulo ou o id do livro:")
    buscarLivro(item)
    sair()

def emprestarItem():
    
    item = input("Digite o titulo ou id do livro que deseja pegar emprestado:")
    x = buscarLivro(item)
    if livros[x]["status"] == "indisponivel":
        print("Este item esta indisponivel!")
        sair()
    elif livros[x]["status"] == "disponivel":
        matricula = int(input("Digite sua matricula:"))
        y = buscarMatricula(matricula)
        if leitores[y]["status"] == "suspenso":
            print("Matricula temporariamente suspensa!")
            sair()
        elif leitores[y]["status"] == "ativo":
            data = int(input("Em qual dia deseja pegar o livro? (apenas o dia)"))
            escolha = input("Finalizar emprestimo do item: [S/N]").lower()
            if escolha == "s":
                emprestar(x, y, data)
            else:
                print("Emprestimo cancelado!")
                sair()

def buscarMatricula(x):
    for i in range(len(leitores)):
        if leitores[i]["matricula"] == x:
            print(leitores[i])
            return i
    print("Matricula não encontrada!")
    sair()

def buscarLivro(x):
    for i in range(len(livros)):
        if livros[i]["titulo"] == x:
            print("Seu livro:")
            print(livros[i])
            return i
    for i in range(len(livros)):       
        if livros[i]["id"] == int(x):
            print("Seu livro:")
            print(livros[i])
            return i
    print("Livro não encontrado!")
    sair()

def emprestar(x, y, z):
# x == posicao na lista de livros
# y == posicao na lista de leitores
# z == data de retirada
    diaDevolucao = z + 14
    if diaDevolucao > 30:
        diaDevolucao - 30

    livros[x]["quantidade"] -= 1
    if livros[x]["quantidade"] < 1:
        livros[x]["status"] = "indisponivel"

    emprestimo = {
        "titulo": livros[x]["titulo"],
        "id": livros[x]["id"],
        "matricula": leitores[y]["matricula"],
        "dataRetirada": z,
        "dataDevolucao": diaDevolucao
    }
    emprestados.append(emprestimo)
    print("Empréstimo comcluido com sucesso!")
    sair()
    
def devolverItem():
    matricula = int(input("Digite sua matricula:"))
    if emprestados == []:
        print("Nenhum livro emprestado com essa matricula")
        sair()
    else:
        for i in range(len(emprestados)):
            if emprestados[i]["matricula"] == matricula:
                print("Matricula encontrada!")
                print("Item:\n{}".format(emprestados[i]))
            else:
                print("Nenhum livro emprestado com essa matricula!")
                sair()

    titulo = input("Digite o titulo que deseja devolver:")
    for i in range(len(emprestados)):
        if emprestados[i]["titulo"] == titulo:
            print("Item:{}" .format(emprestados[i]))
            escolha = input("Confirmar? [S/N]").lower()
            if escolha =="s":
                emprestados.remove(emprestados[i])
                for x in range(len(livros)):
                    if livros[x]["titulo"] == titulo:
                        livros[x]["quantidade"] += 1
                        if livros[x]["quantidade"] > 0:
                            livros[x]["status"] = "disponivel"
                        print("Devolução concluida com sucesso!")
                        sair()

def listarItensDisponiveis():
    if livros == []:
        print("Sem livros disponiveis!")
        sair()
    else:
        for i in range(len(livros)):
            if livros[i]["status"] == "disponivel":
                print(livros[i])   
        sair()                   

def sair():
    escolha = str(input("Deseja sair da biblioteca: [S/N]")).lower()
    if escolha == 's':
        print('------------\nVolte sempre\n------------')
    else:
        main()


main()
