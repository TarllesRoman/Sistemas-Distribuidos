#coding: utf-8

from Tkinter import *
import json
import moduloCliente
from JAlimentacoes import *

class JLogin:
    
    def __init__(self, root):
        self.myRoot = root
        self.myRoot.title("Sistema de alimentação")
        self.frame = Frame(root)
        self.frame.pack()

        self.titulo = Label(self.frame, text="Logar no servidor")
        self.titulo.grid(row=0, column=0, columnspan=4)

        self.txtip = Label(self.frame, text="IP (servidor): ")
        self.txtip.grid(row=1,column=1)

        self.ip = Entry(self.frame)
	self.ip.insert(END,"192.168.0.103")
        self.ip.grid(row=1,column=2)

        self.txtsenha = Label(self.frame, text="Senha: ")
        self.txtsenha.grid(row=2,column=1)

        self.senha = Entry(self.frame)
        self.senha.grid(row=2,column=2)

        self.btnentrar = Button(self.frame, text="Entrar")
        self.btnentrar.grid(row=3,column=0,columnspan=2)
        self.btnentrar["command"] = lambda:self.acaoBotaoEntrar()

        self.btnsair = Button(self.frame,text="Sair")
        self.btnsair.grid(row=3,column=2,columnspan=2)
        self.btnsair["command"] = lambda:self.acaoBotaoSair()


        root.mainloop()

    def acaoBotaoEntrar(self):
        host = moduloCliente.Host(self.ip.get(),self.senha.get())
        response = moduloCliente.listar(host)
        self.myRoot.destroy()
	janela = Tk()
	JAlimentacoes(janela,json.loads(response),host)

    def acaoBotaoSair(self):
        self.myRoot.destroy()

