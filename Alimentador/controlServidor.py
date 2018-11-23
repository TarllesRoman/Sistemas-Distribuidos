#coding: utf-8

import controlAgenda

class Control():
	def __init__(self):
		self.alimentar = False
		self.ler = False
		self.mensagem = ""
		self.cliente = []
		self.dic_operacoes = {'listar':self.listar,'adicionar':self.adicionar,'remover':self.remover}

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

	def gramas_seconds(self):
		pass
