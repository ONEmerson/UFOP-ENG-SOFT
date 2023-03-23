from tkinter import *  # <<<<<< para usar o TKinter (interface)
import customtkinter
from tkinter import ttk  # <<<<<< para usar comboBox, (janela com escolhas clicáveis)
from Create import Create
from Read import Read
from Update import Update
from Delete import Delete
import Connect

class Interface:

    def __init__(self):
        self.comboOpcao = None
        self.usuario = 'Emerson'
        self.passe = 'one'
        self.opcao_modificar = ["Assento", "Código", "Nome", "Sala"]

    #--------------------------------------------------- TELA LOG IN ------------------------------------------
    def logIn(self):
        self.janelaLogIn = customtkinter.CTkToplevel()
        self.janelaLogIn.title("Janela Log In")
        self.fontePadrao = ("Comic Sans MS", 18)
        self.janelaLogIn.geometry("350x300")
        self.janelaLogIn.resizable()


        titulo = customtkinter.CTkLabel(self.janelaLogIn, text="Dados do Administrador",font=("Roboto", 20))
        titulo.pack()
        nomeLog = customtkinter.CTkEntry(self.janelaLogIn, placeholder_text="Usuário", font=("",15))
        nomeLog.pack(pady=12, padx=10)

        senha = customtkinter.CTkEntry(self.janelaLogIn, placeholder_text="Senha", show="*", font=("",15))
        senha.pack(pady=12, padx=10)


        BotaoAutenticar = customtkinter.CTkButton(self.janelaLogIn, text="Autenticar", font=("Arial", 15), command=self.verificaSenha)
        BotaoAutenticar.pack(pady=12)
        lembrar = customtkinter.CTkCheckBox(self.janelaLogIn, text="Lembrar nessa sessão")
        lembrar.pack(pady=8)

        mensagem = customtkinter.CTkLabel(self.janelaLogIn, text="", font=self.fontePadrao)
        mensagem.pack(pady=15)

    #Método verificar senha
    def verificaSenha(self, mensagem=None):
        if (self.nomeLog != self.usuario):
            mensagem.configure(text="Usuário inválido",text_color='red')

        elif(self.senha.get() != self.passe):
            mensagem.configure(text="Senha incorreta",text_color='red')
        else:
            if (self.log == "Apagar"):
                self.apagando()
            elif (self.log == "Editar"):
                self.editando()
            mensagem.configure(text="Autenticado",text_color='green')
            self.janelaLogIn.destroy()

    ##--------------------------------------------------- TELA LOG IN FIM --------------------------------------
    ##--------------------------------------------------- JANELA NOVA RESERVA -------------------------------------------

    def novaReserva(self):##<<<<< INTERFACE NOVA JANELA
        self.janelaEntradaDados = customtkinter.CTkToplevel()
        self.janelaEntradaDados.title("Nova Reserva")
        self.fontePadrao = ("Comic Sans MS", "10")
        self.janelaEntradaDados.geometry("250x505")
        # --------------------------------- CONTAINERS ENTRADA DE DADOS --------------------------------

        titulo = customtkinter.CTkLabel(self.janelaEntradaDados, text="NOVA RESERVA",font=("Agency FB", 15, "bold"))
        titulo.pack()

        nome = customtkinter.CTkEntry(self.janelaEntradaDados, placeholder_text="Nome")
        nome.pack(pady=12, padx=10)

        sala = customtkinter.CTkEntry(self.janelaEntradaDados, placeholder_text="Sala")
        sala.pack(pady=12, padx=10)

        assento = customtkinter.CTkEntry(self.janelaEntradaDados, placeholder_text="Assento")
        assento.pack(pady=12, padx=10)

        valor = customtkinter.CTkEntry(self.janelaEntradaDados, placeholder_text="Valor")
        valor.pack(pady=12, padx=10)

        botaoOkEntradaDados = customtkinter.CTkButton(self.janelaEntradaDados, text="Ok", font=("Comics Sans MS", 10, "bold"),command=Create.Create)
        botaoOkEntradaDados.pack(pady=12)

        novaReservaMsgmLabel = customtkinter.CTkLabel(self.janelaEntradaDados, text="Campo de confirmação:")
        novaReservaMsgmLabel.pack(pady=2)

    #--------------------------------------------------- JANELA NOVA RESERVA FIM -------------------------------------

    def confirme_edicao(self):##<<<<< INTERFACE MENSAGEM RESERVA APAGADA
        msgmConfirm = customtkinter.CTkLabel(self.janelaApagarReserva, text="")
        msgmConfirm.place(x=20,y=180)
        Update.Update()

    def confirme_delecoes(self): ##<<<<< INTERFACE MENSAGEM APAGAR RESERVA
        log = "Apagar"
        msgmConfirm = customtkinter.CTkLabel(self.janelaApagarReserva, text=" Obrigatório preencher todos os campos ")
        msgmConfirm.place(x=20,y=180)
        Delete.Delete()


    def mensagem_edicao(self, botao=None): ##<<<<< INTERFACE MENSAGEM E NOVO PARAMETRO PARA A ESCOLHA EDITAR RESERVA
        txt = self.comboOpcao.get()

        Descricao = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text=txt, font=("Arial", 16))
        Descricao.place(x=170, y=50)

        if(txt == "Sala"):
            DescricaoParaAssento = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Assento", \
                                                          font=("Arial", 16))
            DescricaoParaAssento.place(x=170, y=80)

        elif (txt == "Assento"):
            DescricaoParaSala = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Sala", \
                                                       font=("Arial", 16))
            DescricaoParaSala.place(x=170, y=80)

        elif(txt == "Nome"):
            DescricaoParaSala = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Assento",\
                                                       font=("Arial", 16))
            DescricaoParaSala.place(x=170, y=80)
            DescricaoParaAssento = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Sala",\
                                                          font=("Arial", 16))
            DescricaoParaAssento.place(x=170, y=110)

        botao.destroy()
        botao2 = customtkinter.CTkButton(self.janelaApagarReserva, text="EDITAR", command=self.reservaEdit)
        botao2.place(x=100, y=220)

    def mensagens_para_deletar(self, botao=None): ##<<<<< INTERFACE MENSAGEM DE APAGAR RESERVA
        txt = self.comboOpcao.get()

        Descricao = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text=txt, font=("Arial", 16))
        Descricao.place(x=170, y=50)


        if(txt == "Sala"):
            DescricaoParaAssento = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Assento",\
                                                          font=("Arial", 16))
            DescricaoParaAssento.place(x=170, y=80)

        elif (txt == "Assento"):
            DescricaoParaSala = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Sala", font=("Arial", 16))
            DescricaoParaSala.place(x=170, y=80)

        elif(txt == "Nome"):
            DescricaoParaSala = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Sala",\
                                                       font=("Arial", 16))
            DescricaoParaSala.place(x=170, y=80)
            DescricaoParaAssento = customtkinter.CTkEntry(self.janelaApagarReserva, placeholder_text="Assento",\
                                                          font=("Arial", 16))
            DescricaoParaAssento.place(x=170, y=110)

        botao.destroy()
        botao2 = customtkinter.CTkButton(self.janelaApagarReserva, text="APAGAR", command=self.confirme_delecoes)
        botao2.place(x=100, y=220)


    #--------------------------------------------------- APAGAR RESERVA ---------------------------------------

    def editando(self): ##<<<<< INTERFACE ESCOLHER PARAMETRO PARA EDITAR RESERVA
        janelaApagarReserva = customtkinter.CTkToplevel()
        janelaApagarReserva.geometry("350x280")
        janelaApagarReserva.resizable(True, True)
        janelaApagarReserva.title("Editor de RESERVAS")

        comboLabel = customtkinter.CTkLabel(janelaApagarReserva, text=" Editar a partir de: ", font=("Arial", 16))
        comboLabel.place(x=30, y=20)

        comboOpcao = customtkinter.CTkComboBox(janelaApagarReserva, values=self.opcao_modificar, font=("", 15))
        comboOpcao.place(x=170, y=20)

        txt = comboOpcao.get()

        botao = customtkinter.CTkButton(janelaApagarReserva, text="Confirmar escolha", font=("", 15), \
                                        command=self.mensagem_edicao)
        botao.place(x=100, y=220)

    def apagando(self): ##<<<<< INTERFACE NOVA JANELA APAGAR RESERVA
        janelaApagarReserva = customtkinter.CTkToplevel()
        janelaApagarReserva.geometry("350x280")
        janelaApagarReserva.resizable(True, True)
        janelaApagarReserva.title("Apagar reserva")

        comboLabel = customtkinter.CTkLabel(janelaApagarReserva, text=" Apagar a partir de: ", font=("Arial", 16))
        comboLabel.place(x=30, y=20)

        comboOpcao = customtkinter.CTkComboBox(janelaApagarReserva, values=self.opcao_modificar, font=("", 15))
        comboOpcao.place(x=170, y=20)

        txt=comboOpcao.get()

        botao = customtkinter.CTkButton(janelaApagarReserva, text="Confirmar escolha", font=("", 15), \
                                        command=self.mensagens_para_deletar)
        botao.place(x=100, y=220)

    #--------------------------------------------------- APAGAR RESERVA FIM ---------------------------------------

    def reservaEdit(self): ##<<<<< INTERFACE NOVA JANELA EDITAR RESERVA
        janelaEnstradaDados = customtkinter.CTkToplevel()
        janelaEnstradaDados.title("Editor de Reservas")
        janelaEnstradaDados.geometry("250x545")

        titulo = customtkinter.CTkLabel(janelaEnstradaDados, text="EDITOR DE RESERVA", font=("Agency FB", 20, "bold"))
        titulo.pack(pady=5)

        codigo = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo CÓDIGO")
        codigo.pack(pady=12, padx=10)

        nome = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo NOME")
        nome.pack(pady=12, padx=10)

        sala = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo SALA")
        sala.pack(pady=12, padx=10)

        assento = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Novo ASSENTO")
        assento.pack(pady=12, padx=10)

        valor = customtkinter.CTkEntry(janelaEnstradaDados, placeholder_text="Valor")
        valor.pack(pady=12, padx=10)


        botaoOkEntradaDados = customtkinter.CTkButton(janelaEnstradaDados, text="Ok", command=self.confirme_delecoes)
        botaoOkEntradaDados.pack(pady=10)

        novaReservaMsgmLabel = customtkinter.CTkLabel(janelaEnstradaDados, text="Campo de confirmação:")
        novaReservaMsgmLabel.pack()

    #----------------------------------------------------------------------------------------------------------
    def apagarReserva(self):
        log = "Apagar"
        self.logIn()

    def editarReserva(self):
        log = "Editar"
        self.logIn()
    #----------------------------------------------------------------------------------------------------------


    #--------------------------------------------------- TREEVIEW INICIO---------------------------------------
    def exibir(self, resultado): ##<<<<< INTERFACE NOVA JANELA EXIBIR TABELA DE RESERVAS
        janelaTREEVIEW = resultado.customtkinter.CTkToplevel()
        janelaTREEVIEW.title("Tabela")

        tree = resultado.ttk.Treeview(janelaTREEVIEW, columns=("column1", "column2", "column3", "column4",
                                                     "column5", "column6", "column7", "column8", "column9"),
                                 show='headings')

        tree.column("column1", width=90, minwidth=14, stretch=YES)
        tree.heading("#1", text='Código')

        tree.column("column2", width=160, minwidth=40, stretch=YES)
        tree.heading("#2", text='Nome')

        tree.column("column3", width=75, minwidth=12, stretch=YES)
        tree.heading("#3", text='Sala')

        tree.column("column4", width=100, minwidth=18, stretch=YES)
        tree.heading("#4", text='Assento')

        tree.column("column5", width=70, minwidth=14, stretch=YES)
        tree.heading("#5", text='Valor')

        tree.column("column6", width=80, minwidth=12, stretch=YES)
        tree.heading("#6", text='Tipo')

        tree.column("column7", width=100, minwidth=11, stretch=YES)
        tree.heading("#7", text='Data')

        tree.column("column8", width=55, minwidth=12, stretch=YES)
        tree.heading("#8", text='Hora')

        tree.column("column9", width=95, minwidth=12, stretch=YES)
        tree.heading("#9", text='cliente_cod')

        print(resultado)
        tree.grid(row=0, column=0)
        for (c,n,s,a,v,t,d,h) in resultado:
            tree.insert("", END, values= (f'{c:^20}',f'{n:^40}',f'{s:^20}',
                                          f'{a:^30}',f'{v:^20}',f'{t:^20}',
                                          f'{d:        %d/%m/%y}',f'{h:}',
                                          ))#f'{cc:^20}'))


