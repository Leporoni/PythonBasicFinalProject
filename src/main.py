from agenda.gerenciadores import GerenciadorContatos
from agenda.modelos import Contato
from agenda.enuns import TipoContato
import sys

gerenciador = GerenciadorContatos()

def exibir_contatos(contatos):
    for contato in contatos:
        print(" - {nomeContato}, {tipoContato}, {valorContato}".format(nomeContato=contato.nome,
                                                                       tipoContato=contato.tipo_contato,
                                                                       valorContato=contato.valor_contato))
    print(" * Total de Contatos: ", len(contatos))

def listar_contatos():
    print(" ** LISTA DE CONTATOS: ")
    try:
        contatos = gerenciador.listar_contatos()
        exibir_contatos(contatos)
    except:
        tipo_erro, valor_erro, traceback = sys.exc_info()
        print(" ** Houve um erro ao listar os contatos: ")
        print(tipo_erro)
        print(valor_erro)

def criar_novo_contato():
    print(" ** INCLUSÃO DE CONTATO: ")
    contato = Contato()
    contato.nome = input("Digite o nome do contato: ")
    tipo_contato = -1
    while tipo_contato not in [0, 1, 2]:
        tipo_contato = int(input("Digite o tipo do contato (0 = CELULAR, 1 = FIXO, 2 = EMAIL): "))
        contato.tipo_contato = TipoContato(tipo_contato)
        contato.valor_contato = input("Digite o valor da forma de contato: ")
        try:
            gerenciador.incluir_contato(contato)
        except:
            tipo_erro, valor_erro, traceback = sys.exc_info()
            print(" ** Houve um erro ao incluir o  novo contato: ")
            print(tipo_erro)
            print(valor_erro)

def pesquisar_contato_por_nome():
    print(" ** PESQUISA DE CONTATOS POR NOME: ")
    nome_contato = input("Digite o nome do contato a ser localizado: ")
    try:
        contatos = gerenciador.pesquisar_contato_por_nome(nome_contato)
        exibir_contatos(contatos)
    except:
        tipo_erro, valor_erro, traceback = sys.exc_info()
        print(" ** Houve um erro ao pesquisar os contatos: ")
        print(tipo_erro)
        print(valor_erro)

print(" ** BEM-VINDO! **")
while True:
    print("O que você deseja fazer? \n")
    print("1. Listar contatos...")
    print("2. Adicionar novo contato...")
    print("3. Pesquisar contato por nome...")
    print("4. Sair")
    print("\n")
    opcao = int(input("Opção selecionada -> "))
    if opcao == 1:
        listar_contatos()
    elif opcao == 2:
       criar_novo_contato()
    elif opcao == 3:
        pesquisar_contato_por_nome()
    elif opcao == 4:
        break
    else:
        print("* Opção inválida **")
print("Até a próxima ;)")