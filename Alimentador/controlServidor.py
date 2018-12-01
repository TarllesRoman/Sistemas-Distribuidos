#coding: utf-8

import threading, json
import controlAgenda, modulo_bluetooth

class Control():
	def __init__(self):
		self.alimentar = False
		self.ler = False
		self.mensagem = ""
		self.cliente = []
		self.dic_operacoes = {'listar':self.listar,'adicionar':self.adicionar,'remover':self.remover}
		self.proxima = {} #proxima alimentação
		self.proxima_up = False; 

	def listar(self, alimentacao):
		response = {}
		try:
			response["alimentacoes"] = controlAgenda.get_alimentacoes()
			response["resultado"] = "Lista atualizada"
		except:
			response["resultado"] = "Falha ao buscar lista"
			response["alimentacoes"] = []
		return response

	def adicionar(self, alimentacao):
		response = {}
		try:
			controlAgenda.adicionar_alimentacoes(alimentacao)
			response["resultado"] = "Alimentacoes adicionadas"
		except:
			response["resultado"] = "Falha ao adicionar adicionar alimentacoes"
			
		response["alimentacoes"] = controlAgenda.get_alimentacoes()
		if "timestamp" in self.proxima:
			for alm in response["alimentacoes"]:
				if(alm["timestamp"] < self.proxima["timestamp"]):
					self.proxima = alm
					break
		else:
			self.update_proxima()
		return response

	def remover(self, alimentacao):
		response = {}
		try:
			if(controlAgenda.remover_alimentacao(alimentacao)):
				response["resultado"] = "Alimentação excluida"
			else:
				response["resultado"] = "Alimentação não encontrada"
		except:
			response["resultado"] = "Erro ao tentar excluir o arquivo"
			
		response["alimentacoes"] = controlAgenda.get_alimentacoes()
		return response

	def food_now(self):
		dados = {
            "tanque":self.proxima["tanque"],
            "tempo":self.proxima["quantidade"]
        }
		while(not modulo_bluetooth.connect()):
			pass
		modulo_bluetooth.send_json(dados)
		print(modulo_bluetooth.receive("!"))
		controlAgenda.remover(self.proxima)
		self.update_proxima()

	def update_proxima(self):
		alms = controlAgenda.get_alimentacoes()
		time_s = alms[0]["timestamp"]
		self.proxima = alms[0]
		for alm in alms:
			if(alm["timestamp"] < time_s):
				time_s = alm["timestamp"]
				self.proxima = alm
		return time_s

	def gramas_seconds(self):
		pass
