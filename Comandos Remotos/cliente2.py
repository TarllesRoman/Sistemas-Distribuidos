#coding: utf-8

from socket import *
import subprocess
import commands

server_ip = '127.0.0.1'
server_port = 19199

serverOFF = False

mensagem = ""
tm_zfill = 10
tm_buffer = 2048

clienteSocket = socket(AF_INET, SOCK_STREAM)

def server_on():
	global server_ip
	global server_port
	global serverOFF
	global mensagem
	global clienteSocket
	
	try:
		print "Conectado ao servidor!"
		while mensagem != '\x18':
			clienteSocket.send(mensagem.encode("utf-8"))
				
			resposta = clienteSocket.recv(tm_buffer)
			tamanho = int(resposta[0:tm_zfill])
			respostaCompleta = resposta[tm_zfill:]
			qtdLida = tm_buffer - tm_zfill
			while(qtdLida < tamanho):
				respostaCompleta += clienteSocket.recv(tm_buffer)
				qtdLida += tm_buffer
			
			if(resposta == ""):
				server_off()
			print "Resposta:", respostaCompleta
				
			mensagem = raw_input("Digite uma mensagem: ")
	except:
		clienteSocket.close()
		serverOFF = True
		server_off()			
			

def server_off():
	global server_ip
	global server_port
	global serverOFF
	global mensagem
	
	print "Executando localmente"
	while mensagem != '\x18':
		print "Resposta:", commands.getoutput(mensagem) 
		mensagem = raw_input("Digite uma mensagem: ")
		connect()
		if(not serverOFF):
			server_on()


def connect():
	global server_ip
	global server_port
	global serverOFF
	global clienteSocket
	
	try:
		clienteSocket = socket(AF_INET, SOCK_STREAM)
		clienteSocket.connect((server_ip,server_port))
		serverOFF = False
	except Exception as e:
		serverOFF = True


connect()
print "Digite ctrl+X para sair"
mensagem = raw_input("Digite uma mensagem: ")

if serverOFF:
	server_off()
else:
	server_on()

clienteSocket.close()