"""--------------------------------------------------- TREEVIEW FIM -----------------------------------------------

--------------------------------------------------- JANELA PRINCIPAL -------------------------------------------


     ****************************************************************************************************************
     ************************************************       TK INTER        *****************************************
     ****************************************************************************************************************
"""
customtkinter.set_appearance_mode("light")
Color = 1
Dark = 0
customtkinter.set_default_color_theme("green")

def setMode(self, Dark):
    if(Dark.get() == 0):
        customtkinter.set_appearance_mode("light")
        self.Dark.set = 1
    else:
        customtkinter.set_appearance_mode("dark")
        self.Dark.set = 0

def setColor(self, color):
    if(color.get()== 0):
        customtkinter.set_default_color_theme("green")
        color.configure(text='Cor Azul')
        self.color.set = 1
    else:
        customtkinter.set_default_color_theme("blue")
        self.color.configure(text='implementação futura')
        self.color.set = 0

"""------------------------------------------------------------ TEMA ----------------------------------------------"""

root = customtkinter.CTk()
root.geometry("550x400")
fontePadrao = ("Arial", "10")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady="20", padx=60, fill="both", expand=True)

root.title("CInema")

label = customtkinter.CTkLabel(master=frame, text="Cinema dus Film", font=("Roboto", 20))
label.pack(pady=12, padx=10)


