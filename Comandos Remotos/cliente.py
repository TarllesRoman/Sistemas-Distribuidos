#coding: utf-8

from socket import *

server_ip = '127.0.0.1'
server_port = 19199

clienteSocket = socket(AF_INET, SOCK_STREAM)

clienteSocket.connect((server_ip,server_port))

print "Digite ctrl+X para sair"
mensagem = raw_input("Digite uma mensagem: ")

while mensagem != '\x18':
	clienteSocket.send(mensagem.encode("utf-8"))
	
	resposta = clienteSocket.recv(2048)
	print "Resposta:", resposta 
	
	mensagem = raw_input("Digite uma mensagem: ")

print "saiu"
clienteSocket.close()
