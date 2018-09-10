from os.path import exists
from agenda.modelos import Contato
from agenda.enuns import TipoContato

class GerenciadorContatos:

    __contatos = []

    def listar_contatos(self):
        self.__contatos.clear()
        if exists("agenda.txt"):
            with open("agenda.txt", "r") as leitor:
                linhas = leitor.readlines()
                for linha in linhas:
                    informaçoes_contato = linha.split("|")
                    contato = Contato()
                    contato.nome = informaçoes_contato[0]
                    contato.tipo_contato = TipoContato(int(informaçoes_contato[1]))
                    contato.valor_contato = informaçoes_contato[2].replace("\n", "")
                    self.__contatos.append(contato)
        return self.__contatos

    def incluir_contato(self, contato):
        flag_arquivo = "w"
        if exists("agenda.txt"):
            flag_arquivo = "a"
        with open("agenda.txt", flag_arquivo) as escritor:
            escritor.write(contato.como_string())
            self.__contatos.append(contato)

    def pesquisar_contato_por_nome(self, nome_contato):
        if len(self.__contatos) == 0:
            self.listar_contatos()
        return list(filter(lambda contato: contato.nome.startswith(nome_contato), self.__contatos))