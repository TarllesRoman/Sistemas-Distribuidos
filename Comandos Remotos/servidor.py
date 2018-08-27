#coding: utf-8

server_port = 19199

from socket import *
import subprocess
import commands

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', server_port))
serverSocket.listen(1)

cmdSemResposta = "Comando sem resposta"
tm_zfill = 10
tm_buffer = 2048

while True:
	print "Server pronto para aceitar conexao"
	
	conexao, cliente = serverSocket.accept()
	print "Conexao aceita"
	
	while True:
		message = conexao.recv(tm_buffer)
		
		if(message=="EXIT"):
			print "Conexao encerrada"
			conexao.close()
			break
			
		print "Mensagem recebida: ",message.decode("utf-8")
		resultado = commands.getoutput(message.decode("utf-8"))
		if(resultado == ""):
			conexao.send(str(len(cmdSemResposta)).zfill(tm_zfill)+cmdSemResposta)
		else:
			conexao.send(str(len(resultado)).zfill(tm_zfill)+resultado)
	
serverSocket.close()
