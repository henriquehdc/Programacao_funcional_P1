from asyncio.windows_events import NULL
from optparse import Values
from pickle import FALSE
from tkinter import END, Button, Entry, Frame, Label, Toplevel,messagebox
import application
import sqlite3
import datetime

class funcs():
    
    def limpa_campos(self) :
        self.nome_entrada.delete(0,END)
        self.sobrenome_entrada.delete(0,END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('Prova_Parcial_1.db')
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def monta_tabelas(self):

        self.conecta_bd()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patient(
            PatientID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            LastName TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vaccine(
            VaccineID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            PatientID INTEGER NOT NULL,
            VaccineName TEXT NOT NULL,
            DoseDate TEXT NOT NULL,
            DoseNumber INTEGER,
            VaccineType TEXT NOT NULL,
            FOREIGN KEY(PatientID) REFERENCES Patient(PatientID)
        )
        """)

        self.conn.commit() 
        self.desconecta_bd()      

    def add_paciente(self):       
        self.Name = self.nome_entrada.get()
        self.LastName = self.sobrenome_entrada.get()

        self.conecta_bd()  
        self.cursor.execute('INSERT INTO Patient(Name,LastName) VALUES (?,?)', (self.Name,self.LastName))
        self.conn.commit() 
        self.desconecta_bd() 
        self.limpa_campos()

        messagebox.showinfo('Criação de Paciente','Paciente cadastrado!')
        
    def buscar_paciente(self):
        self.Name = self.nome_entrada2.get()
        self.LastName = self.sobrenome_entrada2.get()
        self.conecta_bd()  
        paciente = self.cursor.execute('SELECT v.VaccineName,v.VaccineType,v.DoseDate, v.DoseNumber from Patient p inner join Vaccine v on p.PatientID = v.PatientID WHERE Name =? AND LastName =?', (self.Name,self.LastName)).fetchall()
        for linha in paciente:
            self.lista_pa.insert("",END,values=linha)
        
        self.conn.commit() 
        self.desconecta_bd()    

    def limpa_campos2(self) :
        self.nome_entradaV.delete(0,END)
        self.sobrenome_entradaV.delete(0,END)    
        self.nome_vacina_entrada.delete(0,END)    
        self.tipo_vacina_entrada.delete(0,END)    
        self.data_dose_entrada.delete(0,END)    
        self.num_dose_entrada.delete(0,END)    

    def add_vacina(self):
        existe = self.existe_paciente
        if existe == -1:
            messagebox.showinfo('Adicionar vacina','Paciente não encontrado!')
        else:
            self.Name = self.nome_entradaV.get()
            self.LastName = self.sobrenome_entradaV.get()
            self.VaccineName = self.nome_vacina_entrada.get()
            self.DoseDate = self.data_dose_entrada.get()
            self.DoseNumber = self.num_dose_entrada.get()
            self.VaccineType = self.tipo_vacina_entrada.get()     
            self.conecta_bd()
            pacienteID = self.cursor.execute('SELECT (PatientID) from Patient WHERE Name = ? AND LastName = ?',(self.Name,self.LastName)).fetchone()
            self.cursor.execute('INSERT INTO Vaccine(PatientID,VaccineName,DoseDate,DoseNumber,VaccineType) VALUES (?,?,?,?,?)', (pacienteID[0],self.VaccineName,self.DoseDate,self.DoseNumber,self.VaccineType))
            self.limpa_campos2()
            self.conn.commit() 
            self.desconecta_bd() 

            messagebox.showinfo('Criação Vacina','Vacina cadastrada!')

    def deletar_paciente(self):
        existe = self.existe_paciente()
        
        if existe == -1:
            messagebox.showinfo('Deletar paciente','Paciente não encontrado!')
        else:    
            self.conecta_bd()  
            self.cursor.execute('DELETE FROM Patient WHERE Name= ? AND LastName = ?', (self.nome_entrada.get(),self.sobrenome_entrada.get()))
            self.conn.commit() 
            self.desconecta_bd() 
            self.limpa_campos()
            messagebox.showinfo('Deletar paciente','Paciente deletado!')

    def atualizar_paciente(self):
        self.lb_tituloA = Label(self.frame1,text='Atualizar dados do Paciente',bg='#b1cbde',font=('verdana',12,'bold'))
        self.lb_tituloA.place(relx=0.2,rely=0.6,relheight=0.1,relwidth=0.6)

        self.lb_nomeA = Label(self.frame1,text='Novo Nome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_nomeA.place(relx=0.01,rely=0.75,relheight=0.1,relwidth=0.2)

        self.nome_entradaA = Entry(self.frame1)
        self.nome_entradaA.place(relx=0.2,rely=0.75,relheight=0.10,relwidth=0.2)

        self.lb_sobrenomeA = Label(self.frame1,text='Novo Sobrenome',bg='#b1cbde',font=('verdana',10,'bold'))
        self.lb_sobrenomeA.place(relx=0.4,rely=0.75,relheight=0.1,relwidth=0.2)

        self.sobrenome_entradaA = Entry(self.frame1)
        self.sobrenome_entradaA.place(relx=0.6,rely=0.75,relheight=0.10,relwidth=0.4)

        self.bt_confirmaA = Button(self.frame1,text='Confirmar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.confirma_atualizar)
        self.bt_confirmaA.place(relx=0.05,rely=0.86,relheight=0.15,relwidth=0.12)

        self.bt_fecharA = Button(self.frame1,text='Fechar',bd=3,bg='#014c85',fg='white',font=('verdana',8,'bold'),command=self.deleta_atualizar)
        self.bt_fecharA.place(relx=0.2,rely=0.86,relheight=0.15,relwidth=0.12)

    def confirma_atualizar(self):
        existe = self.existe_paciente
        if existe == -1:
            messagebox.showinfo('Atualizar vacina','Paciente não encontrado!')
        else:
            self.conecta_bd()  
            self.cursor.execute('UPDATE Patient SET Name = ? ,LastName = ? WHERE Name= ? AND LastName = ?', (self.nome_entradaA.get(), self.sobrenome_entradaA.get(),self.nome_entrada.get(),self.sobrenome_entrada.get()))
            self.conn.commit() 
            self.desconecta_bd() 
            self.deleta_atualizar
            messagebox.showinfo('Atualização','Atualizado com sucesso!')

    def deleta_atualizar(self):
        self.lb_tituloA.destroy()
        self.lb_nomeA.destroy()
        self.nome_entradaA.destroy()
        self.lb_sobrenomeA.destroy()
        self.sobrenome_entradaA.destroy()
        self.bt_confirmaA.destroy()    
        self.bt_fecharA.destroy()

    def existe_paciente(self):

        self.conecta_bd()
        pacienteID = self.cursor.execute('SELECT (PatientID) from Patient WHERE Name = ? AND LastName = ?',(self.nome_entrada.get(),self.sobrenome_entrada.get())).fetchone()
        self.conn.commit() 
        self.desconecta_bd() 
        if pacienteID == None:
            return -1
        else:
            return pacienteID[0]    