texto_espaco = customtkinter.CTkLabel(master=frame, text="", width=14, height=2)
texto_espaco.pack()

botao1 = customtkinter.CTkButton(master=frame, text="Nova RESERVA ", command=Create)
botao1.pack(pady=12, padx=10)

botao2 = customtkinter.CTkButton(master=frame, text="Apagar RESERVA", command=Interface.apagarReserva)
botao2.pack(pady=12, padx=10)

botao3 = customtkinter.CTkButton(master=frame, text="Editar RESERVA", command=Interface.editarReserva)
botao3.pack(pady=12, padx=10)

botao4 = customtkinter.CTkButton(master=frame, text="ExibirRESERVAS", command=Read)
botao4.pack(pady=12, padx=10)

mode = customtkinter.CTkCheckBox(master=frame, text="Dark Mode", command=setMode)
mode.pack(side=LEFT,pady=12, padx=10)

color = customtkinter.CTkSwitch(master=frame, text="Cor Azul", text_color="blue", command=setColor)

color.pack(side=LEFT,pady=12, padx=10)

root.mainloop()

Connect.cursor.close()
Connect.conexao.close()
#       modificado acima
#Connect.cursor.close()
#Connect.conexao.close()
print("\nConexão encerrada com sucesso!!")
print("\nFim da classe Interface")
"""------------------------------------------- Janela principal FIM ------------------------------------------------"""
