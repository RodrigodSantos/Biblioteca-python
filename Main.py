# Biblioteca
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
    else:
        print("\nDigite uma opção válida!")
        main()


def cadastrarLeitor():
 
    matricula = int(input('Digite sua matrícula:'))
    nome = str(input('Digite seu nome:'))
    cargo = int(input('Você é:\n1 - Aluno\n2 - Professor\n3 - Funcinário\n'))

    if cargo == 1:
        cargo = "Aluno"
    elif cargo == 2:
        cargo = "Professor"
    elif cargo == 3:
        cargo = "Funcionário"
    else:
        print("Cargo inválido, preencha novamente os dados:")
        return cadastrarLeitor()


    leitor = {
        "matricula": matricula,
        "nome": nome,
        "cargo": cargo,
        "status": "Ativo"
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
        "status": "Disponível",
        "id": id
    }

    livros.append(livro)
    print("Seu livro foi cadastrado!")
    print(livro)
    sair()

def buscarItem():

    item = input("Digite o titulo ou o id do livro:")
    for i in range(len(livros)):
        if livros[i]["titulo"] == item:
            print("Seu livro:")
            print(livros[i])
            sair()
        else:
            for j in range(len(livros)):
                if livros[j]["id"] == int(item):
                    print("Seu livro:")
                    print(livros[j])
                    sair()
                else:
                    print("Livro não encontrado, tente novamente")
                    sair()

def emprestarItem():
    
    titulo = input("Digite o titulo do livro que deseja pegar emprestado:")
    for i in range(len(livros)):
        if livros[i]["titulo"] == titulo:
            if livros[i]["status"] != "Disponível":
                print("Este item esta indisponivel!")
                sair()
            else:
                print("Seu livro:")
                print(livros[i])
                print("\nContinuando...\n")
    
    matricula = int(input("Digite sua matricula:"))
    for i in range(len(leitores)):
        if leitores[i]["matricula"] == matricula:
            if leitores[i]["status"] == "Ativo":
                print("Matricula ativa para emprestimo de itens!")
                print(leitores[i])
                print("\nContinuando...\n")
            else:
                print("Matricula suspensa para emprestimos de itens!")
                sair()

    data = int(input("Em qual dia deseja pegar o livro? (apenas o dia)"))
    diaDevolucao = data + 14
    if diaDevolucao > 30:
        diaDevolucao - 30

    confirmar = input("Deseja finalizar o emprestimo do item? [S/N]").lower
    if confirmar == 'n':
        print("Esprestimo cancelado!")
        sair()
    elif confirmar == 's':

        emprestimo = {
            "matricula": matricula,
            "titulo": titulo,
            "dia da retirada": data,
            "dia para devolucao": diaDevolucao 
        }
        emprestados.append(emprestimo)
        for i in range(len(livros)):
            if livros[i]["titulo"] == titulo:
#diminuir a quantidade de livros aqui


        print("Empréstimo comcluido com sucesso!")
        sair()
    else:
        print("Opção inválida, emprestimo cancelado, tente novamente.")
        sair()


    

def sair():
    escolha = str(input('Deseja sair da biblioteca: [S/N]')).lower()
    if escolha == 's':
        print('------------\nVolte sempre\n------------')
    else:
        main()

main()
    