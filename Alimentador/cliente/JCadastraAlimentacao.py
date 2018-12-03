#coding: utf-8

from Tkinter import *
import json
import moduloCliente
import JAlimentacoes
from datetime import datetime, time

class JCadastraAlimentacao:
    
    def __init__(self, root, pai, host):
        self.myRoot = root
        self.myRoot.title("Cadastro de Alimentação")
        self.frame = Frame(root)
        self.frame.pack()
        self.pai = pai
	self.host = host

        self.txtDia = Label(self.frame, text="Dia: ", height=2,width=12)
        self.txtDia.grid(row=1,column=1)

        self.dia = Entry(self.frame)
        now = datetime.now()
        self.dia.insert(END,now.strftime("%d/%m/%Y"))
        self.dia.grid(row=1,column=2)

        self.txtHora = Label(self.frame, text="Hora: ", height=2,width=12)
        self.txtHora.grid(row=2,column=1)

        self.hora = Entry(self.frame)
        self.hora.insert(END,now.strftime("%H:"))
        self.hora.grid(row=2,column=2)

        self.txtTanque = Label(self.frame, text="Tanque: ", height=2,width=12)
        self.txtTanque.grid(row=3,column=1)

        self.tanque = Entry(self.frame)
        self.tanque.grid(row=3,column=2)

        self.txtQntde = Label(self.frame,text="Quantidade:", height=2,width=12)
        self.txtQntde.grid(row=4,column=1)

        self.qntde = Entry(self.frame)
        self.qntde.grid(row=4,column=2)

        self.btnInserir = Button(self.frame,text="Salvar", height=2,width=18)
        self.btnInserir.grid(row=5,column=0,columnspan=2, rowspan=2)
        self.btnInserir["command"] = lambda:self.acaoBotaoInserir()

        self.btnCancelar = Button(self.frame,text='Cancelar', height=2,width=18)
        self.btnCancelar.grid(row=5,column=2,columnspan=2,rowspan=2)
        self.btnCancelar["command"] = lambda:self.acaoBotaoCancelar()

        self.__iniciaJanela()

        self.myRoot.protocol("WM_DELETE_WINDOW", lambda:self.__onclosing())
        root.mainloop()

    def acaoBotaoInserir(self):
        response = moduloCliente.adicionar(self.host, self.dia.get(), int(self.tanque.get()), int(self.qntde.get()), [self.hora.get()])
        print(response)
        self.__onclosing()

    def acaoBotaoCancelar(self):
        self.__onclosing()
    
    def __onclosing(self):
        self.myRoot.destroy()
        self.pai.restart()

    def __iniciaJanela(self):
        w = 300
        h = 300
        ws = self.myRoot.winfo_screenwidth()/2 - w/2
        hs = self.myRoot.winfo_screenheight()/2 - h/2
        self.myRoot.geometry('+%d+%d' % (ws,hs))
