""" DELETE
--------------------------------------------------------- DELETE -------------------------------------------------"""
import Connect
import Create
import Interface
import Update
from Create import Create


class Delete:
    def __init__(self):
            match Update.tx:
                case 'Código':  # Código
                    cod = int(Interface.editarReserva.Descricao.get())
                    comando = f'DELETE FROM ingresso WHERE cod = {cod}'
                    Connect.cursor.execute(comando)
                    Connect.conexao.commit()  # <<< editar o banco de dados
                    Create.msgmConfirm.configure(text=f'Reservas de {Update.txt}: ({cod})\n apagada com sucesso!')
                    return 0
                case "Nome":  # Nome
                    comando = f'DELETE FROM ingresso WHERE nome_cliente = "{Interface.Descricao.get()}" AND sala="{Interface.DescricaoParaSala.get()}" AND assento="{Interface.DescricaoParaAssento.get()}"'
                    Connect.cursor.execute(comando)
                    Connect.conexao.commit()  # <<< editar o banco de dados
                    Connect.msgmConfirm.configure(
                        text=f'Reservas de: ( Nome {Interface.Descricao.get()}, Sala {Interface.DescricaoParaSala.get()}, Assento {Interface.DescricaoParaAssento.get()})\n apagada com sucesso!')
                    return 0
                case "Assento":  # Assento
                    comando = f'DELETE FROM ingresso WHERE assento = "{Interface.Descricao.get()}" AND sala = "{Interface.DescricaoParaSala.get()}"'
                    Connect.cursor.execute(comando)
                    Connect.conexao.commit()  # <<< editar o banco de dados
                    Create.msgmConfirm.configure(
                        text=f'Reservas de {Update.txt} {Interface.Descricao.get()}: ( Sala {Interface.DescricaoParaSala.get()} )\n apagada com sucesso!')
                    return 0
                case "Sala":  # Sala
                    comando = f'DELETE FROM ingresso WHERE sala = "{Interface.Descricao.get()}" AND assento = "{Interface.DescricaoParaAssento.get()}"'
                    Connect.cursor.execute(comando)
                    Connect.conexao.commit()  # <<< editar o banco de dados
                    Create.msgmConfirm.configure(
                        text=f'Reserva de {Update.txt} {Interface.Descricao.get()}: ( Assento {Interface.DescricaoParaAssento.get()} ) apagada com sucesso!')
                case _:
                    Create.msgmConfirm["text"] = f'Opção ({Update.txt}) não é válida.\nPor favor confira a escolha e tente novamente.'
                    return 0

        ##--------------------------------------------------- DELETE FIM -------------------------------------------
