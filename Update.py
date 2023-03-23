"""                                                 UPDATE
--------------------------------------------------- UPDATE -------------------------------------------"""
import Create
import Connect


class Update:
    def __init__(self):
        global txt
        match txt:
            case "Código":  # Código
                Create.fazTipo()
                Create.fazData()
                comando = f'UPDATE ingresso SET' \
                          f' cod = "{Create.codigo.get()}",' \
                          f' nome_cliente = "{Create.nome.get()}",' \
                          f' sala = "{Create.sala.get()}",' \
                          f' valor = "{Create.valor.get()}",' \
                          f'tipo_entrada = "{Create.tipo}",' \
                          f' assento = "{Create.assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE cod = "{int(Create.Descricao.get())}"'
                Connect.cursor.execute(comando)
                Connect.conexao.commit()  ##  <<<< editar o banco de dados

                #                    TENTATIVA CANCELAR ABAIXO
                #novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \ <<< [ MODIFICADO ABAIXO ]
                '''Interface.novaReserva.novaReservaMsgmLabel.configure(
                                                    f'\n\nAssento: {Create.assento.get()}' \
                                                    f'\nValor: R${Create.valor.get()}' \
                                                    f'\nNome: {Create.nome.get()}' \
                                                    f'\nSala: {Create.sala.get()}' \
                                                    f'\nTipo: {Create.tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')'''
                return 0

            case "Nome":  # Nome

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{Create.codigo.get()}",' \
                          f' nome_cliente = "{Create.nome.get()}",' \
                          f' sala = "{Create.sala.get()}",' \
                          f' valor = "{Create.valor.get()}",' \
                          f'tipo_entrada = "{Create.tipo}",' \
                          f' assento = "{Create.assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE nome_cliente = "{Create.Descricao.get()}" AND assento = "{Create.DescricaoParaSala.get()}" AND sala = "{Create.DescricaoParaAssento.get()}"'
                print(comando)
                Connect.cursor.execute(comando)
                Connect.conexao.commit()  ##  <<<< editar o banco de dados

                    # TENTATIVA CANCELAR ABAIXO
                '''Interface.novaReserva.novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {Create.assento.get()}' \
                                                    f'\nValor: R${Create.valor.get()}' \
                                                    f'\nNome: {Create.nome.get()}' \
                                                    f'\nSala: {Create.sala.get()}' \
                                                    f'\nTipo: {Create.tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')'''
                return 0

            case "Sala":  # Sala

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{Create.codigo.get()}",' \
                          f' nome_cliente = "{Create.nome.get()}",' \
                          f' sala = "{Create.sala.get()}",' \
                          f' valor = "{Create.valor.get()}",' \
                          f' tipo_entrada = "{Create.tipo}",' \
                          f' assento = "{Create.assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE sala = "{Create.Descricao.get()}" AND assento = "{Create.DescricaoParaAssento.get()}"'
                print(comando)
                Connect.cursor.execute(comando)
                Connect.conexao.commit()  ##  <<<< editar o banco de dados

                #                           TENTATIVA CANCELAR ABAIXO
                '''Interface.novaReserva.novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {Create.assento.get()}' \
                                                    f'\nValor: R${Create.valor.get()}' \
                                                    f'\nNome: {Create.nome.get()}' \
                                                    f'\nSala: {Create.sala.get()}' \
                                                    f'\nTipo: {Create.tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')'''
                return 0

            case "Assento":  # Assento

                Create.fazTipo()
                Create.fazData()

                comando = f'UPDATE ingresso SET' \
                          f' cod = "{Create.codigo.get()}",' \
                          f' nome_cliente = "{Create.nome.get()}",' \
                          f' sala = "{Create.sala.get()}",' \
                          f' valor = "{Create.valor.get()}",' \
                          f'tipo_entrada = "{Create.tipo}",' \
                          f' assento = "{Create.assento.get()}",' \
                          f' data = "{Create.dataIda}",' \
                          f' hora = "{Create.hora}"' \
                          f' WHERE assento = "{Create.Descricao.get()}" AND sala = "{Create.DescricaoParaSala.get()}"'
                Connect.execute(comando)
                Connect.conexao.commit()  ##  <<<< editar o banco de dados

                #                           TENTATIVA CANCELAR ABAIXO
                '''Interface.novaReserva.novaReservaMsgmLabel.configure(text=f'Dados atualizados com sucesso: ' \
                                                    f'\n\nAssento: {Create.assento.get()}' \
                                                    f'\nValor: R${Create.valor.get()}' \
                                                    f'\nNome: {Create.nome.get()}' \
                                                    f'\nSala: {Create.sala.get()}' \
                                                    f'\nTipo: {Create.tipo}' \
                                                    f'\n\n=======Adcionado=======' \
                                                    f'\nData:{Create.dataEscrita}' \
                                                    f'\nHora:{Create.hora}' \
                                                    f'\n=======================')'''
                return 0

            case _:

                #                           TENTATIVA CANCELAR ABAIXO
                #novaReservaMsgmLabel.configure( <<< [ MODIFICADO NA LINHA ABAIXO ]
                '''Interface.reservaEdit().configure(
                    text=f'Opção {txt}: --> {Create.Descricao.get()} <--\nnão é válida.\nPor favor confira a escolha \ne' \
                    f'\ntente novamente.')'''
                return 0

'''--------------------------------------------------- UPDATE FIM -------------------------------------------'''