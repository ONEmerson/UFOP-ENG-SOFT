"""
                                                          READ
#-------------------------------------------------------- READ ------------------------------------------------------"""
import mysql.connector
import Connect

class Read:
    def __init__(self):
        self.comando = f'SELECT * FROM ingresso;'
        self.Connect.cursor.execute(self.comando)
        #Connect.cursor.execute(comando)#      <<< [ MODIFICADO NA LINHA A CIMA ]
        resultado = Connect.cursor.fetchall()
        #resultado = Connect.cursor.fetchall()  # <<<< ler o banco de dados [ MODIFICADO NA LINHA DE CIMA ]
        print(resultado)
        Connect.exibir(self, resultado)
        #Interface.exibir(resultado) <<< [ MODIFICADO NA LINHA DE CIMA]

    def le_ingressos(self):
        self.comando


    """print("Numero de linhas retornadas: ", cursor.rowcount)
        for resultados in resultado:
            print("cod:", resultados[0])
            print("nome:", resultados[1])
            print("sala:", resultados[2])
            print("assento:", resultados[3])
            print("valor:", resultados[4])
            print("tipo: ", resultados[5])
            print("data:", resultados[6])
            print("hora:", resultados[7])

    --------------------------------------------------- READ FIM -------------------------------------------"""