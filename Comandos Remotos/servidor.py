#coding: utf-8

server_port = 19199

from socket import *
import subprocess
import commands

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)


while True:
	print "Server pronto para aceitar conexao"
	
	conexao, cliente = serverSocket.accept()
	print "Conexao aceita"

	while True:		
		message = conexao.recv(2048)
		
		if(message == ""):
			print "Conexao encerrada"
			conexao.close()
			break;
		if(message=="EXIT")
			print "Conexao encerrada"
			conexao.close()
			break;
			
		print "Mensagem recebida: ",message.decode("utf-8")
		resultado = commands.getoutput(message.decode("utf-8"))
		
		conexao.send(resultado)
	
serverSocket.close()
