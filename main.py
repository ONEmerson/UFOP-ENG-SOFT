""" -------------------------------------------------- inicialização -------------------------------------
 Terminal >> 1_ pip install mysql-connector-python <<<<<< para usar o MySQLl
 Terminal >> 1_ pip install requests <<<< para fazer interface"""
import Interface

"""--------------------------------------------------- funções -------------------------------------------"""


def duas_func_apagar(mensagens_para_deletar=None, confirme_delecoes=None):  # <<<<< CHAMA 2 FUNÇÕES
    mensagens_para_deletar()
    confirme_delecoes()


def duas_func_edit(mensagens_para_deletar=None, confirme_edicao=None):  # <<<<< CHAMA 2 FUNÇÕES MSGM2DEL E CONFIRM EDIT
    mensagens_para_deletar()
    confirme_edicao()


Interface()
'''------------------------------------------------------ Encerrado ------------------------------------------------'''
