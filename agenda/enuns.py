from enum import Enum, unique

@unique
class TipoContato(Enum):
    TELEFONE_CELULAR = 0
    TELEFONE_FIXO = 1
    EMAIL = 2