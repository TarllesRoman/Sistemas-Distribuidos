#coding: utf-8

from socket import *
import subprocess
import server_modulo
import json

UDP_port = 19198
receiver_port = 19197

receiver_socket = socket(AF_INET, SOCK_DGRAM)
receiver_socket.bind(('', receiver_port))

sender_socket = socket(AF_INET, SOCK_DGRAM)

tm_buffer = 2048

dic_operacoes = ('som', 'sub', 'div', 'mul')

def buscar_servidores(op):
	try:
		if(op not in dic_operacoes):
			print('Operacao não encontrada')
			return None

		f_serv = open('servers.list','r')
		serv = f_serv.read()
		f_serv.close()
		lista = json.loads(serv)
		return lista[op]
	except Exception as e:
		print(e)
		return None


while True:
	print ('Server pronto para aceitar conexao')
	
	try:
		message, client = receiver_socket.recvfrom(2048)

		message = message.decode('utf-8')
						
		print ('Mensagem recebida: '+message)

		lst_servidores = buscar_servidores(message)

		dic = {"servidores":lst_servidores}
		jso_response = json.dumps(dic)

		dest = (client[0],UDP_port)

		print('Resposta: '+jso_response+'       para: '+dest[0])

		sender_socket.sendto(bytes(jso_response,'utf-8'),dest)
	except Exception as e:
		print('ocorreu excecao'+str(e))
		receiver_socket.close()
		sender_socket.close()

		receiver_socket = socket(AF_INET, SOCK_DGRAM)
		receiver_socket.bind(('', receiver_port))
		sender_socket = socket(AF_INET, SOCK_DGRAM)