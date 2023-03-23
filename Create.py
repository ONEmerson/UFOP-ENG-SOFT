"""                                                   CREATE
----------------------------------------------------- CREATE -------------------------------------------"""
import mysql.connector
from datetime import datetime
from Connect import Connect
import Interface

class Create:
    def __init__(self):
        global nome, sala, assento, valor, tipo, data, hora, novaReservaMsgmLabel, tipo, data, dataIda, comando
        nome
        sala
        assento
        valor
        tipo
        data
        dataIda
        hora
        novaReservaMsgmLabel
        tipo = self.fazTipo()
        data = self.fazData()
        comando

        comando = f'INSERT INTO ingresso( nome_cliente,' \
                  f' sala,' \
                  f' assento,' \
                  f' valor,' \
                  f' tipo_entrada,' \
                  f' data,' \
                  f' hora)' \
                  f' VALUES("{nome.get()}",' \
                  f' {sala.get()},' \
                  f' "{assento.get()}",' \
                  f' {valor.get()},' \
                  f' "{tipo}",' \
                  f'"{dataIda}",' \
                  f' "{hora}")'
        return comando

        #       MODIFICADO ACIMA
        #Connect.cursor.execute(comando)
        #Connect.conexao.commit()  ## <<<< quando se edita o banco de dados

        Interface.novaReserva.novaReservaMsgmLabel.configure(text=f'\n_______________________________' \
                                            f'\nReserva realizada com sucesso' \
                                            f'\n_______________________________' \
                                            f'\n{"Assento:"} {assento.get():>40}' \
                                            f'\n{"Valor:"}{"R$: " + valor.get():>40}' \
                                            f'\n{"Nome:"}{nome_cliente.get():>40}' \
                                            f'\n{"Sala:"}{sala.get():>40}' \
                                            f'\n{"Tipo:"}{tipo:>40}' \
                                            f'\n' \
                                            f'\n=========Adcionado=========' \
                                            f'\n Data:__________ {dataEscrita.get():<7}' \
                                            f'\nHora:_________ {hora:<7}' \
                                            f'\n===========================')

    def fazTipo(self):
        v = int(valor.get())
        if (v > 10):
            tipo = "Inteira"
        elif (v == 10):
            tipo = "Meia"
        elif (v < 10 and v > 0):
            tipo = "Promocional"
        else:
            tipo = "Cortesia"

    def fazData(self):
        dataCrua = datetime.now()
        dataIda = f'{dataCrua:%y/%m/%d}'
        dataEscrita = f'{dataCrua:%d/%m/%y}'
        hora = f'{dataCrua:%H:%M:%S}'
        print(f'{dataIda, hora}')


'''------------------------------------------------------- CREATE FIM-------------------------------------------------'''
