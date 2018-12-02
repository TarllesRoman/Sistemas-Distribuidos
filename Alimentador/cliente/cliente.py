#coding: utf-8

from Tkinter import *
import moduloCliente
import json

print(moduloCliente.adicionar("01/12/2018",3, 5000,["23:12","23:13","23:14"]))

class JAlimentacoes:
    
    def __init__(self, root, dados):
        self.myRoot = root
        self.frame1 = Frame(root)
        self.frame1.pack(side=TOP)

        self.titulo = Label(self.frame1,text="Alimentações")
        self.titulo.pack()

        self.tabela = Frame(self.frame1, width=20, height=30)
        self.tabela.pack()
        self.alimentacoes = dados["alimentacoes"]
        
        for i in range(len(self.alimentacoes)):
            self.adicionar_alimentacao(self.alimentacoes[i],i)

        root.mainloop()

    def adicionar_alimentacao(self, alimentacao, i):
        dia = Label(self.tabela, text=alimentacao["dia"], height=2, width=10)
        dia.grid(row=i, column=0)

        hora = Label(self.tabela, text=alimentacao["hora"], height=2, width=10)
        hora.grid(row=i, column=1)

        quantidade = Label(self.tabela, text=alimentacao["quantidade"], height=2, width=10)
        quantidade.grid(row=i, column=2)

        btnDeletar = Button(self.tabela, text="Apagar", height=2, width=10)
        btnDeletar["command"] = lambda:self.acaoBotao(alimentacao)
        btnDeletar.grid(row=i, column=3)

    def acaoBotao(self, alimentacao):
        #print( moduloCliente.remover(alimentacao["dia"], alimentacao["tanque"], alimentacao["quantidade"], [alimentacao["hora"],]))
        self.myRoot.destroy()
        janela = Tk()
        response = moduloCliente.remover(alimentacao["dia"], alimentacao["tanque"], alimentacao["quantidade"], [alimentacao["hora"],])
        JAlimentacoes(janela, json.loads(response))
        
        
    
        
janela = Tk()
response = moduloCliente.listar()
JAlimentacoes(janela, json.loads(response))
