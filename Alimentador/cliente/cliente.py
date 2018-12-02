#coding: utf-8

from Tkinter import *
import json
import moduloCliente
import JAlimentacoes
from JCadastraAlimentacao import *

#print(moduloCliente.adicionar("01/12/2018",2, 5000,["23:51","23:52","23:53"]))


janela = Tk()


response = moduloCliente.listar()
JAlimentacoes.JAlimentacoes(janela, json.loads(response))
