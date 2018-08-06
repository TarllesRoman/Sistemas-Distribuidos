#coding: utf-8

server_port = 19199

from socket import *
import subprocess
import os

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
			
		print "Mensagem recebida: ",message.decode("utf-8")
		resultado = subprocess.call(message.decode("utf-8") + " >> temp.txt", shell=True)
		
		conexao.send(open("temp.txt","r").read())
		
		os.remove("temp.txt")
	
serverSocket.close()
