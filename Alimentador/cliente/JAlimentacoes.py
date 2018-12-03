#coding: utf-8

from Tkinter import *
import moduloCliente
import json
from JCadastraAlimentacao import *

class JAlimentacoes:
    
    def __init__(self, root, dados, host):
        self.myRoot = root
        self.myRoot.title("Alimentações")
	self.host = host

        self.modal_open = False

        self.frame1 = Frame(root)
        self.frame1.pack(side=TOP)

        self.menubar = Menu(root)
        self.menubar.add_command(label="Adicionar", command=self.adicionar)
        self.menubar.add_command(label="Atualizar", command=self.restart)

        self.tabela = Frame(self.frame1, width=20, height=30)
        self.tabela.pack()

        self.txtdata = Label(self.tabela,text="Data")
        self.txtdata.grid(row=0,column=0)
        self.txthora = Label(self.tabela,text="Hora")
        self.txthora.grid(row=0,column=1)
        self.txttanque = Label(self.tabela,text="Tanque")
        self.txttanque.grid(row=0,column=2)
        self.txtqnt = Label(self.tabela,text="Quantidade")
        self.txtqnt.grid(row=0,column=3)

        self.alimentacoes = dados["alimentacoes"]
        for i in range(len(self.alimentacoes)):
            self.adicionar_alimentacao(self.alimentacoes[i],i+1)

        root.config(menu=self.menubar)
        self.__iniciaJanela()
        root.mainloop()

    def adicionar_alimentacao(self, alimentacao, i):
        dia = Label(self.tabela, text=alimentacao["dia"], height=2, width=10)
        dia.grid(row=i, column=0)

        hora = Label(self.tabela, text=alimentacao["hora"], height=2, width=10)
        hora.grid(row=i, column=1)

        tanque = Label(self.tabela, text=alimentacao["tanque"], height=2, width=10)
        tanque.grid(row=i, column=2)
        
        quantidade = Label(self.tabela, text=alimentacao["quantidade"], height=2, width=10)
        quantidade.grid(row=i, column=3)
        

        btnDeletar = Button(self.tabela, text="Apagar", height=2, width=10)
        btnDeletar["command"] = lambda:self.acaoBotao(alimentacao)
        btnDeletar.grid(row=i, column=4)

    def acaoBotao(self, alimentacao):
        #print( moduloCliente.remover(alimentacao["dia"], alimentacao["tanque"], alimentacao["quantidade"], [alimentacao["hora"],]))
        self.myRoot.destroy()
        janela = Tk()
        response = moduloCliente.remover(self.host, alimentacao["dia"], alimentacao["tanque"], alimentacao["quantidade"], [alimentacao["hora"],])
        JAlimentacoes(janela, json.loads(response), self.host)

    def adicionar(self):
            if self.modal_open: 
                return
            else:
                self.modal_open = True
            janela = Tk()
            #response = moduloCliente.remover(alimentacao["dia"], alimentacao["tanque"], alimentacao["quantidade"], [alimentacao["hora"],])
            JCadastraAlimentacao(janela,self, self.host)
            self.modal_open = True

    def restart(self):
        self.myRoot.destroy()
        janela = Tk()
        response = moduloCliente.listar(self.host)
        JAlimentacoes(janela, json.loads(response), self.host)

    def __iniciaJanela(self):
        w = 300
        h = 300
        ws = self.myRoot.winfo_screenwidth()/2 - w/2
        hs = self.myRoot.winfo_screenheight()/2 - h/2
        self.myRoot.geometry('+%d+%d' % (ws,hs))
    
