from email.mime import image
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, PhotoImage, Scrollbar, ttk
from turtle import bgcolor
from funcs import funcs

window = tk.Tk()

class Application(funcs):

    def __init__(self):
       self.window= window
       self.tela()
       self.frames()
       self.widgets_frame1()
       self.widgets_frame2()
       self.monta_tabelas()
       window.mainloop()

    def tela(self):
        self.window.title('Cadastro de Pacientes e Vacinas!')  
        self.window.geometry('750x500')
        self.window.resizable(True ,True)
        self.window.minsize(width=700,height=400)
        self.bg = PhotoImage(file="img\Hospital.png")
        self.bg_label = Label(self.window, image=self.bg)
        self.bg_label.place(relx=0, rely=0,relwidth=1, relheight=1)
        
    def frames(self):
        self.frame1= Frame(self.window,bd=4,bg='#b1cbde',highlightbackground='#5156ed', highlightthickness=3)
        self.frame1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.4)

        self.frame2= Frame(self.window,bd=4,bg='#b1cbde',highlightbackground='#5156ed', highlightthickness=3)
        self.frame2.place(relx=0.05,rely=0.55,relwidth=0.9,relheight=0.4)
      
    def widgets_frame1(self):
        self.abas= ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.aba1.configure(background="#b1cbde")
        self.aba2.configure(background="#b1cbde")

        self.abas.add(self.aba1, text='Cadastro')
        self.abas.add(self.aba2, text='Listar Dados')

        self.abas.place(relx=0, rely=0,relwidth=0.98,relheight=0.98)
        #Botões
        self.bt_cadastrar = Button(self.aba1,text='Cadastrar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'), command=self.add_paciente)
        self.bt_cadastrar.place(relx=0.12,rely=0.4,relheight=0.15,relwidth=0.12)

        self.bt_limpar = Button(self.aba1,text='Limpar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.limpa_campos)
        self.bt_limpar.place(relx=0.27,rely=0.4,relheight=0.15,relwidth=0.12)


        self.bt_att = Button(self.aba1,text='Atualizar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.atualizar_paciente)
        self.bt_att.place(relx=0.68,rely=0.4,relheight=0.15,relwidth=0.12)

        self.bt_del = Button(self.aba1,text='Deletar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.deletar_paciente)
        self.bt_del.place(relx=0.8,rely=0.4,relheight=0.15,relwidth=0.12)

        #Labels
        self.lb_titulo = Label(self.aba1,text='Cadastro do Paciente',bg='#b1cbde',font=('verdana',12,'bold'))
        self.lb_titulo.place(relx=0.35,rely=0.02,relheight=0.1,relwidth=0.3)

        self.lb_nome = Label(self.aba1,text='Nome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_nome.place(relx=0.01,rely=0.2,relheight=0.1,relwidth=0.1)

        self.nome_entrada = Entry(self.aba1)
        self.nome_entrada.place(relx=0.12,rely=0.2,relheight=0.10,relwidth=0.2)

        self.lb_sobrenome = Label(self.aba1,text='Sobrenome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_sobrenome.place(relx=0.3,rely=0.2,relheight=0.1,relwidth=0.15)

        self.sobrenome_entrada = Entry(self.aba1)
        self.sobrenome_entrada.place(relx=0.47,rely=0.2,relheight=0.10,relwidth=0.5)

        #### ABA2  #####

        self.lb_titulo2 = Label(self.aba2,text='Buscar os dados do paciente',bg='#b1cbde',font=('verdana',12,'bold'))
        self.lb_titulo2.place(relx=0.2,rely=0.02,relheight=0.1,relwidth=0.5)

        self.lb_nome2 = Label(self.aba2,text='Nome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_nome2.place(relx=0.01,rely=0.2,relheight=0.1,relwidth=0.1)

        self.nome_entrada2 = Entry(self.aba2)
        self.nome_entrada2.place(relx=0.12,rely=0.2,relheight=0.10,relwidth=0.2)

        self.lb_sobrenome2 = Label(self.aba2,text='Sobrenome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_sobrenome2.place(relx=0.3,rely=0.2,relheight=0.1,relwidth=0.15)

        self.sobrenome_entrada2 = Entry(self.aba2)
        self.sobrenome_entrada2.place(relx=0.47,rely=0.2,relheight=0.10,relwidth=0.3)   

        self.bt_buscar = Button(self.aba2,text='Buscar Dados',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.buscar_paciente)
        self.bt_buscar.place(relx=0.8,rely=0.18,relheight=0.15,relwidth=0.18)

        self.lista_pa = ttk.Treeview(self.aba2,height=3,columns=('col1','col2','col3','col4'))
        self.lista_pa.heading("#0",text="")
        self.lista_pa.heading("#1",text="Nome Vacina")
        self.lista_pa.heading("#2",text="Tipo Vacina")
        self.lista_pa.heading("#3",text="Data Dose")
        self.lista_pa.heading("#4",text="Num. Dose")

        self.lista_pa.column("#0",width=1)
        self.lista_pa.column("#1",width=200)
        self.lista_pa.column("#2",width=150)
        self.lista_pa.column("#3",width=125)
        self.lista_pa.column("#4",width=125)

        self.lista_pa.place(relx=0.01,rely=0.35,relwidth=0.95,relheight=0.65)

        self.scroolLista = Scrollbar(self.aba2, orient='vertical')
        self.lista_pa.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.35,relwidth=0.04,relheight=0.65)


    def widgets_frame2(self):
        #Botões
        self.bt_cadastrarV = Button(self.frame2,text='Cadastrar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'), command=self.add_vacina)
        self.bt_cadastrarV.place(relx=0.01,rely=0.8,relheight=0.15,relwidth=0.12)

        self.bt_limparV = Button(self.frame2,text='Limpar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.limpa_campos2)
        self.bt_limparV.place(relx=0.15,rely=0.8,relheight=0.15,relwidth=0.12)


        #Labels
        self.lb_titulo1 = Label(self.frame2,text='Cadastro de Vacinas',bg='#b1cbde',font=('verdana',12,'bold'))
        self.lb_titulo1.place(relx=0.35,rely=0.02,relheight=0.1,relwidth=0.3)

        self.lb_titulo2 = Label(self.frame2,text='Dados do Paciente',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_titulo2.place(relx=0.35,rely=0.15,relheight=0.1,relwidth=0.3)

        self.lb_nomeV = Label(self.frame2,text='Nome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_nomeV.place(relx=0.01,rely=0.32,relheight=0.1,relwidth=0.1)

        self.nome_entradaV = Entry(self.frame2)
        self.nome_entradaV.place(relx=0.12,rely=0.32,relheight=0.10,relwidth=0.2)

        self.lb_sobrenomeV = Label(self.frame2,text='Sobrenome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_sobrenomeV.place(relx=0.3,rely=0.32,relheight=0.1,relwidth=0.15)

        self.sobrenome_entradaV = Entry(self.frame2)
        self.sobrenome_entradaV.place(relx=0.47,rely=0.32,relheight=0.10,relwidth=0.5)    

        self.lb_titulo3 = Label(self.frame2,text='Dados da vacina',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_titulo3.place(relx=0.35,rely=0.44,relheight=0.1,relwidth=0.3)
        
        self.lb_nome_vacina = Label(self.frame2,text='Nome vacina',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_nome_vacina.place(relx=0.001,rely=0.56,relheight=0.1,relwidth=0.2)

        self.nome_vacina_entrada = Entry(self.frame2)
        self.nome_vacina_entrada.place(relx=0.2,rely=0.56,relheight=0.10,relwidth=0.2) 

        self.lb_tipo_vacina = Label(self.frame2,text='Tipo vacina',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_tipo_vacina.place(relx=0.4,rely=0.56,relheight=0.1,relwidth=0.2)

        self.tipo_vacina_entrada = Entry(self.frame2)
        self.tipo_vacina_entrada.place(relx=0.6,rely=0.56,relheight=0.10,relwidth=0.3) 

        self.lb_data_dose = Label(self.frame2,text='Data Dose',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_data_dose.place(relx=0.001,rely=0.68,relheight=0.1,relwidth=0.2)

        self.data_dose_entrada = Entry(self.frame2)
        self.data_dose_entrada.place(relx=0.2,rely=0.68,relheight=0.10,relwidth=0.2) 

        self.lb_num_dose = Label(self.frame2,text='Num. Dose',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_num_dose.place(relx=0.4,rely=0.68,relheight=0.1,relwidth=0.2)

        self.num_dose_entrada = Entry(self.frame2)
        self.num_dose_entrada.place(relx=0.6,rely=0.68,relheight=0.10,relwidth=0.3) 

        
         