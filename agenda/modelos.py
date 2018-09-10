from agenda.enuns import TipoContato

class Contato:
    """Representa uma entrada de contato"""
    __nome = ""
    __tipo_contato = TipoContato.TELEFONE_CELULAR
    __valor_contato = ""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def tipo_contato(self):
        return self.__tipo_contato

    @tipo_contato.setter
    def tipo_contato(self, tipo_contato):
        self.__tipo_contato = tipo_contato

    @property
    def valor_contato(self):
        return self.__valor_contato

    @valor_contato.setter
    def valor_contato(self, valor_contato):
        self.__valor_contato = valor_contato

    def como_string(self):
        return "{nomeContato}|{tipoContato}|{valorContato}\n".format(nomeContato=self.__nome,
                                                                     tipoContato=self.__tipo_contato.value,
                                                                     valorContato=self.__valor_contato)